# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegexTester.ui'
#
# Created: Wed Dec 18 18:57:26 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 621, 91))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.textEdit_Regex = QtGui.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_Regex.setObjectName(_fromUtf8("textEdit_Regex"))
        self.verticalLayout_2.addWidget(self.textEdit_Regex)
        self.verticalLayoutWidget_3 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 150, 621, 321))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.textEdit_Data = QtGui.QTextEdit(self.verticalLayoutWidget_3)
        self.textEdit_Data.setObjectName(_fromUtf8("textEdit_Data"))
        self.verticalLayout_3.addWidget(self.textEdit_Data)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox_CI = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_CI.setObjectName(_fromUtf8("checkBox_CI"))
        self.horizontalLayout.addWidget(self.checkBox_CI)
        self.checkBox_MB = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_MB.setObjectName(_fromUtf8("checkBox_MB"))
        self.horizontalLayout.addWidget(self.checkBox_MB)
        self.checkBox_DM = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_DM.setObjectName(_fromUtf8("checkBox_DM"))
        self.horizontalLayout.addWidget(self.checkBox_DM)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Regex Tester", None))
        self.label.setText(_translate("Dialog", "Regex:", None))
        self.label_2.setText(_translate("Dialog", "Test data:", None))
        self.checkBox_CI.setText(_translate("Dialog", "Case insensitive (i)", None))
        self.checkBox_MB.setText(_translate("Dialog", "^$ match at line breaks (m)", None))
        self.checkBox_DM.setText(_translate("Dialog", "Dot matches all (s)", None))

