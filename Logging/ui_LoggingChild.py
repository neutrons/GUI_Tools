# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_LoggingChild.ui'
#
# Created: Fri Mar 20 11:43:30 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(265, 320)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButtonCritical = QtGui.QPushButton(self.centralwidget)
        self.pushButtonCritical.setGeometry(QtCore.QRect(30, 140, 81, 23))
        self.pushButtonCritical.setObjectName(_fromUtf8("pushButtonCritical"))
        self.pushButtonInfo = QtGui.QPushButton(self.centralwidget)
        self.pushButtonInfo.setGeometry(QtCore.QRect(30, 50, 81, 23))
        self.pushButtonInfo.setObjectName(_fromUtf8("pushButtonInfo"))
        self.pushButtonDebug = QtGui.QPushButton(self.centralwidget)
        self.pushButtonDebug.setGeometry(QtCore.QRect(30, 20, 81, 23))
        self.pushButtonDebug.setObjectName(_fromUtf8("pushButtonDebug"))
        self.pushButtonError = QtGui.QPushButton(self.centralwidget)
        self.pushButtonError.setGeometry(QtCore.QRect(30, 110, 81, 23))
        self.pushButtonError.setObjectName(_fromUtf8("pushButtonError"))
        self.pushButtonWarning = QtGui.QPushButton(self.centralwidget)
        self.pushButtonWarning.setGeometry(QtCore.QRect(30, 80, 81, 23))
        self.pushButtonWarning.setObjectName(_fromUtf8("pushButtonWarning"))
        self.pushButtonAll = QtGui.QPushButton(self.centralwidget)
        self.pushButtonAll.setGeometry(QtCore.QRect(30, 200, 81, 23))
        self.pushButtonAll.setObjectName(_fromUtf8("pushButtonAll"))
        self.pushButtonExit = QtGui.QPushButton(self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(170, 240, 75, 23))
        self.pushButtonExit.setObjectName(_fromUtf8("pushButtonExit"))
        self.pushButtonException = QtGui.QPushButton(self.centralwidget)
        self.pushButtonException.setGeometry(QtCore.QRect(30, 170, 81, 23))
        self.pushButtonException.setObjectName(_fromUtf8("pushButtonException"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 265, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCritical.setText(QtGui.QApplication.translate("MainWindow", "Log Critical", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonInfo.setText(QtGui.QApplication.translate("MainWindow", "Log Info", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDebug.setText(QtGui.QApplication.translate("MainWindow", "Log Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonError.setText(QtGui.QApplication.translate("MainWindow", "Log Error", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonWarning.setText(QtGui.QApplication.translate("MainWindow", "Log Warning", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAll.setText(QtGui.QApplication.translate("MainWindow", "Log All", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonException.setText(QtGui.QApplication.translate("MainWindow", "Log Exception", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

