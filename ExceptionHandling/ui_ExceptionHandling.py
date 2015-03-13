# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ExceptionHandling.ui'
#
# Created: Fri Mar 13 11:34:46 2015
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
        MainWindow.resize(390, 516)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButtonExit = QtGui.QPushButton(self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(250, 440, 75, 23))
        self.pushButtonExit.setObjectName(_fromUtf8("pushButtonExit"))
        self.lineEditA = QtGui.QLineEdit(self.centralwidget)
        self.lineEditA.setGeometry(QtCore.QRect(60, 50, 71, 20))
        self.lineEditA.setObjectName(_fromUtf8("lineEditA"))
        self.comboBoxOperator = QtGui.QComboBox(self.centralwidget)
        self.comboBoxOperator.setGeometry(QtCore.QRect(140, 50, 121, 22))
        self.comboBoxOperator.setObjectName(_fromUtf8("comboBoxOperator"))
        self.comboBoxOperator.addItem(_fromUtf8(""))
        self.comboBoxOperator.addItem(_fromUtf8(""))
        self.comboBoxOperator.addItem(_fromUtf8(""))
        self.comboBoxOperator.addItem(_fromUtf8(""))
        self.comboBoxOperator.addItem(_fromUtf8(""))
        self.lineEditB = QtGui.QLineEdit(self.centralwidget)
        self.lineEditB.setGeometry(QtCore.QRect(270, 50, 71, 20))
        self.lineEditB.setObjectName(_fromUtf8("lineEditB"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 30, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(155, 30, 51, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.labelResult = QtGui.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(40, 140, 171, 16))
        self.labelResult.setObjectName(_fromUtf8("labelResult"))
        self.pushButtonCalc = QtGui.QPushButton(self.centralwidget)
        self.pushButtonCalc.setGeometry(QtCore.QRect(30, 100, 75, 23))
        self.pushButtonCalc.setObjectName(_fromUtf8("pushButtonCalc"))
        self.textEditOutLog = QtGui.QTextEdit(self.centralwidget)
        self.textEditOutLog.setGeometry(QtCore.QRect(30, 220, 341, 211))
        self.textEditOutLog.setUndoRedoEnabled(False)
        self.textEditOutLog.setReadOnly(True)
        self.textEditOutLog.setObjectName(_fromUtf8("textEditOutLog"))
        self.labelResult_2 = QtGui.QLabel(self.centralwidget)
        self.labelResult_2.setGeometry(QtCore.QRect(40, 190, 171, 16))
        self.labelResult_2.setObjectName(_fromUtf8("labelResult_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 21))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "App Template", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxOperator.setItemText(0, QtGui.QApplication.translate("MainWindow", "Select Operator", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxOperator.setItemText(1, QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxOperator.setItemText(2, QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxOperator.setItemText(3, QtGui.QApplication.translate("MainWindow", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxOperator.setItemText(4, QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Operator", None, QtGui.QApplication.UnicodeUTF8))
        self.labelResult.setText(QtGui.QApplication.translate("MainWindow", "Result: ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCalc.setText(QtGui.QApplication.translate("MainWindow", "Calculate", None, QtGui.QApplication.UnicodeUTF8))
        self.labelResult_2.setText(QtGui.QApplication.translate("MainWindow", "Output Log", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExit.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

