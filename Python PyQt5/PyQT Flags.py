import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Flags(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('flags_design.ui', self)
        self.btn.clicked.connect(self.run)

    def run(self):
        fl = []
        if self.blue1.isChecked():
            fl.append('Синий')
        elif self.red1.isChecked():
            fl.append('Красный')
        elif self.green1.isChecked():
            fl.append('Зелёный')

        if self.blue2.isChecked():
            fl.append('Синий')
        elif self.red2.isChecked():
            fl.append('Красный')
        elif self.green2.isChecked():
            fl.append('Зелёный')

        if self.blue3.isChecked():
            fl.append('Синий')
        elif self.red3.isChecked():
            fl.append('Красный')
        elif self.green3.isChecked():
            fl.append('Зелёный')

        if fl:
            if len(fl) > 2:
                self.colors.setText(f'Цвета: {", ".join(fl[:-1])} и {fl[-1]}')
            else:
                self.colors.setText(f'Цвета: {", ".join(fl)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Flags()
    win.show()
    sys.exit(app.exec())

