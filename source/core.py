#!/usr/local/bin/python
# coding: utf-8

import view, os, shutil, glob, time
from PyQt4 import QtCore, QtGui

def toUtf(text):
	return view._translate("Form", text, None)

class Application(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.folderSaveDir = None
		self.folderBackupDir = None

	# доступные переменные:
	# self.folderSaveDir - папка с сохранениями игры
	#
	# self.folderBackupDir - папка куда сохр. файлы

	def run(self, template):
		self.template = template

		template.selectFolderSave.clicked.connect(self.selectFolderSave)
		template.selectFolderBackup.clicked.connect(self.selectFolderBackup)
		template.toSave.clicked.connect(self.toSave)
		template.pushButton.clicked.connect(self.runTimer)


		template.time.setValidator(QtGui.QIntValidator())
		template.procent.setValidator(QtGui.QIntValidator())

	def isValidWorkflow(self):
		if self.folderSaveDir and self.folderSaveDir != u'' and self.folderBackupDir and self.folderBackupDir != u'':
			self.toggleEnable(True)
		else:
			self.toggleEnable(False)

	def toggleEnable(self, flag):
		BOOL = True if flag else False
		self.template.pushButton.setEnabled(BOOL)
		self.template.procent.setEnabled(BOOL)
		self.template.toSave.setEnabled(BOOL)

	def selectFolderSave(self):
		self.folderSaveDir = QtGui.QFileDialog.getExistingDirectory(self, toUtf('Выбрать папку с сохранениями игры'), 'C:\\')
		self.folderSaveDir = unicode(self.folderSaveDir)

		if self.folderSaveDir == u'':
			self.template.selectFolderSave.setStyleSheet('color:red;')
		else:
			self.template.selectFolderSave.setStyleSheet('color:green;')

		self.isValidWorkflow()

	def selectFolderBackup(self):
		self.folderBackupDir = QtGui.QFileDialog.getExistingDirectory(self, toUtf('Выбрать папку куда сохранять бекапы'), 'C:\\')
		self.folderBackupDir = unicode(self.folderBackupDir)

		if self.folderBackupDir == u'':
			self.template.selectFolderBackup.setStyleSheet('color:red;')
		else:
			self.template.selectFolderBackup.setStyleSheet('color:green;')

		self.isValidWorkflow()

	def toSave(self):
		value = self.template.procent.text()
		self.backupStart(str(value))

	@QtCore.pyqtSlot()
	def backupStart(self, procent=None):
		os.chdir(self.folderBackupDir)

		dirname = 'backup-' + time.strftime('%d.%m.%Y_%H-%M')

		if procent: dirname = dirname + '_' + procent + '%'

		try:
			os.mkdir(dirname)
		except OSError:
			print('Папка уже существует!')
			return False

		for filename in glob.glob(os.path.join(self.folderSaveDir, '*')):
			shutil.copy(filename, self.folderBackupDir + '/' + dirname)

	def runTimer(self):
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.backupStart)
		self.timer.start(int(self.template.time.text()) * 60000)

		self.template.time.setDisabled(True)

		self.template.pushButton.setText(toUtf('Нажмите чтобы остановить'))
		self.template.pushButton.clicked.disconnect(self.runTimer)
		self.template.pushButton.clicked.connect(self.toogleStart)
		self.isPause = False

	def toogleStart(self):
		if self.isPause:
			self.template.pushButton.setText(toUtf('Остановить'))
			self.timer.start()
			self.isPause = False
		else:
			self.template.pushButton.setText(toUtf('Продолжить'))
			self.timer.stop()
			self.isPause = True