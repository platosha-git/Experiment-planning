import sys
from os import environ
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from experiment import Experiment
from numpy import random as nr

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi("window.ui", self)
        self.experiment = None
        self.Table_position = 1

    @pyqtSlot(name='on_calcButton_clicked')
    def _parse_parameters(self):
        try:
            ui = self.ui

            # TODO: проверки на корректность ввода
            
            min_gen_int = float(ui.line_edit_min_gen_int.text())
            max_gen_int = float(ui.line_edit_max_gen_int.text())
            min_gen_var = float(ui.line_edit_min_gen_var.text())
            max_gen_var = float(ui.line_edit_max_gen_var.text())
            gen = [min_gen_int, max_gen_int, min_gen_var, max_gen_var]

            min_pm_int = float(ui.line_edit_min_pm_int.text())
            max_pm_int = float(ui.line_edit_max_pm_int.text())
            pm = [min_pm_int, max_pm_int]

            if min_gen_int < 0 or max_gen_int < 0 or min_gen_var < 0 or max_gen_var < 0 or \
                min_pm_int < 0 or max_pm_int < 0:
                raise ValueError('Интенсивности и дисперсии интенсивностей должны быть > 0')

            # Input params
            time = int(ui.line_edit_time.text())
            if time <= 0:
                raise ValueError('Необходимо время моделирования > 0')

            self.experiment = Experiment(gen, pm, time)
            table, regr = self.experiment.calculate()

            self._show_results(table, regr)        
        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', 'Ошибка входных данных!\n' + str(e))
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', e)

    def set_value(self, line, column, format, value):
        item = QTableWidgetItem(format % value)
        item.setTextAlignment(Qt.AlignRight)
        self.ui.table.setItem(line, column, item)

    def _show_results(self, table, regr):
        ui = self.ui

        lin_regr = ("y = %.3f + %.3fx1 + %.3fx2 + %.3fx3" % \
                        (regr[0], regr[1], regr[2], regr[3]))
        
        nonlin_regr = ("y = %.3f + %.3fx1 + %.3fx2 + %.3fx3 + %.3fx1x2 + %.3fx1x3 + %.3fx2x3 + %.3fx1x2x3" % \
                        (regr[0], regr[1], regr[2], regr[3], regr[4], regr[5], regr[6], regr[7]))

        lin_regr = lin_regr.replace("+ -", "- ")
        nonlin_regr = nonlin_regr.replace("+ -", "- ")

        ui.line_edit_lin_res.setText(str(lin_regr))
        ui.line_edit_nonlin_res.setText(str(nonlin_regr))

        #print(table[0])
        for i in range(len(table)):            
            ui.table.setRowCount(ui.Table_position + 1)
            table_len = len(table[i])
            for j in range(table_len + 1):
                if j == 0:
                    self.set_value(ui.Table_position, 0, '%d', ui.Table_position)
                elif j < table_len - 2:
                    self.set_value(ui.Table_position, j, '%d', table[i][j - 1])
                else:
                    self.set_value(ui.Table_position, j, '%.4f', table[i][j - 1])
            ui.Table_position += 1

    @pyqtSlot(name='on_checkButton_clicked')
    def _parse_check_parameters(self):
        try:
            ui = self.ui

            # TODO: проверки на корректность ввода
            
            gen_int = float(ui.line_edit_gen_int.text())
            gen_var = float(ui.line_edit_gen_var.text())
            pm_int = float(ui.line_edit_pm_int.text())

            if abs(gen_int) > 1 or abs(gen_var) > 1 or abs(pm_int) > 1:
                raise ValueError('Координаты точки должны находится в диапазоне [-1; 1]')

            # Input params
            time = int(ui.line_edit_time.text())
            if time <= 0:
                raise ValueError('Необходимо время моделирования > 0')

            res = self.experiment.check(gen_int, gen_var, pm_int)

            self._show_table(res)        
        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', 'Ошибка входных данных!\n' + str(e))
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', e)

    def _show_table(self, res):
        ui = self.ui
        x1 = res[0]
        x2 = res[1]
        x3 = res[2]
        exp_res = res[3]
        lin_res = res[4]
        nonlin_res = res[5]
        res = [1, x1, x2, x3, \
                x1*x2, x1*x3, x2*x3, x1*x2*x3, \
                exp_res, lin_res, nonlin_res]
        # res[5] = res[4] + nr.uniform(-0.1, 0.1)
        # res[6] = res[4] + nr.uniform(-0.01, 0.01)

        ui.table.setRowCount(ui.Table_position + 1)
        table_len = len(res)
        for j in range(table_len + 1):
            if j == 0:
                self.set_value(ui.Table_position, 0, '%d', ui.Table_position)
            elif j < table_len - 2:
                self.set_value(ui.Table_position, j, '%g', res[j - 1])
            else:
                self.set_value(ui.Table_position, j, '%.4f', res[j - 1])
        ui.Table_position += 1
        

def qt_app():
    suppress_qt_warnings()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()
    