# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PySide6.QtMultimedia import (QAudioDevice, QAudioFormat,
        QAudioSource, QMediaDevices)
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from Models import Ui_Models
from PyQt5 import QtCore, QtGui, QtWidgets
from Audio import AudioView

class Ui_HomeView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 598)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(300, 100, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setAutoFillBackground(False)
        self.Title.setStyleSheet("color: rgb(255, 255, 255); background-color: None")
        self.Title.setObjectName("Title")
        
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setGeometry(QtCore.QRect(290, 220, 161, 41))
        self.Button.setStyleSheet("background-color: rgb(255, 192, 114);color: rgb(0, 0, 0);")
        self.Button.setObjectName("Button")
        self.Button.clicked.connect(self.AudioView)
        
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(290, 300, 161, 41))
        self.Button_2.setStyleSheet("background-color: rgb(255, 192, 114);color: rgb(0, 0, 0);")
        self.Button_2.setObjectName("Button_2")
        self.Button_2.clicked.connect(self.ModelsViews)
        #self.Button_2.clicked.connect(HomeView.hide)
        
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(290, 380, 161, 41))
        self.Button_3.setStyleSheet("background-color: rgb(255, 192, 114);color: rgb(0, 0, 0);")        
        self.Button_3.setObjectName("Button_3")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "FridayTEC"))
        self.Button.setText(_translate("MainWindow", "Usar comando de voz"))
        self.Button_2.setText(_translate("MainWindow", "Ver modelos"))
        self.Button_3.setText(_translate("MainWindow", "Detectar emocion"))

    def ModelsViews(self):
        HomeView.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Models()
        self.ui.setupUi(self.window)
        self.window.show()

    def AudioView(self):
        app2 = QApplication(sys.argv)

        input_devices = QMediaDevices.audioInputs()
        if not input_devices:
            QMessageBox.warning(None, "audio", "There is no audio input device available.")
            sys.exit(-1)
        main_win = AudioView(input_devices[0])
        main_win.setWindowTitle("audio")
        available_geometry = main_win.screen().availableGeometry()
        size = available_geometry.height() * 3 / 4
        main_win.resize(size, size)
        main_win.show()
        

        sys.exit(app2.exec())
        """self.window = QtWidgets.QMainWindow()
        self.ui = AudioView(input_devices[0])
        self.ui.__init__(self.window)
        self.window.show()"""


if __name__ == "__main__":
    import sys
    url = "http://0e6b-35-245-30-114.ngrok.io"
    app = QtWidgets.QApplication(sys.argv)
    HomeView = QtWidgets.QMainWindow()
    ui = Ui_HomeView()
    ui.setupUi(HomeView)
    HomeView.show()
    sys.exit(app.exec_())

