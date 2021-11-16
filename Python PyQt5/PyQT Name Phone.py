import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget


class Nmph(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Name_phone.ui', self)
        self.btn.clicked.connect(self.add)

    def add(self):
        b = []
        if self.name.text() and self.phone.text():
            b.append(self.name.text())
            b.append(self.phone.text())
        self.lwid.addItem(str(' '.join(b)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Nmph()
    win.show()
    sys.exit(app.exec())
