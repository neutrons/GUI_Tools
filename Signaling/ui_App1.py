# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_App1.ui'
#
# Created: Mon Feb 02 09:45:22 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(585, 306)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButtonLaunchApp2 = QtGui.QPushButton(self.centralwidget)
        self.pushButtonLaunchApp2.setGeometry(QtCore.QRect(30, 10, 161, 23))
        self.pushButtonLaunchApp2.setObjectName(_fromUtf8("pushButtonLaunchApp2"))
        self.textEditDisplayText = QtGui.QTextEdit(self.centralwidget)
        self.textEditDisplayText.setEnabled(True)
        self.textEditDisplayText.setGeometry(QtCore.QRect(30, 100, 511, 161))
        self.textEditDisplayText.setReadOnly(True)
        self.textEditDisplayText.setObjectName(_fromUtf8("textEditDisplayText"))
        self.lineEditEnterText = QtGui.QLineEdit(self.centralwidget)
        self.lineEditEnterText.setGeometry(QtCore.QRect(140, 40, 401, 20))
        self.lineEditEnterText.setObjectName(_fromUtf8("lineEditEnterText"))
        self.pushButtonUpdate = QtGui.QPushButton(self.centralwidget)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(30, 70, 161, 23))
        self.pushButtonUpdate.setObjectName(_fromUtf8("pushButtonUpdate"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(mainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "App1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLaunchApp2.setText(QtGui.QApplication.translate("mainWindow", "Launch App 2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUpdate.setText(QtGui.QApplication.translate("mainWindow", "Update Text Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mainWindow", "Enter Text:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("mainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("mainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

