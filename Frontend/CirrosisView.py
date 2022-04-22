# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CirrosisView.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from URL import url
import requests


class Ui_CirrosisView(object):
    def setupUi(self, CirrosisView):
        CirrosisView.setObjectName("CirrosisView")
        CirrosisView.resize(771, 777)
        CirrosisView.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(CirrosisView)
        self.centralwidget.setObjectName("centralwidget")
        self.NDays = QtWidgets.QLineEdit(self.centralwidget)
        self.NDays.setGeometry(QtCore.QRect(380, 80, 191, 22))
        self.NDays.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NDays.setObjectName("NDays")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(190, 380, 191, 20))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 230, 191, 20))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")

        self.Age = QtWidgets.QLineEdit(self.centralwidget)
        self.Age.setGeometry(QtCore.QRect(380, 170, 191, 22))
        self.Age.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Age.setObjectName("Age")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 110, 191, 20))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 200, 191, 20))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 350, 191, 20))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 140, 191, 20))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(190, 290, 191, 20))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")

        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(310, 620, 131, 31))
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 192, 114);color: rgb(0, 0, 0);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.getData)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.Cholesterol = QtWidgets.QLineEdit(self.centralwidget)
        self.Cholesterol.setGeometry(QtCore.QRect(380, 380, 191, 22))
        self.Cholesterol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Cholesterol.setObjectName("Cholesterol")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 170, 191, 20))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(190, 410, 191, 20))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(190, 260, 191, 20))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")

        self.Albumin = QtWidgets.QLineEdit(self.centralwidget)
        self.Albumin.setGeometry(QtCore.QRect(380, 410, 191, 22))
        self.Albumin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Albumin.setObjectName("Albumin")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, 320, 191, 20))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")

        self.Bilirubin = QtWidgets.QLineEdit(self.centralwidget)
        self.Bilirubin.setGeometry(QtCore.QRect(380, 350, 191, 22))
        self.Bilirubin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Bilirubin.setObjectName("Bilirubin")

        self.Copper = QtWidgets.QLineEdit(self.centralwidget)
        self.Copper.setGeometry(QtCore.QRect(380, 440, 191, 22))
        self.Copper.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Copper.setObjectName("Copper")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 80, 181, 20))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(190, 470, 191, 20))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")

        self.AlkPhos = QtWidgets.QLineEdit(self.centralwidget)
        self.AlkPhos.setGeometry(QtCore.QRect(380, 470, 191, 22))
        self.AlkPhos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AlkPhos.setObjectName("AlkPhos")

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(190, 440, 191, 20))
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")

        self.SGOT = QtWidgets.QLineEdit(self.centralwidget)
        self.SGOT.setGeometry(QtCore.QRect(380, 500, 191, 22))
        self.SGOT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SGOT.setObjectName("SGOT")

        self.Tryglicerides = QtWidgets.QLineEdit(self.centralwidget)
        self.Tryglicerides.setGeometry(QtCore.QRect(380, 530, 191, 22))
        self.Tryglicerides.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tryglicerides.setObjectName("Tryglicerides")

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(190, 560, 191, 20))
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")

        self.Platelets = QtWidgets.QLineEdit(self.centralwidget)
        self.Platelets.setGeometry(QtCore.QRect(380, 560, 191, 22))
        self.Platelets.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Platelets.setObjectName("Platelets")

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(190, 530, 191, 20))
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")

        self.Prothrombin = QtWidgets.QLineEdit(self.centralwidget)
        self.Prothrombin.setGeometry(QtCore.QRect(380, 590, 191, 22))
        self.Prothrombin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Prothrombin.setObjectName("Prothrombin")

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(190, 500, 191, 20))
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")

        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(190, 590, 191, 20))
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")

        self.Res = QtWidgets.QLineEdit(self.centralwidget)
        self.Res.setGeometry(QtCore.QRect(310, 680, 191, 22))
        self.Res.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Res.setReadOnly(True)
        self.Res.setObjectName("Res")

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(250, 680, 61, 20))
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")

        self.Sex = QtWidgets.QComboBox(self.centralwidget)
        self.Sex.setGeometry(QtCore.QRect(380, 200, 191, 22))
        self.Sex.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Sex.setObjectName("Sex")
        self.Sex.addItem("")
        self.Sex.addItem("")

        self.Status = QtWidgets.QComboBox(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(380, 110, 191, 22))
        self.Status.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Status.setObjectName("Status")
        self.Status.addItem("")
        self.Status.addItem("")
        self.Status.addItem("")

        self.Drug = QtWidgets.QComboBox(self.centralwidget)
        self.Drug.setGeometry(QtCore.QRect(380, 140, 191, 22))
        self.Drug.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Drug.setObjectName("Drug")
        self.Drug.addItem("")
        self.Drug.addItem("")

        self.Ascites = QtWidgets.QComboBox(self.centralwidget)
        self.Ascites.setGeometry(QtCore.QRect(380, 230, 191, 22))
        self.Ascites.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Ascites.setObjectName("Ascites")
        self.Ascites.addItem("")
        self.Ascites.addItem("")

        self.Hepatomegaly = QtWidgets.QComboBox(self.centralwidget)
        self.Hepatomegaly.setGeometry(QtCore.QRect(380, 260, 191, 22))
        self.Hepatomegaly.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Hepatomegaly.setObjectName("Hepatomegaly")
        self.Hepatomegaly.addItem("")
        self.Hepatomegaly.addItem("")

        self.Spiders = QtWidgets.QComboBox(self.centralwidget)
        self.Spiders.setGeometry(QtCore.QRect(380, 290, 191, 22))
        self.Spiders.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Spiders.setObjectName("Spiders")
        self.Spiders.addItem("")
        self.Spiders.addItem("")

        self.Edema = QtWidgets.QComboBox(self.centralwidget)
        self.Edema.setGeometry(QtCore.QRect(380, 320, 191, 22))
        self.Edema.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Edema.setObjectName("Edema")
        self.Edema.addItem("")
        self.Edema.addItem("")
        self.Edema.addItem("")

        CirrosisView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CirrosisView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 26))
        self.menubar.setObjectName("menubar")

        CirrosisView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CirrosisView)
        self.statusbar.setObjectName("statusbar")
        CirrosisView.setStatusBar(self.statusbar)

        self.retranslateUi(CirrosisView)
        QtCore.QMetaObject.connectSlotsByName(CirrosisView)

    def retranslateUi(self, CirrosisView):
        _translate = QtCore.QCoreApplication.translate
        CirrosisView.setWindowTitle(_translate("CirrosisView", "CirrosisView"))
        self.label_12.setText(_translate("CirrosisView", "Enter the Cholesterol"))
        self.label_6.setText(_translate("CirrosisView", "Select the Ascites"))
        self.label_3.setText(_translate("CirrosisView", "Select the Status"))
        self.label_7.setText(_translate("CirrosisView", "Select the Sex"))
        self.label_8.setText(_translate("CirrosisView", "Enter the Bilirubin"))
        self.label_4.setText(_translate("CirrosisView", "Select the Drug"))
        self.label_10.setText(_translate("CirrosisView", "Select the Spiders"))
        self.pushButton_13.setText(_translate("CirrosisView", "Classify"))
        self.label_2.setText(_translate("CirrosisView", "Classify the type of Cirrosis"))
        self.label_5.setText(_translate("CirrosisView", "Enter the Age"))
        self.label_13.setText(_translate("CirrosisView", "Enter the Albumin"))
        self.label_11.setText(_translate("CirrosisView", "Select the Hepatomegaly"))
        self.label_9.setText(_translate("CirrosisView", "Select the Edema"))
        self.label.setText(_translate("CirrosisView", "Enter the N_Days"))
        self.label_14.setText(_translate("CirrosisView", "Enter the Alk_Phos"))
        self.label_15.setText(_translate("CirrosisView", "Enter the Copper"))
        self.label_16.setText(_translate("CirrosisView", "Enter the Platelets"))
        self.label_17.setText(_translate("CirrosisView", "Enter the Tryglicerides"))
        self.label_18.setText(_translate("CirrosisView", "Enter the SGOT"))
        self.label_19.setText(_translate("CirrosisView", "Enter the Prothrombin"))
        self.label_20.setText(_translate("CirrosisView", "Type"))
        self.Sex.setItemText(0, _translate("CirrosisView", "Male"))
        self.Sex.setItemText(1, _translate("CirrosisView", "Female"))
        self.Status.setItemText(0, _translate("CirrosisView", "D"))
        self.Status.setItemText(1, _translate("CirrosisView", "C"))
        self.Status.setItemText(2, _translate("CirrosisView", "CL"))
        self.Drug.setItemText(0, _translate("CirrosisView", "D-penicillamine"))
        self.Drug.setItemText(1, _translate("CirrosisView", "Placebo"))
        self.Ascites.setItemText(0, _translate("CirrosisView", "Y"))
        self.Ascites.setItemText(1, _translate("CirrosisView", "N"))
        self.Hepatomegaly.setItemText(0, _translate("CirrosisView", "Y"))
        self.Hepatomegaly.setItemText(1, _translate("CirrosisView", "N"))
        self.Spiders.setItemText(0, _translate("CirrosisView", "Y"))
        self.Spiders.setItemText(1, _translate("CirrosisView", "N"))
        self.Edema.setItemText(0, _translate("CirrosisView", "Y"))
        self.Edema.setItemText(1, _translate("CirrosisView", "S"))
        self.Edema.setItemText(2, _translate("CirrosisView", "N"))

    def getData(self):

        Sex = ""
        Status = ""
        Drug = ""
        Ascites = ""
        Hepatomegaly = ""
        Spiders = ""
        Edema = ""

        if self.Sex.currentText() == "Male":
            Sex = "1"
        else:
            Sex = "0"

        if self.Status.currentText() == "D":
            Status = "2"
        elif self.Status.currentText() == "C":
            Status = "0"
        else: 
            Status = "1"
        
        if self.Drug.currentText() == "D-penicillamine":
            Drug = "0"
        else:
            Drug = "1"

        if self.Ascites.currentText() == "N":
            Ascites = "0"
        else:
            Ascites = "1"

        if self.Hepatomegaly.currentText() == "N":
            Hepatomegaly = "0"
        else:
            Hepatomegaly = "1"

        if self.Spiders.currentText() == "N":
            Spiders = "0"
        else:
            Spiders = "1"

        if self.Edema.currentText() == "Y":
            Edema = "2"
        elif self.Edema.currentText() == "N":
            Edema = "1"
        else:
            Edema = "0"

        response = requests.get(url + "/modelCirrosis?N_Days=" + self.NDays.text() + "&Status=" + Status + "&Drug=" + 
        Drug + "&Age=" + self.Age.text() + "&Sex=" + Sex + "&Ascites=" + Ascites + "&Hepatomegaly=" + 
        Hepatomegaly + "&Spiders=" + Spiders + "&Edema=" + Edema + "&Bilirubin=" + self.Bilirubin.text()
         + "&Cholesterol=" + self.Cholesterol.text() + "&Albumin=" + self.Albumin.text() + "&Copper=" + self.Copper.text() + "&Alk_Phos=" + 
         self.AlkPhos.text() + "&SGOT=" + self.SGOT.text() + "&Tryglicerides=" + self.Tryglicerides.text() + "&Platelets=" + 
         self.Platelets.text() + "&Prothrombin=" + self.Prothrombin.text())
        
        info = response.json()

        self.Res.setText(str(info["Result"]["0"]))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CirrosisView = QtWidgets.QMainWindow()
    ui = Ui_CirrosisView()
    ui.setupUi(CirrosisView)
    CirrosisView.show()
    sys.exit(app.exec_())
