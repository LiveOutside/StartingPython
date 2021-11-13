import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QLabel, QLineEdit


class Focus(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 70)
        self.setWindowTitle('Focus w/ words')
        self.inp1 = QLineEdit(self)
        self.inp1.move(5, 25)
        self.inp1.resize(100, 20)

        self.btn = QPushButton('->', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(110, 23)
        self.btn.clicked.connect(self.focus)

        self.inp2 = QLineEdit(self)
        self.inp2.move(190, 25)
        self.inp2.resize(100, 20)

    def focus(self):
        if self.inp1.text() != '':
            w = self.inp1.text()
            self.inp1.clear()
            self.inp2.setText(w)
            self.btn.setText('<-')
        else:
            w = self.inp2.text()
            self.inp1.setText(w)
            self.inp2.clear()
            self.btn.setText('->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Focus()
    ex.show()
    sys.exit(app.exec())