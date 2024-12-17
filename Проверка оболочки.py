import random
import numpy
import sys
dictator = {}
otveti = {}
prosh = {}
with open("Вопросы.txt", "r", encoding="UTF-8") as file:
    lines = [line.rstrip() for line in file]
for i in lines:
    a = i.split("? ")
    wopros = a[0] + "?"
    otvet = a[1]
    dictator.update({wopros: otvet})
for i in lines:
    a = i.split("? ")
    wopross = a[1]
    otvett = a[0] + "?"
    otveti.update({wopros : otvet})

from PyQt5 import QtCore, QtMultimedia
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QBrush, QPixmap


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Design/Start.ui', self)
        self.pushButton.clicked.connect(self.Title)
        self.pushButton_2.clicked.connect(self.Start)
        self.pushButton_3.clicked.connect(self.Exti)

    def Exti(self):
        uic.loadUi('./Design/Start.ui', self)
        self.label_3.setText(f"<b>{wors}</b>")

    def Start(self):
        wors = numpy.random.choice(list(dictator))
        uic.loadUi("./Design/run.ui", self)
        self.label_3.setText(f"<b>{wors}</b>")
        self.pushButton.clicked.connect(self.Run)


    def Title(self):
        uic.loadUi("./Design/Titles.ui", self)
        self.pushButton.clicked.connect(self.Run)

    def Run(self):
        uic.loadUi("./Design/Start.ui", self)
        self.pushButton.clicked.connect(self.Title)
        self.pushButton_2.clicked.connect(self.Start)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
