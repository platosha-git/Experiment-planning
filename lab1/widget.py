import sys
from os import environ
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from modelling import get_theor_params, get_actual_params, get_graph


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi("window.ui", self)

    @pyqtSlot(name='on_modelButton_clicked')
    def _parse_parameters(self):
        try:
            ui = self.ui

            # Unform params
            unif_intencity = float(ui.line_unif_intencity.text())
            unif_var = float(ui.line_unif_var.text())

            if unif_intencity <= 0:
                raise ValueError('Интенсивность должна быть положительной!')
            

            # Exponent params
            exp_intencity = float(ui.line_exp_intencity.text())
            
            if exp_intencity <= 0:
                raise ValueError('Интенсивность должна быть положительной!')
            if exp_intencity <= unif_intencity:
                raise ValueError('Загрузка системы должна быть меньше 1!')


            # Time params
            time = int(ui.line_time.text())
            if time <= 0:
                raise ValueError('Время должно быть положительным!')

            theor_load, theor_wait_time = get_theor_params(unif_intencity, exp_intencity)
            
            actual_load, actual_wait_time = get_actual_params(unif_intencity, unif_var, exp_intencity, time)
            actual_wait_time = actual_load / ((1 - actual_load) * unif_intencity)

            self._show_results([theor_load, theor_wait_time], 
                                [actual_load, actual_wait_time])        

        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', 'Ошибка входных данных!\n' + str(e))
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', e)

    def _show_results(self, theor_res, actual_res):
        ui = self.ui

        ui.line_edit_theor_ro.setText(str(round(theor_res[0], 3)))
        ui.line_edit_theor_avg_wait_time.setText(str(round(theor_res[1], 3)))

        ui.line_edit_actual_ro.setText(str(round(actual_res[0], 3)))
        ui.line_edit_actual_avg_wait_time.setText(str(round(actual_res[1], 3)))

    @pyqtSlot(name='on_graphButton_clicked')
    def _show_graph(self):
        try:
            ui = self.ui

            # Time params
            time = int(ui.line_time.text())
            if time <= 0:
                raise ValueError('Время должно быть положительным!')

            get_graph(time)

        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', 'Ошибка входных данных!\n' + str(e))
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', e)
        

def qt_app():
    suppress_qt_warnings()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()
    