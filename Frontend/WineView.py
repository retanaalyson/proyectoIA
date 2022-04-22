# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WineView.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from URL import url


class Ui_WineView(object):
    def setupUi(self, WineView):
        WineView.setObjectName("WineView")
        WineView.resize(770, 600)
        WineView.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(WineView)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 70, 181, 20))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.Acid = QtWidgets.QLineEdit(self.centralwidget)
        self.Acid.setGeometry(QtCore.QRect(370, 100, 191, 22))
        self.Acid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Acid.setObjectName("Acid")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 100, 191, 20))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 130, 191, 20))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 160, 191, 20))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 220, 191, 20))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 190, 191, 20))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(180, 340, 191, 20))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(180, 310, 191, 20))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(180, 280, 191, 20))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(180, 250, 191, 20))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(180, 370, 191, 20))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(180, 400, 191, 20))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")

        self.Sulfur = QtWidgets.QLineEdit(self.centralwidget)
        self.Sulfur.setGeometry(QtCore.QRect(370, 250, 191, 22))
        self.Sulfur.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Sulfur.setObjectName("Sulfur")

        self.Chlorides = QtWidgets.QLineEdit(self.centralwidget)
        self.Chlorides.setGeometry(QtCore.QRect(370, 220, 191, 22))
        self.Chlorides.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Chlorides.setObjectName("Chlorides")

        self.Sugar = QtWidgets.QLineEdit(self.centralwidget)
        self.Sugar.setGeometry(QtCore.QRect(370, 190, 191, 22))
        self.Sugar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Sugar.setObjectName("Sugar")

        self.Citric = QtWidgets.QLineEdit(self.centralwidget)
        self.Citric.setGeometry(QtCore.QRect(370, 160, 191, 22))
        self.Citric.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Citric.setObjectName("Citric")

        self.Density = QtWidgets.QLineEdit(self.centralwidget)
        self.Density.setGeometry(QtCore.QRect(370, 310, 191, 22))
        self.Density.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Density.setObjectName("Density")

        self.Dioxide = QtWidgets.QLineEdit(self.centralwidget)
        self.Dioxide.setGeometry(QtCore.QRect(370, 280, 191, 22))
        self.Dioxide.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Dioxide.setObjectName("Dioxide")

        self.Volatic = QtWidgets.QLineEdit(self.centralwidget)
        self.Volatic.setGeometry(QtCore.QRect(370, 130, 191, 22))
        self.Volatic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Volatic.setObjectName("Volatic")

        self.Alcohol = QtWidgets.QLineEdit(self.centralwidget)
        self.Alcohol.setGeometry(QtCore.QRect(370, 370, 191, 22))
        self.Alcohol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Alcohol.setObjectName("Alcohol")

        self.PH = QtWidgets.QLineEdit(self.centralwidget)
        self.PH.setGeometry(QtCore.QRect(370, 340, 191, 22))
        self.PH.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PH.setObjectName("PH")

        self.Sulphates = QtWidgets.QLineEdit(self.centralwidget)
        self.Sulphates.setGeometry(QtCore.QRect(370, 400, 191, 22))
        self.Sulphates.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Sulphates.setObjectName("Sulphates")

        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(300, 440, 131, 31))
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 192, 114);color: rgb(0, 0, 0);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.getData)

        self.Type = QtWidgets.QComboBox(self.centralwidget)
        self.Type.setGeometry(QtCore.QRect(370, 70, 191, 22))
        self.Type.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Type.setObjectName("Type")
        self.Type.addItem("")
        self.Type.addItem("")

        self.Res = QtWidgets.QLineEdit(self.centralwidget)
        self.Res.setGeometry(QtCore.QRect(300, 500, 191, 22))
        self.Res.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Res.setReadOnly(True)
        self.Res.setObjectName("Res")

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(240, 500, 61, 20))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        
        WineView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WineView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 26))
        self.menubar.setObjectName("menubar")
        WineView.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(WineView)
        self.statusbar.setObjectName("statusbar")
        WineView.setStatusBar(self.statusbar)

        self.retranslateUi(WineView)
        QtCore.QMetaObject.connectSlotsByName(WineView)

    def retranslateUi(self, WineView):
        _translate = QtCore.QCoreApplication.translate
        WineView.setWindowTitle(_translate("WineView", "WineView"))
        self.label_2.setText(_translate("WineView", "Classify the quality of the wine"))
        self.label.setText(_translate("WineView", "Select the type"))
        self.label_3.setText(_translate("WineView", "Enter the acid level"))
        self.label_4.setText(_translate("WineView", "Enter the volatic level"))
        self.label_5.setText(_translate("WineView", "Enter the citric level"))
        self.label_6.setText(_translate("WineView", "Enter the chlorides level"))
        self.label_7.setText(_translate("WineView", "Enter the sugar level"))
        self.label_8.setText(_translate("WineView", "Enter the ph level"))
        self.label_9.setText(_translate("WineView", "Enter the density level"))
        self.label_10.setText(_translate("WineView", "Enter the dioxide level"))
        self.label_11.setText(_translate("WineView", "Enter the sulfur level"))
        self.label_12.setText(_translate("WineView", "Enter the alcohol level"))
        self.label_13.setText(_translate("WineView", "Enter the sulphates level"))
        self.pushButton_13.setText(_translate("WineView", "Classify"))
        self.Type.setItemText(0, _translate("WineView", "Red"))
        self.Type.setItemText(1, _translate("WineView", "White"))
        self.label_14.setText(_translate("WineView", "Quality"))

    def getData(self):

        Type = ""

        if self.Type.currentText() == "White":
            Type = "1"
        else:
            Type = "0"

        response = requests.get(url + "/modelVino?tipo=" + Type + "&acido=" + self.Acid.text() + "&volatil=" + 
        self.Volatic.text() + "&citric=" + self.Citric.text() + "&sugar=" + self.Sugar.text() + "&chlorides=" + 
        self.Chlorides.text() + "&sulfur=" + self.Sulfur.text() + "&dioxide=" + self.Dioxide.text() + "&density=" + 
        self.Density.text() + "&pH=" + self.PH.text() + "&sulphates=" + self.Sulphates.text() + "&alcohol=" + self.Alcohol.text())
        
        info = response.json()

        self.Res.setText(str(info["Result"]["0"]))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WineView = QtWidgets.QMainWindow()
    ui = Ui_WineView()
    ui.setupUi(WineView)
    WineView.show()
    sys.exit(app.exec_())
