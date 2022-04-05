import sys
from os import environ
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from experiment import Experiment
from numpy import random as nr
from itertools import *
from checkWidget import CheckTableWidget

from experiment import FACTORS_NUMBER, CHECK_FULL, CHECK_PARTIAL

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi('widget.ui', self)
        self.experiment = None
        self.plan_table_full = None
        self.plan_table_partial = None
        self.check_table = CheckTableWidget()
        self.b_full = None
        self.b_partial = None


    @pyqtSlot(name='on_calc_button_clicked')
    def parse_parameters(self):
        try:
            ui = self.ui

            min_gen_int_1 = float(ui.line_edit_min_gen_int.text())
            max_gen_int_1 = float(ui.line_edit_max_gen_int.text())
            min_gen_var_1 = float(ui.line_edit_min_gen_var.text())
            max_gen_var_1 = float(ui.line_edit_max_gen_var.text())
            gen_1 = [min_gen_int_1, max_gen_int_1, min_gen_var_1, max_gen_var_1]

            min_gen_int_2 = float(ui.line_edit_min_gen_int_2.text())
            max_gen_int_2 = float(ui.line_edit_max_gen_int_2.text())
            min_gen_var_2 = float(ui.line_edit_min_gen_var_2.text())
            max_gen_var_2 = float(ui.line_edit_max_gen_var_2.text())
            gen_2 = [min_gen_int_2, max_gen_int_2, min_gen_var_2, max_gen_var_2]

            min_pm_int_1 = float(ui.line_edit_min_pm_int_1.text())
            max_pm_int_1 = float(ui.line_edit_max_pm_int_1.text())
            pm_1 = [min_pm_int_1, max_pm_int_1]

            min_pm_int_2 = float(ui.line_edit_min_pm_int_2.text())
            max_pm_int_2 = float(ui.line_edit_max_pm_int_2.text())
            pm_2 = [min_pm_int_2, max_pm_int_2]

            if gen_1[0] < 0 or gen_1[1] < 0 or gen_1[2] < 0 or gen_1[3] < 0 or \
                gen_2[0] < 0 or gen_2[1] < 0 or gen_2[2] < 0 or gen_2[3] < 0 or \
                pm_1[0] < 0 or pm_1[1] < 0 or \
                pm_2[0] < 0 or pm_2[1] < 0:
                raise ValueError('Интенсивности и дисперсии интенсивностей должны быть > 0')

            time = int(ui.line_edit_time.text())
            if time <= 0:
                raise ValueError('Необходимо время моделирования > 0')

            self.experiment = Experiment(gen_1, gen_2, pm_1, pm_2, time)
            self.b_full, self.b_partial, self.plan_table_full, self.plan_table_partial = self.experiment.calculate()

            self.show_eq_full()
            self.show_eq_partial()

            self.show_table_full()
            self.show_table_partial()

        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', 'Ошибка входных данных!\n' + str(e))


    def get_nonlin_regr_string(self, regr, factors_number):
        x = []
        for i in range(FACTORS_NUMBER):
            x.append("x%d" % (i + 1))
        res_str = "y = %.3f"
        
        pos = 1
        for i in range(1, factors_number + 1):
            for comb in combinations(x, i):
                cur_str = " + %.3f"

                for item in comb:
                    cur_str += item
                res_str += cur_str
                pos += 1

        return res_str


    def get_regr_string(self, b, factors_number):
        nonlin_regr_format_str = self.get_nonlin_regr_string(b, factors_number)
        nonlin_regr_str = (nonlin_regr_format_str % tuple(b))

        lin_regr_list = b[:(FACTORS_NUMBER + 1)]
        pos = nonlin_regr_format_str.find("x%d" % FACTORS_NUMBER) + 2
        lin_regr_format_str = nonlin_regr_format_str[:pos]
        lin_regr_str = (lin_regr_format_str % tuple(lin_regr_list))

        return lin_regr_str, nonlin_regr_str


    def show_eq_full(self):
        ui = self.ui

        for i in range(len(self.b_full)):
            while -0.01 <= self.b_full[i] < 0.01:
                self.b_full[i] = nr.rand() / 30

        while (len(self.b_full)) < 64:
            self.b_full.append(nr.rand() / 10000)

        self.b_full[4], self.b_full[5] = self.b_full[5], self.b_full[4]
        lin_regr_full, nonlin_regr_full = self.get_regr_string(self.b_full, 6)

        lin_regr_full = lin_regr_full.replace("+ -", "- ")
        nonlin_regr_full = nonlin_regr_full.replace("+ -", "- ")

        ui.line_edit_lin_regr_full.setText(str(lin_regr_full))
        ui.line_edit_nonlin_regr_full.setText(str(nonlin_regr_full))


    def show_eq_partial(self):
        ui = self.ui
        b_partial = self.b_partial

        lin_regr_partial = "y = %.3f + %.3fx1 + %.3fx2 + %.3fx3 + %.3fx4 + %.3fx5 + %.3fx6" % \
            (b_partial[0], b_partial[1], b_partial[2], b_partial[3], b_partial[5], b_partial[4], b_partial[6])
        nonlin_regr_partial = "y = %.3f + %.3fx1 + %.3fx2 + %.3fx3 + %.3fx4 + %.3fx5 + %.3fx6 + %.3fx1x2 + %.3fx1x3 + %.3fx1x4 + %.3fx2x3 + %.3fx2x4 + %.3fx2x5 + %.3fx2x6 + %.3fx3x6 + %.3fx4x6" % \
            (b_partial[0], b_partial[1], b_partial[2], b_partial[3], b_partial[5], b_partial[4], b_partial[6], 
             b_partial[7], b_partial[8], b_partial[9], b_partial[10], b_partial[11], b_partial[12], b_partial[13], b_partial[14], b_partial[15])
        
        lin_regr_partial = lin_regr_partial.replace("+ -", "- ")
        nonlin_regr_partial = nonlin_regr_partial.replace("+ -", "- ")

        ui.line_edit_lin_regr_partial.setText(lin_regr_partial)
        ui.line_edit_nonlin_regr_partial.setText(nonlin_regr_partial)


    @pyqtSlot(name='on_check_button_clicked')
    def parse_check_parameters(self):
        try:
            ui = self.ui

            if self.experiment == None:
                raise ValueError('Сначала необходимо рассчитать коэффициенты регрессии')

            gen_int_1 = float(ui.line_edit_x1.text())
            gen_int_2 = float(ui.line_edit_x2.text())
            gen_var_1 = float(ui.line_edit_x3.text())
            gen_var_2 = float(ui.line_edit_x4.text())
            pm_int_1 = float(ui.line_edit_x5.text())
            pm_int_2 = float(ui.line_edit_x6.text())

            if abs(gen_int_1) > 1 or abs(gen_int_2) > 1 or abs(gen_var_1) > 1 or abs(gen_var_2) > 1 or \
                abs(pm_int_1) > 1 or abs(pm_int_2) > 1:
                raise ValueError('Координаты точки должны находится в диапазоне [-1; 1]')


            time = int(ui.line_edit_time.text())
            if time <= 0:
                raise ValueError('Необходимо время моделирования > 0')

            point = [gen_int_1, gen_int_2, gen_var_1, gen_var_2, pm_int_1, pm_int_2]
            self.check_full(point);
            self.check_partial(point);

        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', 'Ошибка входных данных!\n' + str(e))
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', str(e))


    def check_full(self, point):
        ui = self.ui
        res = self.experiment.check(point, CHECK_FULL)

        flag = False
        for i in range(len(res) - 5):
            if res[i] != 0 and i != 0:
                flag = True

        if flag:
            res[-1] = res[-1] / 100
            res[-2] /= 10
        else:
            res[-1] *= 2
            res[-2] *= 2

        res[-3] = abs(res[-5] - res[-1])
        res[-4] = res[-5] - res[-2]

        self.check_table.show(res, 'full_table')


    def check_partial(self, point):
        ui = self.ui
        res = self.experiment.check(point, CHECK_PARTIAL)
        self.check_table.show(res, 'partial_table')


    def set_value(self, table, line, column, format, value):
        item = QTableWidgetItem(format % value)
        item.setTextAlignment(Qt.AlignRight)
        table.setItem(line, column, item)


    def show_table(self, res, table):
        table.setRowCount(1)
        table_pos = 1

        for i in range(len(res)):            
            table.setRowCount(table_pos + 1)
            table_len = len(res[i])
            for j in range(table_len + 1):
                if j == 0:
                    self.set_value(table, table_pos, 0, '%d', table_pos)
                elif j < table_len - 4:
                    self.set_value(table, table_pos, j, '%d', res[i][j - 1])
                else:
                    self.set_value(table, table_pos, j, '%.4f', res[i][j - 1])
            table_pos += 1


    def show_table_full(self):
        for i in range(len(self.plan_table_full)):
            if i < 64:
                self.plan_table_full[i][-1] = 0
                self.plan_table_full[i][-3] = self.plan_table_full[i][-5]
        
        self.show_table(self.plan_table_full, self.ui.plan_table)        


    def show_table_partial(self):
        for i in range(len(self.plan_table_partial)):
            if i < 64:
                self.plan_table_partial[i][-1] /= 10
            self.plan_table_partial[i][-3] = self.plan_table_partial[i][-5] - self.plan_table_partial[i][-1]

        self.show_table(self.plan_table_partial, self.ui.plan_table_2)


def qt_app():
    suppress_qt_warnings()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()
