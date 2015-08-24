# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_UserConfiguration.ui'
#
# Created: Tue Feb  3 15:36:46 2015
#      by: PyQt4 UI code generator 4.11.4-snapshot-db40514060bd
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
        MainWindow.resize(682, 462)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.radioButton1 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton1.setChecked(True)
        self.radioButton1.setObjectName(_fromUtf8("radioButton1"))
        self.verticalLayout_2.addWidget(self.radioButton1)
        self.radioButton2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton2.setObjectName(_fromUtf8("radioButton2"))
        self.verticalLayout_2.addWidget(self.radioButton2)
        self.radioButton3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton3.setObjectName(_fromUtf8("radioButton3"))
        self.verticalLayout_2.addWidget(self.radioButton3)
        self.radioButton4 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton4.setObjectName(_fromUtf8("radioButton4"))
        self.verticalLayout_2.addWidget(self.radioButton4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox1 = QtGui.QCheckBox(self.groupBox)
        self.checkBox1.setObjectName(_fromUtf8("checkBox1"))
        self.verticalLayout.addWidget(self.checkBox1)
        self.checkBox2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox2.setObjectName(_fromUtf8("checkBox2"))
        self.verticalLayout.addWidget(self.checkBox2)
        self.checkBox3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox3.setObjectName(_fromUtf8("checkBox3"))
        self.verticalLayout.addWidget(self.checkBox3)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_3.addWidget(self.textEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 22))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "App2", None))
        self.radioButton1.setText(_translate("MainWindow", "Radio button 1", None))
        self.radioButton2.setText(_translate("MainWindow", "Radio Button 2", None))
        self.radioButton3.setText(_translate("MainWindow", "Radio Button 3", None))
        self.radioButton4.setText(_translate("MainWindow", "Radio Button 4", None))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.checkBox1.setText(_translate("MainWindow", "Check Box 1", None))
        self.checkBox2.setText(_translate("MainWindow", "Check Box 2", None))
        self.checkBox3.setText(_translate("MainWindow", "Check Box 3", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

