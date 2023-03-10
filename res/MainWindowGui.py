# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BackGroud = QtWidgets.QLabel(self.centralwidget)
        self.BackGroud.setGeometry(QtCore.QRect(0, 0, 854, 480))
        self.BackGroud.setStyleSheet("background-image: url(:/assets/bgs.png);")
        self.BackGroud.setText("")
        self.BackGroud.setObjectName("BackGroud")
        self.But_Label = QtWidgets.QLabel(self.centralwidget)
        self.But_Label.setGeometry(QtCore.QRect(0, 420, 854, 60))
        self.But_Label.setStyleSheet("background-image: url(:/assets/mainbg.png);")
        self.But_Label.setText("")
        self.But_Label.setObjectName("But_Label")
        self.White_Label = QtWidgets.QLabel(self.centralwidget)
        self.White_Label.setGeometry(QtCore.QRect(0, 40, 221, 381))
        self.White_Label.setStyleSheet("background-color: rgba(255, 255, 255, 135);")
        self.White_Label.setText("")
        self.White_Label.setObjectName("White_Label")
        self.Top__Label = QtWidgets.QLabel(self.centralwidget)
        self.Top__Label.setGeometry(QtCore.QRect(0, 0, 854, 40))
        self.Top__Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"微软雅黑\";\n"
