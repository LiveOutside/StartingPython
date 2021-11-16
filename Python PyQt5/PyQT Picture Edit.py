import sys
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap


class PictureEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../uics/pic.ui', self)
        self.filename = QFileDialog.getOpenFileName(self,
                                                    'Выберете картинку', '', 'Картинки(*jpg)')[0]
        self.original_img = Image.open(self.filename)
        self.current_img = Image.open(self.filename)
        self.degrees = 0
        self.i = ImageQt(self.current_img)
        self.pixmap = QPixmap.fromImage(self.i)
        self.piclabel.setPixmap(self.pixmap)

        self.Red_Button.clicked.connect(self.set_channel)
        self.Green_Button.clicked.connect(self.set_channel)
        self.Blue_Button.clicked.connect(self.set_channel)
        self.All_Buttons.clicked.connect(self.set_channel)

        self.Left_Button.clicked.connect(self.rotate)
        self.Right_Button.clicked.connect(self.rotate)

        self.Slider.setMinimum(0)
        self.Slider.setMaximum(255)
        self.Slider.setValue(255)
        self.Slider.valueChanged.connect(self.change_alpha)

        self.new_img = 'new.png'

    def set_channel(self):
        self.current_img = self.original_img.copy()
        pixels = self.current_img.load()
        x, y = self.current_img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if self.sender().text() == 'R':
                    pixels[i, j] = r, 0, 0
                elif self.sender().text() == 'G':
                    pixels[i, j] = 0, g, 0
                elif self.sender().text() == 'B':
                    pixels[i, j] = 0, 0, b
                else:
                    pass
        self.current_img = self.current_img.rotate(self.degrees, expand=True)
        self.i = ImageQt(self.current_img)
        self.pixmap = QPixmap.fromImage(self.i)
        self.piclabel.setPixmap(self.pixmap)

    def rotate(self):
        if self.sender().text() == 'По часовой стрелке':
            self.degrees -= 90
            deg = -90
        else:
            self.degrees += 90
            deg = 90
        self.degrees %= 360
        self.current_img = self.current_img.rotate(deg, expand=True)
        self.i = ImageQt(self.current_img)
        self.pixmap = QPixmap.fromImage(self.i)
        self.piclabel.setPixmap(self.pixmap)

    def change_alpha(self):
        alpha = int(self.Slider.value())
        image = Image.open(self.filename)
        image.putalpha(alpha)
        image.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.piclabel.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PictureEdit()
    win.show()
    sys.exit(app.exec())
