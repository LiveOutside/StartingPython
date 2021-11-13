import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QLabel, QLineEdit, QCheckBox


class Focus(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Прятки для виджетов')

        self.cbox = QCheckBox(self)
        self.cbox.move(5, 10)
        self.cbox.setText('edit1')
        self.cbox.clicked.connect(self.run)

        self.cbox2 = QCheckBox(self)
        self.cbox2.move(5, 40)
        self.cbox2.setText('edit2')
        self.cbox2.clicked.connect(self.run)

        self.cbox3 = QCheckBox(self)
        self.cbox3.move(5, 70)
        self.cbox3.setText('edit3')
        self.cbox3.clicked.connect(self.run)

        self.cbox4 = QCheckBox(self)
        self.cbox4.move(5, 100)
        self.cbox4.setText('edit4')
        self.cbox4.clicked.connect(self.run)

        self.inp1 = QLineEdit(self)
        self.inp1.move(70, 10)
        self.inp1.resize(70, 20)
        self.inp1.setText('Поле edit1')
        self.inp1.hide()

        self.inp2 = QLineEdit(self)
        self.inp2.move(70, 40)
        self.inp2.resize(70, 20)
        self.inp2.setText('Поле edit2')
        self.inp2.hide()

        self.inp3 = QLineEdit(self)
        self.inp3.move(70, 70)
        self.inp3.resize(70, 20)
        self.inp3.setText('Поле edit3')
        self.inp3.hide()

        self.inp4 = QLineEdit(self)
        self.inp4.move(70, 100)
        self.inp4.resize(70, 20)
        self.inp4.setText('Поле edit4')
        self.inp4.hide()

    def run(self):
        if self.cbox.isChecked():
            self.inp1.show()
        else:
            self.inp1.hide()
        if self.cbox2.isChecked():
            self.inp2.show()
        else:
            self.inp2.hide()
        if self.cbox3.isChecked():
            self.inp3.show()
        else:
            self.inp3.hide()
        if self.cbox4.isChecked():
            self.inp4.show()
        else:
            self.inp4.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Focus()
    ex.show()
    sys.exit(app.exec())