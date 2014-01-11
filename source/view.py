# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created: Fri Jan 10 18:42:29 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(390, 294)
        Form.setMinimumSize(QtCore.QSize(390, 300))
        Form.setMaximumSize(QtCore.QSize(390, 300))
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Belarus))
        self.selectFolderBackup = QtGui.QPushButton(Form)
        self.selectFolderBackup.setGeometry(QtCore.QRect(10, 50, 371, 35))
        self.selectFolderBackup.setStyleSheet(_fromUtf8("color:red;"))
        self.selectFolderBackup.setObjectName(_fromUtf8("selectFolderBackup"))
        self.time = QtGui.QLineEdit(Form)
        self.time.setGeometry(QtCore.QRect(20, 100, 51, 21))
        self.time.setObjectName(_fromUtf8("time"))
        self.timeLabel = QtGui.QLabel(Form)
        self.timeLabel.setGeometry(QtCore.QRect(80, 100, 161, 19))
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.selectFolderSave = QtGui.QPushButton(Form)
        self.selectFolderSave.setGeometry(QtCore.QRect(10, 10, 371, 35))
        self.selectFolderSave.setStyleSheet(_fromUtf8("color:red;"))
        self.selectFolderSave.setObjectName(_fromUtf8("selectFolderSave"))
        self.toSave = QtGui.QPushButton(Form)
        self.toSave.setEnabled(False)
        self.toSave.setGeometry(QtCore.QRect(190, 250, 171, 32))
        self.toSave.setObjectName(_fromUtf8("toSave"))
        self.procent = QtGui.QLineEdit(Form)
        self.procent.setEnabled(False)
        self.procent.setGeometry(QtCore.QRect(30, 250, 151, 31))
        self.procent.setObjectName(_fromUtf8("procent"))
        self.procentLabel = QtGui.QLabel(Form)
        self.procentLabel.setGeometry(QtCore.QRect(30, 220, 211, 19))
        self.procentLabel.setObjectName(_fromUtf8("procentLabel"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 371, 71))
        self.pushButton.setStyleSheet(_fromUtf8("font:700 24px \"Arial\";\n"""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "AC4 Save Backup", None))
        self.selectFolderBackup.setText(_translate("Form", "Выбрать папку куда сохранять бекапы", None))
        self.time.setText(_translate("Form", "10", None))
        self.timeLabel.setText(_translate("Form", "мин. таймер бекапа", None))
        self.selectFolderSave.setText(_translate("Form", "Выбрать папку с сохранениями игры", None))
        self.toSave.setText(_translate("Form", "Сохранить сейчас", None))
        self.procentLabel.setText(_translate("Form", "Проиденный процент:", None))
        self.pushButton.setText(_translate("Form", "Начать бекапить", None))