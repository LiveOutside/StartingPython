import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ariph(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../uics/ariph.ui', self)
        self.btn1.clicked.connect(self.plus)
        self.btn2.clicked.connect(self.minus)
        self.btn3.clicked.connect(self.up)

    def plus(self):
        if self.l1.text() and self.l2.text():
            res = int(self.l1.text()) + int(self.l2.text())
            self.res_label.setText(str(res))

    def minus(self):
        if self.l1.text() and self.l2.text():
            res = int(self.l1.text()) - int(self.l2.text())
            self.res_label.setText(str(res))

    def up(self):
        if self.l1.text() and self.l2.text():
            res = int(self.l1.text()) * int(self.l2.text())
            self.res_label.setText(str(res))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Ariph()
    win.show()
    sys.exit(app.exec())
