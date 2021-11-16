import sys
from random import choice
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Choice(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('C:/Users/maslihov/PycharmProjects/maslihov/uics/randomchoice.ui', self)
        self.pushButton.clicked.connect(self.rand)

    def rand(self):
        with open('C:/Users/maslihov/PycharmProjects/maslihov/text_files/lines.txt', encoding='utf-8') as f:
            txt = f.readlines()
        if txt:
            self.lineEdit.setText(choice(txt))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Choice()
    win.show()
    sys.exit(app.exec())
