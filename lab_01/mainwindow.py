# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 532)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(310, 50, 261, 71))
        self.groupBox.setObjectName("groupBox")
        self.spinbox_intensivity_oa = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spinbox_intensivity_oa.setGeometry(QtCore.QRect(130, 30, 121, 26))
        self.spinbox_intensivity_oa.setMaximum(9999.99)
        self.spinbox_intensivity_oa.setObjectName("spinbox_intensivity_oa")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 115, 21))
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 81, 17))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(410, 20, 81, 17))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setObjectName("label_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 261, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 115, 21))
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 34, 26))
        self.label_4.setObjectName("label_4")
        self.spinbox_intensivity_gen = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spinbox_intensivity_gen.setGeometry(QtCore.QRect(130, 30, 121, 26))
        self.spinbox_intensivity_gen.setMaximum(99999.99)
        self.spinbox_intensivity_gen.setObjectName("spinbox_intensivity_gen")
        self.spinbox_intensivity_gen_range = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spinbox_intensivity_gen_range.setGeometry(QtCore.QRect(130, 60, 121, 26))
        self.spinbox_intensivity_gen_range.setMaximum(99999.99)
        self.spinbox_intensivity_gen_range.setObjectName("spinbox_intensivity_gen_range")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 168, 26))
        self.label_5.setObjectName("label_5")
        self.spinbox_time_model = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.spinbox_time_model.setGeometry(QtCore.QRect(190, 160, 121, 26))
        self.spinbox_time_model.setMinimum(1.0)
        self.spinbox_time_model.setMaximum(99999999.99)
        self.spinbox_time_model.setProperty("value", 100.0)
        self.spinbox_time_model.setObjectName("spinbox_time_model")
        self.pushButton_model = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_model.setGeometry(QtCore.QRect(10, 210, 559, 31))
        self.pushButton_model.setObjectName("pushButton_model")
        self.pushButton_graph = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_graph.setGeometry(QtCore.QRect(10, 250, 559, 31))
        self.pushButton_graph.setObjectName("pushButton_graph")
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 350, 471, 151))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(10, 300, 561, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(10, 320, 561, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Экспоненциальное распределение"))
        self.label_2.setText(_translate("MainWindow", "Интенсивность :"))
        self.label.setText(_translate("MainWindow", "Генератор"))
        self.label_8.setText(_translate("MainWindow", "ОА"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Равномерное распределение"))
        self.label_6.setText(_translate("MainWindow", "Интенсивность :"))
        self.label_4.setText(_translate("MainWindow", "СКО:"))
        self.label_5.setText(_translate("MainWindow", "Время моделирования:"))
        self.pushButton_model.setText(_translate("MainWindow", "Моделировать"))
        self.pushButton_graph.setText(_translate("MainWindow", "Построить график"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Загруженность системы"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Среднее время завки в очереди"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Количество обработанных заявок"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Общее время моделирования"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Теоретич."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Фактич."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
