# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_PopupTemplate.ui'
#
# Created: Tue Dec 30 16:16:44 2014
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
        MainWindow.resize(207, 355)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButtonExit = QtGui.QPushButton(self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(50, 250, 75, 23))
        self.pushButtonExit.setObjectName(_fromUtf8("pushButtonExit"))
        self.pushButtonSaveFile = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSaveFile.setGeometry(QtCore.QRect(50, 180, 75, 23))
        self.pushButtonSaveFile.setObjectName(_fromUtf8("pushButtonSaveFile"))
        self.pushButtonMessage = QtGui.QPushButton(self.centralwidget)
        self.pushButtonMessage.setGeometry(QtCore.QRect(50, 60, 75, 23))
        self.pushButtonMessage.setObjectName(_fromUtf8("pushButtonMessage"))
        self.pushButtonGetDirectory = QtGui.QPushButton(self.centralwidget)
        self.pushButtonGetDirectory.setGeometry(QtCore.QRect(50, 120, 75, 23))
        self.pushButtonGetDirectory.setObjectName(_fromUtf8("pushButtonGetDirectory"))
        self.pushButtonGetFile = QtGui.QPushButton(self.centralwidget)
        self.pushButtonGetFile.setGeometry(QtCore.QRect(50, 150, 75, 23))
        self.pushButtonGetFile.setObjectName(_fromUtf8("pushButtonGetFile"))
        self.pushButtonQuestion = QtGui.QPushButton(self.centralwidget)
        self.pushButtonQuestion.setGeometry(QtCore.QRect(50, 90, 75, 23))
        self.pushButtonQuestion.setObjectName(_fromUtf8("pushButtonQuestion"))
        self.pushButtonListSelect = QtGui.QPushButton(self.centralwidget)
        self.pushButtonListSelect.setGeometry(QtCore.QRect(50, 210, 75, 23))
        self.pushButtonListSelect.setObjectName(_fromUtf8("pushButtonListSelect"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 207, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuExit = QtGui.QMenu(self.menubar)
        self.menuExit.setObjectName(_fromUtf8("menuExit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuExit.addAction(self.actionExit)
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButtonExit, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButtonExit.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Popup Template", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSaveFile.setText(QtGui.QApplication.translate("MainWindow", "Save File", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonMessage.setText(QtGui.QApplication.translate("MainWindow", "Message", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGetDirectory.setText(QtGui.QApplication.translate("MainWindow", "Get Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGetFile.setText(QtGui.QApplication.translate("MainWindow", "Get File", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonQuestion.setText(QtGui.QApplication.translate("MainWindow", "Question", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonListSelect.setText(QtGui.QApplication.translate("MainWindow", "List Select", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExit.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

