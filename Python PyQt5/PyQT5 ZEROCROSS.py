import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class ZeroCross(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('', self)
