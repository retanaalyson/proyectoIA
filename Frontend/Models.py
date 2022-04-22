# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Models.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#Models
from AvocadoView import Ui_AvocadoView
from TeslaView import Ui_TeslaView
from BitcoinView import Ui_BitcoinView
from AutomovilView import Ui_AutomovilView
from HouseView import Ui_HouseView
from WineView import Ui_WineView
from CirrosisView import Ui_CirrosisView
from HepatitisView import Ui_HepatitisView
from CorporalMassView import Ui_CorporalMassView
from LondresView import Ui_LondresView

class Ui_Models(object):
    def setupUi(self, Models):
        Models.setObjectName("Models")
        Models.resize(770, 597)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Models.sizePolicy().hasHeightForWidth())
        Models.setSizePolicy(sizePolicy)
        Models.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton = QtWidgets.QPushButton(Models)
        self.pushButton.setGeometry(QtCore.QRect(100, 130, 251, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(148, 255, 160);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.bitcoin)
        
        self.pushButton_2 = QtWidgets.QPushButton(Models)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 190, 251, 31))
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(148, 255, 160);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.casa)
        
        self.pushButton_3 = QtWidgets.QPushButton(Models)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 250, 251, 31))
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(148, 255, 160);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.automovil)
        
        self.pushButton_4 = QtWidgets.QPushButton(Models)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 310, 251, 31))
        self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(148, 255, 160);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.corporal)
        
        self.pushButton_5 = QtWidgets.QPushButton(Models)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 370, 251, 31))
        self.pushButton_5.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(148, 255, 160);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.avocado)

        
        self.pushButton_6 = QtWidgets.QPushButton(Models)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 130, 251, 31))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        
        self.pushButton_6.setFont(font)
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_6.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(148, 255, 160);")
        self.pushButton_6.setAutoRepeat(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.londres)
        
        self.pushButton_7 = QtWidgets.QPushButton(Models)
        self.pushButton_7.setGeometry(QtCore.QRect(430, 190, 251, 31))
        self.pushButton_7.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(148, 255, 160);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.tesla)
        
        self.pushButton_8 = QtWidgets.QPushButton(Models)
        self.pushButton_8.setGeometry(QtCore.QRect(430, 250, 251, 31))
        self.pushButton_8.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(148, 255, 160);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.hepatitis)
        
        self.pushButton_9 = QtWidgets.QPushButton(Models)
        self.pushButton_9.setGeometry(QtCore.QRect(430, 310, 251, 31))
        self.pushButton_9.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(148, 255, 160);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.cirrosis)
        
        self.pushButton_10 = QtWidgets.QPushButton(Models)
        self.pushButton_10.setGeometry(QtCore.QRect(430, 370, 251, 31))
        self.pushButton_10.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(148, 255, 160);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.vino)
        
        self.pushButton_11 = QtWidgets.QPushButton(Models)
        self.pushButton_11.setGeometry(QtCore.QRect(320, 470, 131, 31))
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 192, 114);color: rgb(0, 0, 0);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.regresar)
        self.pushButton_11.clicked.connect(Models.close)
        
        self.label = QtWidgets.QLabel(Models)
        self.label.setGeometry(QtCore.QRect(330, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.retranslateUi(Models)
        QtCore.QMetaObject.connectSlotsByName(Models)

    def retranslateUi(self, Models):
        _translate = QtCore.QCoreApplication.translate
        Models.setWindowTitle(_translate("Models", "Models"))
        self.pushButton.setText(_translate("Models", "Predecir precio del Bitcoin"))
        self.pushButton_2.setText(_translate("Models", "Predecir precio de una casa"))
        self.pushButton_3.setText(_translate("Models", "Predecir el precio de un automovil"))
        self.pushButton_4.setText(_translate("Models", "Predecir masa corporal"))
        self.pushButton_5.setText(_translate("Models", "Predecir precio de un aguacate"))
        self.pushButton_6.setText(_translate("Models", "Predecir cantidad de crimenes en Londres"))
        self.pushButton_7.setText(_translate("Models", "Predecir acciones de Tesla"))
        self.pushButton_8.setText(_translate("Models", "Clasificar tipo de Hepatitis"))
        self.pushButton_9.setText(_translate("Models", "Clasificar tipo de Cirrosis"))
        self.pushButton_10.setText(_translate("Models", "Clasificar la calidad del vino"))
        self.pushButton_11.setText(_translate("Models", "Regresar"))
        self.label.setText(_translate("Models", "Modelos"))

    def bitcoin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BitcoinView()
        self.ui.setupUi(self.window)
        self.window.show()
              
    def casa(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HouseView()
        self.ui.setupUi(self.window)
        self.window.show()

    def automovil(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AutomovilView()
        self.ui.setupUi(self.window)
        self.window.show()

    def corporal(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CorporalMassView()
        self.ui.setupUi(self.window)
        self.window.show()

    def avocado(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AvocadoView()
        self.ui.setupUi(self.window)
        self.window.show()

    def londres(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LondresView()
        self.ui.setupUi(self.window)
        self.window.show()

    def tesla(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TeslaView()
        self.ui.setupUi(self.window)
        self.window.show()

    def hepatitis(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HepatitisView()
        self.ui.setupUi(self.window)
        self.window.show()

    def cirrosis(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CirrosisView()
        self.ui.setupUi(self.window)
        self.window.show()

    def vino(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WineView()
        self.ui.setupUi(self.window)
        self.window.show()

    def regresar(self):
        from Main import Ui_HomeView
        self.HomeView = QtWidgets.QMainWindow()
        self.ui = Ui_HomeView()
        self.ui.setupUi(self.HomeView)
        self.HomeView.show()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Models = QtWidgets.QMainWindow()
    ui = Ui_Models()
    ui.setupUi(Models)
    Models.show()
    sys.exit(app.exec_())
