# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hourly_Rent.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Hourly_Rent(object):
    def setupUi(self, Loading):
        Loading.setObjectName("Loading")
        Loading.resize(547, 537)
        self.centralwidget = QtWidgets.QWidget(Loading)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 551, 541))
        self.frame.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(170, 0, 221, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/rental22).png"))
        self.label_2.setObjectName("label_2")
        self.radioButton_1 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_1.setGeometry(QtCore.QRect(30, 230, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setStyleSheet("background-color:none;\n"
"color: rgb(148, 33, 48);")
        self.radioButton_1.setCheckable(False)
        self.radioButton_1.setObjectName("radioButton_1")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 180, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:none;\n"
"color: rgb(148, 33, 48);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 270, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setAutoFillBackground(False)
        self.radioButton_2.setStyleSheet("background-color:none;\n"
"color: rgb(148, 33, 48);")
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 310, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("background-color:none;\n"
"color: rgb(148, 33, 48);")
        self.radioButton_3.setCheckable(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 350, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("background-color:none;\n"
"color: rgb(148, 33, 48);")
        self.radioButton_4.setCheckable(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_5.setGeometry(QtCore.QRect(30, 390, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet("background-color:none;\n"
"color: rgb(148, 33, 48);")
        self.radioButton_5.setCheckable(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.label_m2 = QtWidgets.QLabel(self.frame)
        self.label_m2.setGeometry(QtCore.QRect(70, 450, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_m2.setFont(font)
        self.label_m2.setStyleSheet("background-color:none;\n"
"color: rgb(50, 63, 107);")
        self.label_m2.setText("")
        self.label_m2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_m2.setObjectName("label_m2")
        self.label_m1 = QtWidgets.QLabel(self.frame)
        self.label_m1.setGeometry(QtCore.QRect(70, 410, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_m1.setFont(font)
        self.label_m1.setStyleSheet("background-color:none;\n"
"color: rgb(50, 63, 107);")
        self.label_m1.setText("")
        self.label_m1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_m1.setObjectName("label_m1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)

        # user manual code
        self.onlyInt = QtGui.QIntValidator()

        self.lineEdit_2.setGeometry(QtCore.QRect(450, 450, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(50, 63, 107);\n"
"border-color:  rgb(148, 33, 48)")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setObjectName("lineEdit_2")

        # user manual code
        self.lineEdit_2.setValidator(self.onlyInt)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame)

        # user manual code
        self.onlyInt = QtGui.QIntValidator()

        self.lineEdit_1.setGeometry(QtCore.QRect(450, 410, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setStyleSheet("color: rgb(50, 63, 107);\n"
"border-color: rgb(148, 33, 48)")
        self.lineEdit_1.setFrame(True)
        self.lineEdit_1.setObjectName("lineEdit_1")

        # user manual code
        self.lineEdit_1.setValidator(self.onlyInt)

        self.pushButton_confirm = QtWidgets.QPushButton(self.frame)
        self.pushButton_confirm.setGeometry(QtCore.QRect(240, 500, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_confirm.setFont(font)
        self.pushButton_confirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_confirm.setStyleSheet("color:  rgb(148, 33, 48);")
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        Loading.setCentralWidget(self.centralwidget)

        self.retranslateUi(Loading)
        QtCore.QMetaObject.connectSlotsByName(Loading)

    def retranslateUi(self, Loading):
        _translate = QtCore.QCoreApplication.translate
        Loading.setWindowTitle(_translate("Loading", "HourlyRentWindow"))
        self.radioButton_1.setText(_translate("Loading", "Show available bikes"))
        self.label_3.setText(_translate("Loading", "Please enter your choice:"))
        self.radioButton_2.setText(_translate("Loading", "Hourly rent: $5"))
        self.radioButton_3.setText(_translate("Loading", "Daily  rent: $20"))
        self.radioButton_4.setText(_translate("Loading", "Weekly rent: $60"))
        self.radioButton_5.setText(_translate("Loading", "Return a bike"))
        self.pushButton_confirm.setText(_translate("Loading", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Loading = QtWidgets.QMainWindow()
    ui = Ui_Hourly_Rent()
    ui.setupUi(Loading)
    Loading.show()
    sys.exit(app.exec_())
