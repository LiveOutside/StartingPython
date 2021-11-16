import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Objective(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../uics/cube_obj.ui', self)
        self.pushButton.clicked.connect(self.printer)
        self.flag = False

    def printer(self):
        self.side = int(self.le1.text())
        self.coeff = float(self.le2.text())
        self.n = int(self.le3.text())
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 0, 0))
            self.x, self.y = 90, 150
            for i in range(self.n):
                self.drawSquare(qp)
                delta = self.side * (1 - self.coeff) / 2
                self.side *= self.coeff
                self.x += delta
                self.y += delta
            qp.end()

    def drawSquare(self, painter):
        self.x, self.y, self.side = int(self.x), int(self.y), int(self.side)
        painter.drawLine(self.x, self.y, self.x + self.side, self.y)
        painter.drawLine(self.x + self.side, self.y, self.x + self.side, self.y + self.side)
        painter.drawLine(self.x + self.side, self.y + self.side, self.x, self.y + self.side)
        painter.drawLine(self.x, self.y + self.side, self.x, self.y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Objective()
    win.show()
    sys.exit(app.exec())
