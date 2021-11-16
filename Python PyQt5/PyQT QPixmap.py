import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QInputDialog
from PyQt5.QtGui import QPaintDevice, QPixmap


SCREENSIZE = [400, 400]


class Map(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, *SCREENSIZE)
        self.image = QLabel(self)
        self.image.move(60, 60)
        self.image.resize(250, 250)
        self.image.setPixmap(self.pixmap)