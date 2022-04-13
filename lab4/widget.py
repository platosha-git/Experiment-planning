from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from equationwindow import *
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
        self.btn_full.clicked.connect(self.show_full_equasion)

        self.b = list()
        self.equation_window = EquationWindow()

        self.star_length = calc_star_length()
        self.label_length.setText(str(self.star_length))

        self.star_shift = calc_star_shift()
        self.label_a.setText(str(self.star_shift))

        for i in range(1, EXP_AMOUNT + 2):
            self.table_plan.setItem(i, 0, QTableWidgetItem(str(i)))
        self.fill_table()

        self.show()


    def get_factor(self, entry):
        delta = 1e-10
        res = get_valid(entry, float, lambda val: False)

        if abs(res) < delta:
            res = delta

        return res


    def check_factors(self):
        passed = True
        entries = [
            [self.entry_gen1_int_min, self.entry_gen1_int_max],
            [self.entry_gen2_int_min, self.entry_gen2_int_max],
            [self.entry_proc1_int_min, self.entry_proc1_int_max],
            [self.entry_proc1_dev_min, self.entry_proc1_dev_max],
            [self.entry_proc2_int_min, self.entry_proc2_int_max],
            [self.entry_proc2_dev_min, self.entry_proc2_dev_max]
        ]

        for i in range(len(entries)):
            try:
                min_val = self.get_factor(entries[i][0])
                max_val = self.get_factor(entries[i][1])

                if -self.star_length < -1 - 2 * min_val / (max_val - min_val):
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
                gen2_int_min = self.get_factor(self.entry_gen2_int_min)
                gen2_int_max = self.get_factor(self.entry_gen2_int_max)
                proc1_int_min = self.get_factor(self.entry_proc1_int_min)
                proc1_int_max = self.get_factor(self.entry_proc1_int_max)
                proc1_dev_min = self.get_factor(self.entry_proc1_dev_min)
                proc1_dev_max = self.get_factor(self.entry_proc1_dev_max)
                proc2_int_min = self.get_factor(self.entry_proc2_int_min)
                proc2_int_max = self.get_factor(self.entry_proc2_int_max)
                proc2_dev_min = self.get_factor(self.entry_proc2_dev_min)
                proc2_dev_max = self.get_factor(self.entry_proc2_dev_max)
            except ValueError:
                pass

            else:
                y = list()

                # for each experiment
                for exp in self.plan:
                    gen_int1 = scale_factor(exp[1], gen1_int_min, gen1_int_max)
                    gen_int2 = scale_factor(exp[2], gen2_int_min, gen2_int_max)

                    proc_int1 = scale_factor(exp[3], proc1_int_min, proc1_int_max)
                    proc_dev1 = scale_factor(exp[4], proc1_dev_min, proc1_dev_max)
                    
                    proc_int2 = scale_factor(exp[5], proc2_int_min, proc2_int_max)
                    proc_dev2 = scale_factor(exp[6], proc2_dev_min, proc2_dev_max)

                    gens = [Generator(exp_by_intensity, (gen_int1,)), Generator(exp_by_intensity, (gen_int2,))]
                    procs = [Generator(norm_by_intensity, (proc_int1, proc_dev1)),
                             Generator(norm_by_intensity, (proc_int2, proc_dev2))]
                    model = EventModel(gens, procs, total_apps)

                    y.append(model.proceed() / total_apps)


                for i in range(len(self.custom_plan)):
                    if len(self.custom_plan[i]) > 0:
                        gen_int1 = scale_factor(self.custom_plan[i][1], gen1_int_min, gen1_int_max)
                        gen_int2 = scale_factor(self.custom_plan[i][2], gen2_int_min, gen2_int_max)
                        
                        proc_int1 = scale_factor(self.custom_plan[i][3], proc1_int_min, proc1_int_max)
                        proc_dev1 = scale_factor(self.custom_plan[i][4], proc1_dev_min, proc1_dev_max)
                        
                        proc_int2 = scale_factor(self.custom_plan[i][5], proc2_int_min, proc2_int_max)
                        proc_dev2 = scale_factor(self.custom_plan[i][6], proc2_dev_min, proc2_dev_max)

                        gens = [Generator(exp_by_intensity, (gen_int1,)),
                                Generator(exp_by_intensity, (gen_int2,))]
                        procs = [Generator(norm_by_intensity, (proc_int1, proc_dev1)),
                                 Generator(norm_by_intensity, (proc_int2, proc_dev2))]
                        model = EventModel(gens, procs, total_apps)

                        y.append(model.proceed() / total_apps)

                else:
                    y.append(None)

                self.b = expand_plan(self.plan, self.custom_plan, y)

                self.fill_table()
                self.set_equasion()


    def fill_table(self):
        for i in range(len(self.plan)):
            for j in range(len(self.plan[i])):
                self.table_plan.setItem(i + 1, j + 1, QTableWidgetItem(str(round(self.plan[i][j], 3))))

        for i in range(len(self.custom_plan)):
            for j in range(len(self.custom_plan[i])):
                self.table_plan.setItem(i + len(self.plan) + 1, j + 1,
                                        QTableWidgetItem(str(round(self.custom_plan[i][j], 3))))


    def set_equasion(self, accuracy=3):
        if len(self.b) == 70:
            y = form_equasion(self.b, accuracy)
            y = y.replace("+ -", "- ")
            y = y.replace("+ \n-", "-\n")
            self.label_y.setText(y)


    def show_full_equasion(self):
        accuracy = 3
        if len(self.b) == 70:
            y = form_full_equasion(self.b, accuracy)
            y = y.replace("+ -", "- ")
            y = y.replace("+ \n-", "-\n")
            self.equation_window.show(y)


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
            self.custom_plan[0].extend(shifted_points(factors, self.star_length))

            for i in range(len(self.custom_plan)):
                for j in range(len(self.custom_plan[i])):
                    self.table_plan.setItem(78, j + 1, QTableWidgetItem(str(round(self.custom_plan[i][j], 3))))
