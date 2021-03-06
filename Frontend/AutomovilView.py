# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutomovilView.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from URL import url
import requests


class Ui_AutomovilView(object):
    def setupUi(self, AutomovilView):
        AutomovilView.setObjectName("AutomovilView")
        AutomovilView.resize(772, 600)
        AutomovilView.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(AutomovilView)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(340, 260, 131, 31))
        self.pushButton_12.setStyleSheet("background-color: rgb(255, 192, 114);color: rgb(0, 0, 0);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.getData)

        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(490, 180, 73, 22))
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
        self.label_3.setGeometry(QtCore.QRect(470, 180, 16, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 70, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 180, 111, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 180, 16, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(330, 180, 51, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(410, 180, 51, 22))
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_5.setFrame(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 340, 181, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 340, 91, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 380, 181, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 380, 91, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        AutomovilView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AutomovilView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 26))
        self.menubar.setObjectName("menubar")
        AutomovilView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AutomovilView)
        self.statusbar.setObjectName("statusbar")
        AutomovilView.setStatusBar(self.statusbar)

        self.retranslateUi(AutomovilView)
        QtCore.QMetaObject.connectSlotsByName(AutomovilView)

    def retranslateUi(self, AutomovilView):
        _translate = QtCore.QCoreApplication.translate
        AutomovilView.setWindowTitle(_translate("AutomovilView", "MainWindow"))
        self.pushButton_12.setText(_translate("AutomovilView", "Predecir"))
        self.comboBox_4.setItemText(0, _translate("AutomovilView", "2023"))
        self.comboBox_4.setItemText(1, _translate("AutomovilView", "2024"))
        self.comboBox_4.setItemText(2, _translate("AutomovilView", "2025"))
        self.comboBox_4.setItemText(3, _translate("AutomovilView", "2026"))
        self.comboBox_4.setItemText(4, _translate("AutomovilView", "2027"))
        self.comboBox_4.setItemText(5, _translate("AutomovilView", "2028"))
        self.comboBox_4.setItemText(6, _translate("AutomovilView", "2029"))
        self.comboBox_4.setItemText(7, _translate("AutomovilView", "2030"))
        self.label_3.setText(_translate("AutomovilView", "/"))
        self.label_2.setText(_translate("AutomovilView", "Predecir precio de un automovil"))
        self.label.setText(_translate("AutomovilView", "Ingrese una fecha"))
        self.label_4.setText(_translate("AutomovilView", "/"))
        self.comboBox.setItemText(0, _translate("AutomovilView", "31"))
        self.comboBox_5.setItemText(0, _translate("AutomovilView", "12"))
        self.label_5.setText(_translate("AutomovilView", "Valor Minimo"))
        self.label_6.setText(_translate("AutomovilView", "Valor Maximo"))
        
    def getData(self):
        date = self.comboBox_4.currentText() + "-" + self.comboBox_5.currentText() + "-" + self.comboBox.currentText()
        
        response = requests.get(url + "/modelAuto?fecha=" + date)
        info = response.json()

        self.lineEdit.setText(str(info[date+"T00:00:00.000Z"]["lower Selling_Price"]))
        self.lineEdit_2.setText(str(info[date+"T00:00:00.000Z"]["upper Selling_Price"]))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutomovilView = QtWidgets.QMainWindow()
    ui = Ui_AutomovilView()
    ui.setupUi(AutomovilView)
    AutomovilView.show()
    sys.exit(app.exec_())
