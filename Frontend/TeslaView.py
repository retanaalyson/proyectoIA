# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TeslaView.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from URL import url
import requests


class Ui_TeslaView(object):
    def setupUi(self, TeslaView):
        TeslaView.setObjectName("TeslaView")
        TeslaView.resize(768, 600)
        TeslaView.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(TeslaView)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 60, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 160, 111, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 160, 16, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(330, 240, 131, 31))
        self.pushButton_12.setStyleSheet("background-color: rgb(255, 192, 114);color: rgb(0, 0, 0);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.getData)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(480, 160, 73, 22))
        self.comboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_4.setFrame(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 160, 16, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 370, 91, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 330, 91, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 330, 141, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 370, 141, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(320, 160, 51, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(400, 160, 51, 22))
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_5.setFrame(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        TeslaView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TeslaView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 26))
        self.menubar.setObjectName("menubar")
        TeslaView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TeslaView)
        self.statusbar.setObjectName("statusbar")
        TeslaView.setStatusBar(self.statusbar)

        self.retranslateUi(TeslaView)
        QtCore.QMetaObject.connectSlotsByName(TeslaView)

    def retranslateUi(self, TeslaView):
        _translate = QtCore.QCoreApplication.translate
        TeslaView.setWindowTitle(_translate("TeslaView", "MainWindow"))
        self.label_2.setText(_translate("TeslaView", "Predecir precio de las acciones de Tesla"))
        self.label.setText(_translate("TeslaView", "Ingrese una fecha"))
        self.label_4.setText(_translate("TeslaView", "/"))
        self.pushButton_12.setText(_translate("TeslaView", "Predecir"))
        self.comboBox_4.setItemText(0, _translate("TeslaView", "2023"))
        self.comboBox_4.setItemText(1, _translate("TeslaView", "2024"))
        self.comboBox_4.setItemText(2, _translate("TeslaView", "2025"))
        self.comboBox_4.setItemText(3, _translate("TeslaView", "2026"))
        self.comboBox_4.setItemText(4, _translate("TeslaView", "2027"))
        self.comboBox_4.setItemText(5, _translate("TeslaView", "2028"))
        self.comboBox_4.setItemText(6, _translate("TeslaView", "2029"))
        self.comboBox_4.setItemText(7, _translate("TeslaView", "2030"))
        self.label_3.setText(_translate("TeslaView", "/"))
        self.label_6.setText(_translate("TeslaView", "Valor Maximo"))
        self.label_5.setText(_translate("TeslaView", "Valor Minimo"))
        self.comboBox.setItemText(0, _translate("TeslaView", "01"))
        self.comboBox_5.setItemText(0, _translate("TeslaView", "01"))
        self.comboBox_5.setItemText(1, _translate("TeslaView", "02"))
        self.comboBox_5.setItemText(2, _translate("TeslaView", "03"))
        self.comboBox_5.setItemText(3, _translate("TeslaView", "04"))
        self.comboBox_5.setItemText(4, _translate("TeslaView", "05"))
        self.comboBox_5.setItemText(5, _translate("TeslaView", "06"))
        self.comboBox_5.setItemText(6, _translate("TeslaView", "07"))
        self.comboBox_5.setItemText(7, _translate("TeslaView", "08"))
        self.comboBox_5.setItemText(8, _translate("TeslaView", "09"))
        self.comboBox_5.setItemText(9, _translate("TeslaView", "10"))
        self.comboBox_5.setItemText(10, _translate("TeslaView", "11"))
        self.comboBox_5.setItemText(11, _translate("TeslaView", "12"))
        
    def getData(self):
        date = self.comboBox_4.currentText() + "-" + self.comboBox_5.currentText() + "-" + self.comboBox.currentText()

        response = requests.get(url + "/modelTesla?fecha=" + date)
        info = response.json()

        print(info)

        self.lineEdit.setText(str(info[date+"T00:00:00.000Z"]["lower Adj Close"]))
        self.lineEdit_2.setText(str(info[date+"T00:00:00.000Z"]["upper Adj Close"])) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TeslaView = QtWidgets.QMainWindow()
    ui = Ui_TeslaView()
    ui.setupUi(TeslaView)
    TeslaView.show()
    sys.exit(app.exec_())
