# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_App2.ui'
#
# Created: Mon Feb 02 09:45:31 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_App2(object):
    def setupUi(self, App2):
        App2.setObjectName(_fromUtf8("App2"))
        App2.resize(366, 193)
        self.centralwidget = QtGui.QWidget(App2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButtonSignalApp1 = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSignalApp1.setGeometry(QtCore.QRect(40, 90, 131, 31))
        self.pushButtonSignalApp1.setObjectName(_fromUtf8("pushButtonSignalApp1"))
        self.lineEditApp2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEditApp2.setGeometry(QtCore.QRect(40, 50, 251, 20))
        self.lineEditApp2.setObjectName(_fromUtf8("lineEditApp2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        App2.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(App2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 366, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        App2.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(App2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        App2.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(App2)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(App2)
        QtCore.QMetaObject.connectSlotsByName(App2)

    def retranslateUi(self, App2):
        App2.setWindowTitle(QtGui.QApplication.translate("App2", "App2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSignalApp1.setText(QtGui.QApplication.translate("App2", "Signal App 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("App2", "Text to send to App 1", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("App2", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("App2", "Exit", None, QtGui.QApplication.UnicodeUTF8))

