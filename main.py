import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генератор кругов")
        self.setGeometry(100, 100, 400, 400)

        self.button = QPushButton("Сгенерировать круг", self)
        self.button.setGeometry(150, 150, 100, 50)
        self.button.clicked.connect(self.generateCircle)

    def generateCircle(self):
        diameter = random.randint(10, 100)
        color = QColor.fromRgb(random.randint(0, 255),
                               random.randint(0, 255),
                               random.randint(0, 255))

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(color)
        painter.drawEllipse(random.randint(0, 300),
                            random.randint(0, 300),
                            diameter, diameter)

        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
