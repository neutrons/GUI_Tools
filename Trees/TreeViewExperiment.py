# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TreeViewExperiment.ui'
#
# Created: Fri Aug 14 12:16:32 2015
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(889, 1023)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 4, 1, 1)
        self.lineEdit_col0 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_col0.setObjectName(_fromUtf8("lineEdit_col0"))
        self.gridLayout.addWidget(self.lineEdit_col0, 2, 4, 1, 1)
        self.pushButton_addCol1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_addCol1.setObjectName(_fromUtf8("pushButton_addCol1"))
        self.gridLayout.addWidget(self.pushButton_addCol1, 3, 5, 1, 1)
        self.plainTextEdit_main = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_main.setObjectName(_fromUtf8("plainTextEdit_main"))
        self.gridLayout.addWidget(self.plainTextEdit_main, 0, 4, 1, 2)
        self.lineEdit_col1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_col1.setObjectName(_fromUtf8("lineEdit_col1"))
        self.gridLayout.addWidget(self.lineEdit_col1, 2, 5, 1, 1)
        self.treeView_file = QtGui.QTreeView(self.centralwidget)
        self.treeView_file.setObjectName(_fromUtf8("treeView_file"))
        self.gridLayout.addWidget(self.treeView_file, 0, 6, 7, 1)
        self.pushButton_appendCol0 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_appendCol0.setObjectName(_fromUtf8("pushButton_appendCol0"))
        self.gridLayout.addWidget(self.pushButton_appendCol0, 4, 4, 1, 1)
        self.treeView_main = QtGui.QTreeView(self.centralwidget)
        self.treeView_main.setObjectName(_fromUtf8("treeView_main"))
        self.gridLayout.addWidget(self.treeView_main, 0, 1, 7, 1)
        self.pushButton_addCol0 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_addCol0.setObjectName(_fromUtf8("pushButton_addCol0"))
        self.gridLayout.addWidget(self.pushButton_addCol0, 3, 4, 1, 1)
        self.pushButton_appendCol1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_appendCol1.setObjectName(_fromUtf8("pushButton_appendCol1"))
        self.gridLayout.addWidget(self.pushButton_appendCol1, 4, 5, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 5, 1, 1)
        self.pushButton_removeLastCol1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_removeLastCol1.setObjectName(_fromUtf8("pushButton_removeLastCol1"))
        self.gridLayout.addWidget(self.pushButton_removeLastCol1, 5, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Column 0", None))
        self.pushButton_addCol1.setText(_translate("MainWindow", "Add", None))
        self.pushButton_appendCol0.setText(_translate("MainWindow", "Append", None))
        self.pushButton_addCol0.setText(_translate("MainWindow", "Add", None))
        self.pushButton_appendCol1.setText(_translate("MainWindow", "Append", None))
        self.label_2.setText(_translate("MainWindow", "Column 1", None))
        self.pushButton_removeLastCol1.setText(_translate("MainWindow", "Remove Last", None))

