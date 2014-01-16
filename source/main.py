#!/usr/local/bin/python
# coding: utf-8

import sys, view, core, ctypes, os
from PyQt4 import QtGui, QtCore

if __name__ == "__main__":
	appexe = QtGui.QApplication(sys.argv)

	widget = core.Application()
	template = view.Ui_Form()
	template.setupUi(widget)

	appexe.setWindowIcon(QtGui.QIcon('ac4.png'))
	widget.setWindowIcon(QtGui.QIcon('ac4.png'))

	widget.run(template)

	myappid = 'csscodeRu.ac.sb.1' # arbitrary string
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

	widget.show()

	sys.exit(appexe.exec_())