# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TreeViewExperiment.ui'
#
# Created: Tue Aug 18 17:05:55 2015
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
        MainWindow.resize(1023, 798)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeView_main = QtGui.QTreeView(self.centralwidget)
        self.treeView_main.setObjectName(_fromUtf8("treeView_main"))
        self.verticalLayout.addWidget(self.treeView_main)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_appendCol0 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_appendCol0.setObjectName(_fromUtf8("pushButton_appendCol0"))
        self.gridLayout.addWidget(self.pushButton_appendCol0, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.lineEdit_col1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_col1.setObjectName(_fromUtf8("lineEdit_col1"))
        self.gridLayout.addWidget(self.lineEdit_col1, 2, 1, 1, 1)
        self.lineEdit_col0 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_col0.setObjectName(_fromUtf8("lineEdit_col0"))
        self.gridLayout.addWidget(self.lineEdit_col0, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_appendCol1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_appendCol1.setObjectName(_fromUtf8("pushButton_appendCol1"))
        self.gridLayout.addWidget(self.pushButton_appendCol1, 4, 1, 1, 1)
        self.pushButton_addCol0 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_addCol0.setObjectName(_fromUtf8("pushButton_addCol0"))
        self.gridLayout.addWidget(self.pushButton_addCol0, 3, 0, 1, 1)
        self.pushButton_addCol1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_addCol1.setObjectName(_fromUtf8("pushButton_addCol1"))
        self.gridLayout.addWidget(self.pushButton_addCol1, 3, 1, 1, 1)
        self.pushButton_removeLastCol1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_removeLastCol1.setObjectName(_fromUtf8("pushButton_removeLastCol1"))
        self.gridLayout.addWidget(self.pushButton_removeLastCol1, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.treeView_custom = CustomizedTreeView(self.centralwidget)
        self.treeView_custom.setObjectName(_fromUtf8("treeView_custom"))
        self.verticalLayout_3.addWidget(self.treeView_custom)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_addIPTS = QtGui.QPushButton(self.centralwidget)
        self.pushButton_addIPTS.setObjectName(_fromUtf8("pushButton_addIPTS"))
        self.gridLayout_2.addWidget(self.pushButton_addIPTS, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.pushButton_sortRun = QtGui.QPushButton(self.centralwidget)
        self.pushButton_sortRun.setObjectName(_fromUtf8("pushButton_sortRun"))
        self.gridLayout_2.addWidget(self.pushButton_sortRun, 5, 1, 1, 1)
        self.pushButton_insertRun = QtGui.QPushButton(self.centralwidget)
        self.pushButton_insertRun.setObjectName(_fromUtf8("pushButton_insertRun"))
        self.gridLayout_2.addWidget(self.pushButton_insertRun, 4, 1, 1, 1)
        self.lineEdit_ipts = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_ipts.setObjectName(_fromUtf8("lineEdit_ipts"))
        self.gridLayout_2.addWidget(self.lineEdit_ipts, 1, 0, 1, 1)
        self.lineEdit_run = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_run.setObjectName(_fromUtf8("lineEdit_run"))
        self.gridLayout_2.addWidget(self.lineEdit_run, 1, 1, 1, 1)
        self.pushButton_sortIPTS = QtGui.QPushButton(self.centralwidget)
        self.pushButton_sortIPTS.setObjectName(_fromUtf8("pushButton_sortIPTS"))
        self.gridLayout_2.addWidget(self.pushButton_sortIPTS, 5, 0, 1, 1)
        self.pushButton_addRun = QtGui.QPushButton(self.centralwidget)
        self.pushButton_addRun.setObjectName(_fromUtf8("pushButton_addRun"))
        self.gridLayout_2.addWidget(self.pushButton_addRun, 2, 1, 1, 1)
        self.pushButton_clearModel = QtGui.QPushButton(self.centralwidget)
        self.pushButton_clearModel.setObjectName(_fromUtf8("pushButton_clearModel"))
        self.gridLayout_2.addWidget(self.pushButton_clearModel, 4, 0, 1, 1)
        self.pushButton_addIptsRun = QtGui.QPushButton(self.centralwidget)
        self.pushButton_addIptsRun.setObjectName(_fromUtf8("pushButton_addIptsRun"))
        self.gridLayout_2.addWidget(self.pushButton_addIptsRun, 3, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.treeView_file = QtGui.QTreeView(self.centralwidget)
        self.treeView_file.setObjectName(_fromUtf8("treeView_file"))
        self.horizontalLayout.addWidget(self.treeView_file)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.treeView_fileSystem = FileSystemTreeView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_fileSystem.sizePolicy().hasHeightForWidth())
        self.treeView_fileSystem.setSizePolicy(sizePolicy)
        self.treeView_fileSystem.setObjectName(_fromUtf8("treeView_fileSystem"))
        self.verticalLayout_2.addWidget(self.treeView_fileSystem)
        self.lineEdit_rootPath = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_rootPath.setObjectName(_fromUtf8("lineEdit_rootPath"))
        self.verticalLayout_2.addWidget(self.lineEdit_rootPath)
        self.pushButton_browseRootPath = QtGui.QPushButton(self.centralwidget)
        self.pushButton_browseRootPath.setObjectName(_fromUtf8("pushButton_browseRootPath"))
        self.verticalLayout_2.addWidget(self.pushButton_browseRootPath)
        self.lineEdit_currentPath = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_currentPath.setObjectName(_fromUtf8("lineEdit_currentPath"))
        self.verticalLayout_2.addWidget(self.lineEdit_currentPath)
        self.pushButton_setCurrentDir = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setCurrentDir.setObjectName(_fromUtf8("pushButton_setCurrentDir"))
        self.verticalLayout_2.addWidget(self.pushButton_setCurrentDir)
        self.pushButton_getCurrentPath = QtGui.QPushButton(self.centralwidget)
        self.pushButton_getCurrentPath.setObjectName(_fromUtf8("pushButton_getCurrentPath"))
        self.verticalLayout_2.addWidget(self.pushButton_getCurrentPath)
        self.lineEdit_readOutCurrentPath = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_readOutCurrentPath.setObjectName(_fromUtf8("lineEdit_readOutCurrentPath"))
        self.verticalLayout_2.addWidget(self.lineEdit_readOutCurrentPath)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1023, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_appendCol0.setText(_translate("MainWindow", "Append", None))
        self.label_2.setText(_translate("MainWindow", "Column 1", None))
        self.label.setText(_translate("MainWindow", "Column 0", None))
        self.pushButton_appendCol1.setText(_translate("MainWindow", "Append", None))
        self.pushButton_addCol0.setText(_translate("MainWindow", "Add", None))
        self.pushButton_addCol1.setText(_translate("MainWindow", "Add", None))
        self.pushButton_removeLastCol1.setText(_translate("MainWindow", "Remove Last", None))
        self.pushButton_addIPTS.setText(_translate("MainWindow", "Add IPTS", None))
        self.label_4.setText(_translate("MainWindow", "RUN", None))
        self.label_3.setText(_translate("MainWindow", "IPTS", None))
        self.pushButton_sortRun.setText(_translate("MainWindow", "Sort Run", None))
        self.pushButton_insertRun.setText(_translate("MainWindow", "Insert Run", None))
        self.pushButton_sortIPTS.setText(_translate("MainWindow", "Sort IPTS", None))
        self.pushButton_addRun.setText(_translate("MainWindow", "Add Run", None))
        self.pushButton_clearModel.setText(_translate("MainWindow", "Clear", None))
        self.pushButton_addIptsRun.setText(_translate("MainWindow", "Add IPTS-Run", None))
        self.pushButton_browseRootPath.setText(_translate("MainWindow", "Browse Root Path", None))
        self.pushButton_setCurrentDir.setText(_translate("MainWindow", "Browse Current Path", None))
        self.pushButton_getCurrentPath.setText(_translate("MainWindow", "Get Current Path", None))

from FileSystemTreeView import FileSystemTreeView
from CustomizedTreeView import CustomizedTreeView
