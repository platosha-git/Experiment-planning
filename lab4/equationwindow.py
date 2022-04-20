from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QLabel


class EquationWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('equation.ui', self)

    def show(self, y):
        ui = self.ui

        self.label_y.setText(y)
        super().show()
