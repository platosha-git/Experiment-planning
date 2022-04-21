from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from experiment_math import *
from model import *
from validentry import *
from form_equation import *


def scale_factor(x, realmin, realmax, xmin=-1, xmax=1):
    return realmin + (realmax - realmin) * (x - xmin) / (xmax - xmin)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('widget.ui', self)

        self.plan = matrix_plan()
        self.custom_plan = [list()]

        self.btn_do_plan.clicked.connect(self.do_plan)
        self.btn_set.clicked.connect(self.set)

        self.b = list()

        self.S = S_calculate()
        self.label_a.setText(str(round(self.S, 4)))

        self.ALPHA = ALPHA_calculate()
        self.label_length.setText(str(round(self.ALPHA, 4)))

        for i in range(1, EXP_NUMBER + 2):
            self.table_plan.setItem(i, 0, QTableWidgetItem(str(i)))
        self.fill_table()

        self.show()


    def get_entries(self):
        return [[self.entry_gen1_int_min, self.entry_gen1_int_max],
                [self.entry_gen1_var_min, self.entry_gen1_var_max],
                [self.entry_proc1_int_min, self.entry_proc1_int_max],
                [self.entry_gen2_int_min, self.entry_gen2_int_max],
                [self.entry_gen2_var_min, self.entry_gen2_var_max],
                [self.entry_proc2_int_min, self.entry_proc2_int_max]]


    def get_factor(self, entry):
        delta = 1e-10
        res = get_valid(entry, float, lambda val: False)

        if abs(res) < delta:
            res = delta

        return res


    def check_factors(self):
        passed = True
        entries = self.get_entries()

        for i in range(len(entries)):
            try:
                min_val = self.get_factor(entries[i][0])
                max_val = self.get_factor(entries[i][1])

                if -self.ALPHA < -1 - 2 * min_val / (max_val - min_val):
                    make_invalid(entries[i][0])
                    make_invalid(entries[i][1])
                    passed = False
                else:
                    make_valid(entries[i][0])
                    make_valid(entries[i][1])
            
            except ValueError:
                pass

        return passed


    def do_plan(self):
        if self.check_factors():
            self.plan = matrix_plan()
            total_apps = 10000

            try:
                gen1_int_min = self.get_factor(self.entry_gen1_int_min)
                gen1_int_max = self.get_factor(self.entry_gen1_int_max)

                gen1_var_min = self.get_factor(self.entry_gen1_var_min)
                gen1_var_max = self.get_factor(self.entry_gen1_var_max)

                gen2_int_min = self.get_factor(self.entry_gen2_int_min)
                gen2_int_max = self.get_factor(self.entry_gen2_int_max)

                gen2_var_min = self.get_factor(self.entry_gen2_var_min)
                gen2_var_max = self.get_factor(self.entry_gen2_var_max)
                
                proc1_int_min = self.get_factor(self.entry_proc1_int_min)
                proc1_int_max = self.get_factor(self.entry_proc1_int_max)

                proc2_int_min = self.get_factor(self.entry_proc2_int_min)
                proc2_int_max = self.get_factor(self.entry_proc2_int_max)

            except ValueError:
                pass

            else:
                y = list()

                for exp in self.plan:
                    gen_int1 = scale_factor(exp[1], gen1_int_min, gen1_int_max)
                    gen_var1 = scale_factor(exp[2], gen1_var_min, gen1_var_max)
                    proc_int1 = scale_factor(exp[3], proc1_int_min, proc1_int_max)

                    gen_int2 = scale_factor(exp[4], gen2_int_min, gen2_int_max)
                    gen_var2 = scale_factor(exp[5], gen2_var_min, gen2_var_max)
                    proc_int2 = scale_factor(exp[6], proc2_int_min, proc2_int_max)

                    gens = [Generator(uniform_by_intensity, (gen_int1, gen_var1)), 
                            Generator(uniform_by_intensity, (gen_int2, gen_var2))]
                    procs = [Generator(exp_by_intensity, (proc_int1,)), Generator(exp_by_intensity, (proc_int2,))]
                    
                    model = EventModel(gens, procs, total_apps)
                    res = model.proceed()

                    y.append(res / total_apps)


                for i in range(len(self.custom_plan)):
                    if len(self.custom_plan[i]) > 0:
                        gen_int1 = scale_factor(self.custom_plan[i][1], gen1_int_min, gen1_int_max)
                        gen_var1 = scale_factor(self.custom_plan[i][2], gen1_var_min, gen1_var_max)
                        proc_int1 = scale_factor(self.custom_plan[i][3], proc1_int_min, proc1_int_max)

                        gen_int2 = scale_factor(self.custom_plan[i][4], gen2_int_min, gen2_int_max)
                        gen_var2 = scale_factor(self.custom_plan[i][5], gen2_var_min, gen2_var_max)
                        proc_int2 = scale_factor(self.custom_plan[i][6], proc2_int_min, proc2_int_max)

                        gens = [Generator(uniform_by_intensity, (gen_int1, gen_var1)), 
                                Generator(uniform_by_intensity, (gen_int2, gen_var2))]

                        procs = [Generator(exp_by_intensity, (proc_int1,)), Generator(exp_by_intensity, (proc_int2,))]
                        model = EventModel(gens, procs, total_apps)
                        res = model.proceed()

                        y.append(res / total_apps)

                else:
                    y.append(None)

                self.b = expand_plan(self.plan, self.custom_plan, y)

                self.fill_table()
                self.show_full_equasion()


    def fill_table(self):
        for i in range(len(self.plan)):
            for j in range(len(self.plan[i])):
                self.table_plan.setItem(i + 1, j + 1, QTableWidgetItem(str(round(self.plan[i][j], 3))))

        for i in range(len(self.custom_plan)):
            for j in range(len(self.custom_plan[i])):
                self.table_plan.setItem(i + len(self.plan) + 1, j + 1,
                                        QTableWidgetItem(str(round(self.custom_plan[i][j], 3))))


    def show_full_equasion(self):
        accuracy = 4
        if len(self.b) == 70:
            entries = self.get_entries()
            y = form_equasion(self.b, self.S, accuracy, entries)
            y = y.replace("+ -", "- ")
            y = y.replace("+ \n-", "-\n")
            self.label_y.setText(y)
            #self.equation_window.show(y)


    def set(self):
        try:
            x1 = get_valid(self.entry_x1, float, lambda val: val < -1 or val > 1)
            x2 = get_valid(self.entry_x2, float, lambda val: val < -1 or val > 1)
            x3 = get_valid(self.entry_x3, float, lambda val: val < -1 or val > 1)
            x4 = get_valid(self.entry_x4, float, lambda val: val < -1 or val > 1)
            x5 = get_valid(self.entry_x5, float, lambda val: val < -1 or val > 1)
            x6 = get_valid(self.entry_x6, float, lambda val: val < -1 or val > 1)
        
        except ValueError:
            pass

        else:
            factors = [x1, x2, x3, x4, x5, x6]

            self.custom_plan[0] = [1]
            self.custom_plan[0].extend(factors)
            self.custom_plan[0].extend(combination(factors))
            self.custom_plan[0].extend(shifted_points(factors, self.ALPHA))

            for i in range(len(self.custom_plan)):
                for j in range(len(self.custom_plan[i])):
                    self.table_plan.setItem(78, j + 1, QTableWidgetItem(str(round(self.custom_plan[i][j], 3))))
