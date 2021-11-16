import csv
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QHeaderView, QTableWidgetItem


class InteractiveCheckout(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../uics/table.ui', self)
        self.load_table('../text_files/price.csv')
        self.table.itemChanged.connect(self.update)

    def load_table(self, table_name):
        with open(table_name) as file:
            reader = csv.reader(file, delimiter=';')
            title = next(reader)
            self.table.setColumnCount(len(title) + 1)
            self.table.setHorizontalHeaderLabels(title + ['Количество'])
            header = self.table.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Stretch)
            self.table.setRowCount(0)
            for i, row in enumerate(reader):
                self.table.setRowCount(self.table.rowCount + 1)
                for j, element in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(''))
            self.table.resizeColumnsToContents()

    def update(self):
        price = [int(self.table.item(i, 1).text())
                 for i in range(self.table.rowCount())]
        count = [int(self.table.item(i, 1).text())
                 if self.table.item(i, 2).text() != '' else 0
                 for i in range(self.table.rowCount())]
        summ = 0
        for i in range(len(price)):
            summ += price[i] * count[i]
        self.edit.setText(str(summ))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = InteractiveCheckout()
    win.show()
    sys.exit(app.exec())
