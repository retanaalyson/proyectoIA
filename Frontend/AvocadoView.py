# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AvocadoView.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from URL import url
import requests


class Ui_AvocadoView(object):
    def setupUi(self, AvocadoView):
        AvocadoView.setObjectName("AvocadoView")
        AvocadoView.resize(768, 600)
        AvocadoView.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(AvocadoView)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 80, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(330, 270, 131, 31))
        self.pushButton_12.setStyleSheet("background-color: rgb(255, 192, 114);color: rgb(0, 0, 0);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.getData)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 190, 16, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(400, 190, 51, 22))
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

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(320, 190, 51, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")

        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(480, 190, 73, 22))
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
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 190, 111, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 190, 16, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 390, 91, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 350, 91, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 350, 151, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 390, 151, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")

        AvocadoView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AvocadoView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 26))
        self.menubar.setObjectName("menubar")
        AvocadoView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AvocadoView)
        self.statusbar.setObjectName("statusbar")
        AvocadoView.setStatusBar(self.statusbar)

        self.retranslateUi(AvocadoView)
        QtCore.QMetaObject.connectSlotsByName(AvocadoView)

    def retranslateUi(self, AvocadoView):
        _translate = QtCore.QCoreApplication.translate
        AvocadoView.setWindowTitle(_translate("AvocadoView", "AvocadoView"))
        self.label_2.setText(_translate("AvocadoView", "Predecir precio del Aguacate"))
        self.pushButton_12.setText(_translate("AvocadoView", "Predecir"))
        self.label_3.setText(_translate("AvocadoView", "/"))
        self.comboBox_5.setItemText(0, _translate("AvocadoView", "01"))
        self.comboBox_5.setItemText(1, _translate("AvocadoView", "02"))
        self.comboBox_5.setItemText(2, _translate("AvocadoView", "03"))
        self.comboBox_5.setItemText(3, _translate("AvocadoView", "04"))
        self.comboBox_5.setItemText(4, _translate("AvocadoView", "05"))
        self.comboBox_5.setItemText(5, _translate("AvocadoView", "06"))
        self.comboBox_5.setItemText(6, _translate("AvocadoView", "07"))
        self.comboBox_5.setItemText(7, _translate("AvocadoView", "08"))
        self.comboBox_5.setItemText(8, _translate("AvocadoView", "09"))
        self.comboBox_5.setItemText(9, _translate("AvocadoView", "10"))
        self.comboBox_5.setItemText(10, _translate("AvocadoView", "11"))
        self.comboBox_5.setItemText(11, _translate("AvocadoView", "12"))
        self.comboBox.setItemText(0, _translate("AvocadoView", "01"))
        self.comboBox_4.setItemText(0, _translate("AvocadoView", "2020"))
        self.comboBox_4.setItemText(1, _translate("AvocadoView", "2021"))
        self.comboBox_4.setItemText(2, _translate("AvocadoView", "2022"))
        self.comboBox_4.setItemText(3, _translate("AvocadoView", "2023"))
        self.comboBox_4.setItemText(4, _translate("AvocadoView", "2024"))
        self.comboBox_4.setItemText(5, _translate("AvocadoView", "2025"))
        self.comboBox_4.setItemText(6, _translate("AvocadoView", "2026"))
        self.comboBox_4.setItemText(7, _translate("AvocadoView", "2027"))
        self.comboBox_4.setItemText(8, _translate("AvocadoView", "2028"))
        self.comboBox_4.setItemText(9, _translate("AvocadoView", "2029"))
        self.comboBox_4.setItemText(10, _translate("AvocadoView", "2030"))
        self.label.setText(_translate("AvocadoView", "Ingrese una fecha"))
        self.label_4.setText(_translate("AvocadoView", "/"))
        self.label_6.setText(_translate("AvocadoView", "Valor Maximo"))
        self.label_5.setText(_translate("AvocadoView", "Valor Minimo"))

    def getData(self):
        date = self.comboBox_4.currentText() + "-" + self.comboBox_5.currentText() + "-" + self.comboBox.currentText()
        
        response = requests.get(url + "/modelAguacate?fecha=" + date)
        info = response.json()

        self.lineEdit.setText(str(info[date+"T00:00:00.000Z"]["lower AveragePrice"]))
        self.lineEdit_2.setText(str(info[date+"T00:00:00.000Z"]["upper AveragePrice"]))   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AvocadoView = QtWidgets.QMainWindow()
    ui = Ui_AvocadoView()
    ui.setupUi(AvocadoView)
    AvocadoView.show()
    sys.exit(app.exec_())
