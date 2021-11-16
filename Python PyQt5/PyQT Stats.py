import sys
from random import choice
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Choice(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../uics/stats.ui', self)
        self.pushButton.clicked.connect(self.rand)

    def rand(self):
        self.label_5.clear()
        filename = self.lineEdit.text()
        try:
            with open(f'../text_files/{filename}', encoding='utf-8') as inputFile:
                nums = list(map(int, inputFile.read().split()))
                min_n, max_n, avg_n = min(nums), max(nums), sum(nums) / len(nums)
                self.spinBox.setValue(max_n)
                self.spinBox_2.setValue(min_n)
                self.doublebox.setValue(avg_n)
            with open('../text_files/output.txt', 'w', encoding='utf-8') as outputFile:
                outputFile.write(f'Максимальное значене: {max_n}, Минимальное значение: {min_n}, '
                                 f'Среднее значение: {avg_n}')
        except FileNotFoundError:
            self.label_5.setText(f'Файл {filename} не найден')
        except ValueError:
            self.label_5.setText(f'В файле {filename} содержаться неверные данные')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Choice()
    win.show()
    sys.exit(app.exec())
