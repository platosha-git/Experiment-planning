from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
import sys

import numpy as np
from scipy import interpolate

from model import *

class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_model.clicked.connect(self.onModelBtnClick)
        self.ui.pushButton_graph.clicked.connect(self.onGraphBtnClick)

    def addItemTableWidget(self, row, column, value):
        item = QTableWidgetItem()
        item.setText(str(value))
        self.ui.tableWidget.setItem(row, column, item)

    def onModelBtnClick(self):
        try:
            l_coming = self.ui.spinbox_intensivity_oa.value()
            mu_handling = self.ui.spinbox_intensivity_gen.value()
            sigma_handling = self.ui.spinbox_intensivity_gen_range.value()
            maxTimeModulation = self.ui.spinbox_time_model.value()

            terminal = Terminal()
            #device = Device("ОA", timeDistribution=generatorGauss(1 / mu_handling, sigma_handling), next=terminal.process)
            device = Device("ОA", timeDistribution=generatorExponent(1 / mu_handling), next=terminal.process)

            # capacity=-1 -- очередь бесконечная
            storage: LoadBalancer = LoadBalancer("Буфер", [device], terminal, capacity=-1)

            #generator: Generator = Generator(generatorExponent(1 / l_coming), storage.process)
            generator: Generator = Generator(generatorUD(1 / mu_handling, 1 / sigma_handling), storage.process)

            eventModel: EventModel = EventModel(terminal)
            eventModel.addEvents(generator.process())
            eventModel.run(maxTimeModulation = maxTimeModulation)

            self.addItemTableWidget(2, 1, terminal.processed)
            self.addItemTableWidget(3, 1, round(terminal.lastRequest.time, 2))

            self.addItemTableWidget(1, 1, round(storage.totalWaitingTime / (storage.processedRequest + len(storage.queue)), 2))

            print(f"Максимальный размер буфера: {storage.maxQueue}")
            print(f"Эксп. интенсивность генератора: {generator.Lambda:.2f}")
            print(f"Эксп. интенсивность ОА: {device.Mu:.2f}")
            self.addItemTableWidget(0, 1, round(generator.Lambda / device.Mu, 2))

            # если загрузка > 1 - нестационарный режим (неустоявшийся)
            p = mu_handling / l_coming
            self.addItemTableWidget(0, 0, round(p, 2))

            if p < 1:
                avg_size = p * p / (1 - p)
                #print(f"Ср. длина очереди: {avg_size:.2f}")

                avg_t = avg_size / mu_handling
                # print(f"Ср. время ожидания: {avg_t:.2f}")

                t_avg = p / (1 - p) / mu_handling
                print(avg_t)
                self.addItemTableWidget(1, 0, '-')
            else:
                self.addItemTableWidget(1, 0, '-')

            # Работает, только для экспоненциальных законов
            #print(f"Вероятность что ОА занят: {p:.2f}")

            # avg_size = p * p / (1 - p)
            #print(f"Ср. длина очереди: {avg_size:.2f}")

            # avg_t = avg_size / l_coming
            # print(f"Ср. время ожидания: {avg_t:.2f}")

            self.addItemTableWidget(2, 0, round(maxTimeModulation * min(l_coming, mu_handling), 2))
            self.addItemTableWidget(3, 0, round(maxTimeModulation, 2))

        except AttributeError as e:
            msgBox = QMessageBox()
            msgBox.setText('Произошла ошибка, недостаточное время моделирования!\n')
            msgBox.show()
            msgBox.exec()
    
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText('Произошла ошибка!\n' + repr(e))
            msgBox.show()
            msgBox.exec()

    def onGraphBtnClick(self):
        create_graph()

if __name__ == "__main__":
    app = QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())