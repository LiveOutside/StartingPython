import datetime
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QTimeEdit, QListWidget


class DiaryEvent:
    def __init__(self, dt, title):
        self.dt = dt
        self.title = title

    def to_str(self):
        return f'{self.dt} - {self.title}'

    def __str__(self):
        return self.to_str()


class Planer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('planer.ui', self)
        self.events = []
        self.btn.clicked.connect(self.addText)

    def addText(self):
        if self.edit.text():
            dt = datetime.datetime(self.cal.selectedDate().year(),
                                   self.cal.selectedDate().month(),
                                   self.cal.selectedDate().day(),
                                   self.time.time().hour(),
                                   self.time.time().minute())
            event = DiaryEvent(dt, self.edit.text())
            self.events.append(event)
            self.events = sorted(self.events, key=lambda x: x.dt)
            self.lwid.clear()
            self.lwid.addItems([i.to_str() for i in self.events])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Planer()
    win.show()
    sys.exit(app.exec())