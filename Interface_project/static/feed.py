# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feed.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_feed(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 589)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(30, 320, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(30, 50, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 15, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 80, 331, 243))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 2, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 4, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 7, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(30, 350, 333, 185))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_2.addWidget(self.lineEdit_13, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget1)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_2.addWidget(self.lineEdit_14, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget1)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_2.addWidget(self.lineEdit_15, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget1)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_2.addWidget(self.lineEdit_17, 4, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget1)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 5, 0, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_2.addWidget(self.lineEdit_16, 5, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget1)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 6, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_2.addWidget(self.lineEdit_18, 6, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Дата"))
        self.label_9.setText(_translate("Form", "Температуры, ℃"))
        self.label_17.setText(_translate("Form", "Содержание, %мас"))
        self.label_2.setText(_translate("Form", "Легкая ароматика"))
        self.label_18.setText(_translate("Form", "Полиароматика"))
        self.label_5.setText(_translate("Form", "Смолы\n"
""))
        self.label_4.setText(_translate("Form", "Биароматика"))
        self.label_6.setText(_translate("Form", "Сера"))
        self.label_7.setText(_translate("Form", "Плотность при 20 ℃, г/см3"))
        self.label_8.setText(_translate("Form", "Молекулярная масса сырья, г/моль"))
        self.label_3.setText(_translate("Form", "Насыщенные углеводороды"))
        self.label_11.setText(_translate("Form", "Начала кипения"))
        self.label_10.setText(_translate("Form", "10%"))
        self.label_12.setText(_translate("Form", "50%"))
        self.label_16.setText(_translate("Form", "90%"))
        self.label_14.setText(_translate("Form", "95%"))
        self.label_15.setText(_translate("Form", "Конца кипения"))
        self.label_13.setText(_translate("Form", "Доля углерода в нафтеновых структурах"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_feed()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
