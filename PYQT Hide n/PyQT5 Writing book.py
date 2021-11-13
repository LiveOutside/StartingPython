import datetime
import sys
from PyQT5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget


class Book(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.load