"border-image: url(:/assets/mainbg.png);")
        self.Top__Label.setObjectName("Top__Label")
        self.Acount_Label = QtWidgets.QLabel(self.centralwidget)
        self.Acount_Label.setGeometry(QtCore.QRect(50, 110, 120, 30))
        self.Acount_Label.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 170, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.Acount_Label.setObjectName("Acount_Label")
        self.Password_Label = QtWidgets.QLabel(self.centralwidget)
        self.Password_Label.setGeometry(QtCore.QRect(50, 190, 120, 30))
        self.Password_Label.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 170, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.Password_Label.setObjectName("Password_Label")
        self.Acount_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Acount_Edit.setGeometry(QtCore.QRect(20, 150, 180, 30))
        self.Acount_Edit.setStyleSheet("border-image: url(:/assets/mainbg.png);\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.Acount_Edit.setText("")
        self.Acount_Edit.setObjectName("Acount_Edit")
        self.Password_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Password_Edit.setGeometry(QtCore.QRect(20, 230, 180, 30))
        self.Password_Edit.setStyleSheet("border-image: url(:/assets/mainbg.png);\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.Password_Edit.setText("")
        self.Password_Edit.setObjectName("Password_Edit")
        self.Skin_Label = QtWidgets.QLabel(self.centralwidget)
        self.Skin_Label.setGeometry(QtCore.QRect(50, 270, 120, 30))
        self.Skin_Label.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 170, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.Skin_Label.setObjectName("Skin_Label")
        self.Skin_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Skin_Edit.setGeometry(QtCore.QRect(20, 310, 140, 30))
        self.Skin_Edit.setStyleSheet("border-image: url(:/assets/mainbg.png);\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.Skin_Edit.setText("")
        self.Skin_Edit.setObjectName("Skin_Edit")
        self.Skin_Sc = QtWidgets.QPushButton(self.centralwidget)
        self.Skin_Sc.setGeometry(QtCore.QRect(160, 310, 40, 30))
        self.Skin_Sc.setStyleSheet("QPushButton:!hover{\n"
"border-image: url(:/assets/mainbg.png);\n"
"font: 20pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/assets/BT_ht.png);\n"
"font: 20pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/assets/BT_ps.png);\n"
"font: 20pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.Skin_Sc.setObjectName("Skin_Sc")
        self.JavaDir_Label = QtWidgets.QLabel(self.centralwidget)
        self.JavaDir_Label.setGeometry(QtCore.QRect(221, 150, 220, 50))
        self.JavaDir_Label.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 170, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.JavaDir_Label.setObjectName("JavaDir_Label")
        self.McDir_Label = QtWidgets.QLabel(self.centralwidget)
        self.McDir_Label.setGeometry(QtCore.QRect(221, 200, 220, 50))
        self.McDir_Label.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 170, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.McDir_Label.setObjectName("McDir_Label")
        self.Xmx__Label = QtWidgets.QLabel(self.centralwidget)
        self.Xmx__Label.setGeometry(QtCore.QRect(221, 250, 220, 50))
        self.Xmx__Label.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 170, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.Xmx__Label.setObjectName("Xmx__Label")
        self.Xms_Label = QtWidgets.QLabel(self.centralwidget)
        self.Xms_Label.setGeometry(QtCore.QRect(221, 300, 220, 50))
        self.Xms_Label.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 170, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.Xms_Label.setObjectName("Xms_Label")
        self.Xmx_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Xmx_Edit.setGeometry(QtCore.QRect(440, 260, 370, 30))
        self.Xmx_Edit.setStyleSheet("border-image: url(:/assets/mainbg.png);\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.Xmx_Edit.setText("")
        self.Xmx_Edit.setObjectName("Xmx_Edit")
        self.Xms_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Xms_Edit.setGeometry(QtCore.QRect(440, 310, 370, 30))
        self.Xms_Edit.setStyleSheet("border-image: url(:/assets/mainbg.png);\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.Xms_Edit.setText("")
        self.Xms_Edit.setObjectName("Xms_Edit")
        self.JavaDir_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.JavaDir_Edit.setGeometry(QtCore.QRect(440, 160, 330, 30))
        self.JavaDir_Edit.setStyleSheet("border-image: url(:/assets/mainbg.png);\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.JavaDir_Edit.setText("")
        self.JavaDir_Edit.setObjectName("JavaDir_Edit")
        self.McDir_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.McDir_Edit.setGeometry(QtCore.QRect(440, 210, 330, 30))
        self.McDir_Edit.setStyleSheet("border-image: url(:/assets/mainbg.png);\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.McDir_Edit.setText("")
        self.McDir_Edit.setObjectName("McDir_Edit")
        self.JavaDir_Sc = QtWidgets.QPushButton(self.centralwidget)
        self.JavaDir_Sc.setGeometry(QtCore.QRect(770, 160, 40, 30))
        self.JavaDir_Sc.setStyleSheet("QPushButton:!hover{\n"
"border-image: url(:/assets/mainbg.png);\n"
"font: 20pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/assets/BT_ht.png);\n"
"font: 20pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/assets/BT_ps.png);\n"
"font: 20pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.JavaDir_Sc.setObjectName("JavaDir_Sc")
        self.McDir_Sc = QtWidgets.QPushButton(self.centralwidget)
        self.McDir_Sc.setGeometry(QtCore.QRect(770, 210, 40, 30))
        self.McDir_Sc.setStyleSheet("QPushButton:!hover{\n"
"border-image: url(:/assets/mainbg.png);\n"
"font: 20pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/assets/BT_ht.png);\n"
"font: 20pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/assets/BT_ps.png);\n"
"font: 20pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.McDir_Sc.setObjectName("McDir_Sc")
        self.Main_Close = QtWidgets.QPushButton(self.centralwidget)
        self.Main_Close.setGeometry(QtCore.QRect(820, 10, 20, 20))
        self.Main_Close.setStyleSheet("QPushButton:!hover{\n"
"border-image: url(:/assets/close.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border-image: url(:/assets/close2.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-image: url(:/assets/close2.png);\n"
"}\n"
"")
        self.Main_Close.setText("")
        self.Main_Close.setObjectName("Main_Close")
        self.Main_Mix = QtWidgets.QPushButton(self.centralwidget)
        self.Main_Mix.setGeometry(QtCore.QRect(790, 0, 20, 30))
        self.Main_Mix.setStyleSheet("font: 75 40pt \"微软雅黑\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.Main_Mix.setObjectName("Main_Mix")
        self.Launch_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Launch_Button.setGeometry(QtCore.QRect(355, 420, 140, 60))
        self.Launch_Button.setStyleSheet("QPushButton:!hover{\n"
"\n"
"    background-color: rgb(0, 170, 0);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 0px;  border: 0px groove gray;\n"
"    border-style: outset;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 190, 0);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 0px;  border: 0px groove gray;\n"
"    border-style: outset;\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(0, 165, 0);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 0px;  border: 0px groove gray;\n"
"    border-style: outset;\n"
"}\n"
"    ")
        self.Launch_Button.setObjectName("Launch_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.Acount_Label.setBuddy(self.Acount_Edit)
        self.Password_Label.setBuddy(self.Password_Edit)
        self.Skin_Label.setBuddy(self.Skin_Edit)
        self.JavaDir_Label.setBuddy(self.JavaDir_Edit)
        self.McDir_Label.setBuddy(self.McDir_Edit)
        self.Xmx__Label.setBuddy(self.Xmx_Edit)
        self.Xms_Label.setBuddy(self.Xms_Edit)

        self.retranslateUi(MainWindow)
        self.Main_Close.clicked.connect(MainWindow.close)
        self.Main_Mix.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Top__Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">MCLP 0.0.1 Beta</span></p></body></html>"))
        self.Acount_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Acount</span></p></body></html>"))
        self.Password_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Password</span></p></body></html>"))
        self.Skin_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Skin</span></p></body></html>"))
        self.Skin_Sc.setText(_translate("MainWindow", "..."))
        self.JavaDir_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Java Diretory</span></p></body></html>"))
        self.McDir_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Minecraft Dirtory</span></p></body></html>"))
        self.Xmx__Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Java Max Memory(MB)</span></p></body></html>"))
        self.Xms_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Java Min Memory(MB)</span></p></body></html>"))
        self.JavaDir_Sc.setText(_translate("MainWindow", "..."))
        self.McDir_Sc.setText(_translate("MainWindow", "..."))
        self.Main_Mix.setText(_translate("MainWindow", "-"))
        self.Launch_Button.setText(_translate("MainWindow", "Launch"))
