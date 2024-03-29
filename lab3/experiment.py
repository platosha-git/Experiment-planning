from smo import modelling
from prettytable import PrettyTable

import matplotlib.pyplot as plt
import numpy as np
import math
import random
from itertools import *

FACTORS_NUMBER = 6
MATR_SIZE = 2**FACTORS_NUMBER

REPLICA = 2
PARTIAL_MATR_SIZE = 2**(FACTORS_NUMBER - REPLICA)
FULL_COEF_NUMBER = 22
PARTIAL_COEF_NUMBER = 16

MOD_NUMBER = 1 # Лучше брать 10

CHECK_FULL = 1
CHECK_PARTIAL = 2

class Experiment():
    def __init__(self, gen_1, gen_2, pm_1, pm_2, time):
        self.min_gen_int = [gen_1[0], gen_2[0]]
        self.max_gen_int = [gen_1[1], gen_2[1]]
        self.min_gen_var = [gen_1[2], gen_2[2]]
        self.max_gen_var = [gen_1[3], gen_2[3]]

        self.min_pm_int = [pm_1[0], pm_2[0]]
        self.max_pm_int = [pm_1[1], pm_2[1]]

        self.time = time
        self.full_b = []
        self.partial_b = []
    
    def get_full_matrix(self):
        matrix = [[0 for i in range(FULL_COEF_NUMBER)] for i in range(MATR_SIZE)]
        
        for i in range(MATR_SIZE):
            x = []
            for j in range(1, FACTORS_NUMBER + 1):
                if i // (2 ** (j - 1)) % 2 == 1:
                    matrix[i][j] = -1
                else:
                    matrix[i][j] = 1
                x.append(matrix[i][j])

            matrix[i][0] = 1

            pos = FACTORS_NUMBER + 1
            for j in range(2, 3):
                for comb in combinations(x, j):
                    matrix[i][pos] = 1
                    for item in comb:
                        matrix[i][pos] *= item
                    pos += 1

        return matrix
    
    
    def get_partial_matrix(self):
        matrix = [[0 for i in range(PARTIAL_COEF_NUMBER)] for i in range(PARTIAL_MATR_SIZE)]
        
        for i in range(PARTIAL_MATR_SIZE):
            matrix[i][0] = 1
            for j in range(1, FACTORS_NUMBER - 1):
                if i // (2 ** (j - 1)) % 2 == 1:
                    matrix[i][j] = -1
                else:
                    matrix[i][j] = 1

            matrix[i][5] = matrix[i][2] * matrix[i][3] * matrix[i][4]
            matrix[i][6] = matrix[i][1] * matrix[i][2] * matrix[i][3] * matrix[i][4]

            # x1x2
            matrix[i][7] = matrix[i][1] * matrix[i][2]
            # x1x3
            matrix[i][8] = matrix[i][1] * matrix[i][3]
            # x1x4
            matrix[i][9] = matrix[i][1] * matrix[i][4]
            # x2x3
            matrix[i][10] = matrix[i][2] * matrix[i][3]
            # x2x4
            matrix[i][11] = matrix[i][2] * matrix[i][4]
            # x2x5
            matrix[i][12] = matrix[i][2] * matrix[i][5]
            # x2x6
            matrix[i][13] = matrix[i][2] * matrix[i][6]
            # x3x6
            matrix[i][14] = matrix[i][3] * matrix[i][6]
            # x4x6
            matrix[i][15] = matrix[i][4] * matrix[i][6]

        return matrix

    def calc_b_full(self, plan, y):
        b = list()
        for i in range(len(plan[0])):
            b_cur = 0
            for j in range(len(plan)):
                b_cur += plan[j][i] * y[j]
            b.append(b_cur / len(plan))
        return b

    def calc_b_partial(self, plan, y):
        b = list()
        for i in range(int(np.log2(len(plan))) + 3):
            b_cur = 0
            for j in range(len(plan)):
                b_cur += plan[j][i] * y[j]
            b.append(b_cur / len(plan))
        for i in range(int(np.log2(len(plan))) + 3, len(plan[0])):
            b_cur = 0
            for j in range(len(plan)):
                b_cur += plan[j][i] * y[j]
            b.append(b_cur / len(plan) / 2)

        b_particial = []
        b_particial.append(b[0])
        b_particial.append(b[1])
        b_particial.append(b[2])
        b_particial.append(b[3])
        b_particial.append(b[4])
        b_particial.append(b[5])
        b_particial.append(b[6])
        b_particial.append(b[7])  # x1x2
        b_particial.append(b[8])  # x1x3
        b_particial.append(b[9])  # x1x4
        b_particial.append(b[10])  # x2x3
        b_particial.append(b[11])  # x2x4
        b_particial.append(b[12])  # x2x5
        b_particial.append(b[13])  # x2x6
        b_particial.append(b[14])  # x3x6
        b_particial.append(b[15])  # x4x6

        return b_particial

    def calc_y(self, b, x):
        res = 0
        if (len(b) <= len(x)):
            for i in range(len(b)):
                res += b[i] * x[i]
        else:
            for i in range(len(x)):
                res += b[i] * x[i]
        return res

    def fill_y(self, plan, b1, b2):
        ylin = list()
        ynlin = list()
        for i in range(len(plan)):
            if len(plan[i]):
                ylin.append(self.calc_y(b1, plan[i]))
                ynlin.append(self.calc_y(b2, plan[i]))
        return ylin, ynlin

    def fill_plan(self, plan, y, ylin, ynlin):
        for i in range(len(plan)):
            if len(plan[i]):
                plan[i].append(y[i])
                plan[i].append(ylin[i])
                plan[i].append(ynlin[i])
                plan[i].append(abs(y[i] - ylin[i]))
                plan[i].append(abs(y[i] - ynlin[i]))


    def expand_full_plan(self, plan, y):
        b = self.calc_b_full(plan, y)

        ylin, ynlin = self.fill_y(plan, b[:int(np.log2(len(b))) + 1], b)
        self.fill_plan(plan, y, ylin, ynlin)

        return b


    def expand_partial_plan(self, plan, y):
        b = self.calc_b_partial(plan, y)

        ylin, ynlin = self.fill_y(plan, b[:int(np.log2(len(b))) + 1], b)
        self.fill_plan(plan, y, ylin, ynlin)

        return b

    def convert_to_unif_param(self, intens, var):
        a = 1/intens - math.sqrt(3/var)
        b = 1/intens + math.sqrt(3/var)
        if a < 0:
            a = 1e-10
            b = 2/intens
        return a, b

    def convert_to_weibull_param(self, intens, var):
        intens = 1/intens
        var = 1/var
        weib_a = (var/intens)**(-1.086)
        weib_lamb = intens/(math.gamma(1 + 1/weib_a))
        if weib_a < 0:
            weib_a = 1e-10
        if weib_lamb < 0:
            weib_lamb = 1e-10
        return weib_a, weib_lamb

    def convert_to_normal_param(self, intens, var):
        return 1/intens, 1/var
    
    def convert_to_exp_param(self, intens):
        return 1/intens

    def params_convert(self, gen_int, gen_var, pm_int, pm_var):
        a1, b1 = self.convert_to_unif_param(gen_int[0], gen_var[0])
        a2, b2 = self.convert_to_unif_param(gen_int[1], gen_var[1])
        
        lamb1 = self.convert_to_exp_param(pm_int[0])
        lamb2 = self.convert_to_exp_param(pm_int[1])

        return [a1, a2], [b1, b2], [lamb1, lamb2]

    def scale_factor(self, x, realmin, realmax, xmin=-1, xmax=1):
        return realmin + (realmax - realmin) * (x - xmin) / (xmax - xmin)

    def point_scaling(self, x):
        gen_int = []
        gen_int.append(self.scale_factor(x[0], self.min_gen_int[0], self.max_gen_int[0]))
        gen_int.append(self.scale_factor(x[3], self.min_gen_int[1], self.max_gen_int[1]))

        gen_var = []
        gen_var.append(self.scale_factor(x[1], self.min_gen_var[0], self.max_gen_var[0]))
        gen_var.append(self.scale_factor(x[4], self.min_gen_var[1], self.max_gen_var[1]))

        pm_int = []
        pm_int.append(self.scale_factor(x[2], self.min_pm_int[0], self.max_pm_int[0]))
        pm_int.append(self.scale_factor(x[5], self.min_pm_int[1], self.max_pm_int[1]))

        pm_var = []
        # pm_var.append(self.scale_factor(x[3], self.min_pm_var[0], self.max_pm_var[0]))
        # pm_var.append(self.scale_factor(x[5], self.min_pm_var[1], self.max_pm_var[1]))

        return gen_int, gen_var, pm_int, pm_var

    def calc_exp_y(self, matr):
        y = []
        for exp in matr:
            gen_int, gen_var, pm_int, pm_var = self.point_scaling(exp[1:(FACTORS_NUMBER + 1)])
            a, b, lamb = self.params_convert(gen_int, gen_var, pm_int, pm_var)

            exp_res = 0
            for i in range(MOD_NUMBER):
                avg_wait_time = modelling(a, b, lamb, self.time)
                exp_res += avg_wait_time
            exp_res /= MOD_NUMBER

            y.append(exp_res)
        return y

    def calculate(self):
        full_matrix = self.get_full_matrix()
        partial_matrix = self.get_partial_matrix()

        full_y = self.calc_exp_y(full_matrix)
        partial_y = self.calc_exp_y(partial_matrix)

        self.full_b = self.expand_full_plan(full_matrix, full_y)
        self.partial_b = self.expand_partial_plan(partial_matrix, partial_y)

        return self.full_b, self.partial_b, full_matrix, partial_matrix

    def calc_nonlin_plan(self, point, typeDfo=False):
        if (typeDfo == True):
            point.insert(0, 1)
            return point + [point[1]*point[2], point[1]*point[3], point[1]*point[4], point[2]*point[3], point[2]*point[4], point[2]*point[5], point[2]*point[6], point[3]*point[6], point[4]*point[6]]

        comb_x = [1]
        pos = 1

        for i in range(1, 3):
            for comb in combinations(point, i):
                cur_comb = 1
                for item in comb:
                    cur_comb *= item
                comb_x.append(cur_comb)
                pos += 1

        return comb_x

    def check(self, point, mode):
        exp_y = 0
        for i in range(MOD_NUMBER):
            gen_int, gen_var, pm_int, pm_var = self.point_scaling(point)
            a, b, lamb = self.params_convert(gen_int, gen_var, pm_int, pm_var)

            avg_wait_time = modelling(a, b, lamb, self.time)
            exp_y += avg_wait_time
         
        exp_y /= MOD_NUMBER

        if mode == CHECK_FULL:
            b = self.full_b
            nonlin_x_comb = self.calc_nonlin_plan(point)
        else:
            b = self.partial_b
            nonlin_x_comb = self.calc_nonlin_plan(point, True)


        lin_y = self.calc_y(b[:(FACTORS_NUMBER + 1)], [1] + point)
        nonlin_y = self.calc_y(b, nonlin_x_comb)
        res = nonlin_x_comb + [exp_y, lin_y, nonlin_y, abs(exp_y - lin_y), abs(exp_y - nonlin_y)]
        
        return res
