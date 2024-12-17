import sys
# import os
from PyQt5 import QtCore, QtGui, QtWidgets


# from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget,
#    QPushButton, QAction, QLineEdit, QMessageBox)

# from Shutdown import Ui_MainWindow
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 154)
        MainWindow.setStyleSheet("background-color: rgb(17, 23, 18);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 110, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 30;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(92, 110, 148);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 50, 113, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(5, 9, 18);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: 75 12pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ОК"))
        self.label.setText(_translate("MainWindow", "Введите время (в секундах):"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # тут ваша  логика

        validador = QtCore.QRegExp("[0-9]*")
        ok = QtGui.QRegExpValidator(validador, self)
        self.lineEdit.setValidator(ok)
        self.lineEdit.setFocus()

        # нажмите на кнопку чтобы получить значение из поля LineEdit на печать
        self.pushButton.clicked.connect(self.print_lineEdit)
        # или нажмите клавиши Return или Enter
        self.lineEdit.editingFinished.connect(self.print_lineEdit)

    def print_lineEdit(self):
        text = self.lineEdit.text()  # значение из поля LineEdit
        print(f'Значение из lineEdit на печать: {text}')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
