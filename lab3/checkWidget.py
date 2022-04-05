from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtCore import Qt


class CheckTableWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('checkWidget.ui', self)
    

    def set_value(self, table, line, column, format, value):
        item = QTableWidgetItem(format % value)
        item.setTextAlignment(Qt.AlignRight)
        table.setItem(line, column, item)
    

    def show(self, res, table_name):
        ui = self.ui

        if table_name == 'full_table':
            table = ui.table_full
        else:
            table = ui.table_partial

        table.setRowCount(2)
        table_len = len(res)

        for j in range(table_len + 1):
            if j == 0:
                self.set_value(table, 1, 0, '%d', 1)
            elif j < table_len - 4:
                self.set_value(table, 1, j, '%g', res[j - 1])
            else:
                self.set_value(table, 1, j, '%.4f', res[j - 1])

        super().show()
