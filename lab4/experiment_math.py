import numpy as np
import itertools as it

FACTORS_NUMBER = 6
N = 2 ** FACTORS_NUMBER
EXP_NUMBER = 2 ** FACTORS_NUMBER + 2 * FACTORS_NUMBER + 1


def S_calculate():
    return np.sqrt(N / EXP_NUMBER)


def ALPHA_calculate():
    return np.sqrt((N / 2) * (np.sqrt(EXP_NUMBER / N) - 1))


def combination(factors):
    res = list()
    for length in range(2, len(factors) + 1):
        for subset in it.combinations(factors, length):
            res.append(np.prod(subset))
    return res


def shifted_points(factors, a):
    res = list()
    for f in factors:
        res.append(f ** 2 - a)
    return res


def fill_factors(plan):
    step = 1
    for j in range(FACTORS_NUMBER):
        sign = -1
        for i in range(N):
            plan[i][j + 1] = sign
            if (i + 1) % step == 0:
                sign *= -1
        step *= 2


def fill_star_sides(plan):
    sign = -1
    factori = 0
    alpha = ALPHA_calculate()

    for i in range(N, EXP_NUMBER - 1):
        factors = [0] * FACTORS_NUMBER
        factors[factori] = sign * alpha
        plan[i].extend(factors)
        if sign == 1:
            factori += 1
            sign = -1
        else:
            sign = 1


def fill_star_center(plan):
    s = S_calculate()
    plan[EXP_NUMBER - 1].extend([0] * (N - 1))
    plan[EXP_NUMBER - 1].extend([-s] * FACTORS_NUMBER)


def matrix_plan():
    res = [[1 for i in range(1 + FACTORS_NUMBER)] for j in range(N)]
    res.extend([[1 for i in range(1)] for j in range(EXP_NUMBER - N)])

    fill_factors(res)
    fill_star_sides(res)
    fill_star_center(res)

    s = S_calculate()
    for i in range(EXP_NUMBER - 1):
        res[i].extend(combination(res[i][1:FACTORS_NUMBER + 1]))
        res[i].extend(shifted_points(res[i][1:FACTORS_NUMBER + 1], s))

    return res


def calc_b(plan, y):
    b = list()
    for i in range(len(plan[0])):
        xy = xx = 0
        for j in range(len(plan)):
            xy += plan[j][i] * y[j]
            xx += plan[j][i] ** 2
        b.append(xy / xx)
    return b


def calc_y(b, x):
    res = 0
    for i in range(len(b)):
        res += b[i] * x[i]
    return res


def fill_y(plan, b):
    ycalc = list()
    for i in range(len(plan)):
        if len(plan[i]):
            ycalc.append(calc_y(b, plan[i]))
    return ycalc


def fill_plan(plan, y, ycalc):
    for i in range(len(plan)):
        if len(plan[i]):
            plan[i].append(y[i])
            plan[i].append(ycalc[i])
            plan[i].append(abs(y[i] - ycalc[i]))


def expand_plan(plan, custom_plan, y):
    b = calc_b(plan, y)

    ycalc = fill_y(plan, b)
    fill_plan(plan, y, ycalc)
    ycalc = fill_y(custom_plan, b)
    if len(custom_plan) > 0:
        fill_plan(custom_plan, y[len(plan):], ycalc)

    return b
