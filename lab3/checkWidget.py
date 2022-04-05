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
    

    def show(self, res, table_name, table_pos):
        ui = self.ui

        if table_name == 'full_table':
            table = ui.table_full
        else:
            table = ui.table_partial

        table.setRowCount(table_pos + 1)
        table_len = len(res)

        for j in range(table_len + 1):
            if j == 0:
                self.set_value(table, table_pos, 0, '%d', table_pos)
            elif j < table_len - 4:
                self.set_value(table, table_pos, j, '%g', res[j - 1])
            else:
                self.set_value(table, table_pos, j, '%.4f', res[j - 1])

        super().show()
