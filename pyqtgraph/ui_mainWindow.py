# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(1535, 845)
        MainWindow.setMinimumSize(QtCore.QSize(300, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_1 = QtGui.QWidget(self.centralwidget)
        self.widget_1.setObjectName(_fromUtf8("widget_1"))
        self.verticalLayout.addWidget(self.widget_1)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1535, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.action1_Data = QtGui.QAction(MainWindow)
        self.action1_Data.setObjectName(_fromUtf8("action1_Data"))
        self.action2_Normalization = QtGui.QAction(MainWindow)
        self.action2_Normalization.setEnabled(True)
        self.action2_Normalization.setObjectName(_fromUtf8("action2_Normalization"))
        self.action3_Binning = QtGui.QAction(MainWindow)
        self.action3_Binning.setObjectName(_fromUtf8("action3_Binning"))
        self.action4_Fitting = QtGui.QAction(MainWindow)
        self.action4_Fitting.setObjectName(_fromUtf8("action4_Fitting"))
        self.action5_Results = QtGui.QAction(MainWindow)
        self.action5_Results.setObjectName(_fromUtf8("action5_Results"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.action1_Raw_Data = QtGui.QAction(MainWindow)
        self.action1_Raw_Data.setObjectName(_fromUtf8("action1_Raw_Data"))
        self.action2_Normalization_2 = QtGui.QAction(MainWindow)
        self.action2_Normalization_2.setObjectName(_fromUtf8("action2_Normalization_2"))
        self.action3_Normalized_Data = QtGui.QAction(MainWindow)
        self.action3_Normalized_Data.setObjectName(_fromUtf8("action3_Normalized_Data"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.action1_Data.setText(_translate("MainWindow", "1. Data", None))
        self.action2_Normalization.setText(_translate("MainWindow", "2. Normalization", None))
        self.action3_Binning.setText(_translate("MainWindow", "4. Binning", None))
        self.action4_Fitting.setText(_translate("MainWindow", "5. Fitting", None))
        self.action5_Results.setText(_translate("MainWindow", "6. Strain Mapping", None))
        self.actionAbout.setText(_translate("MainWindow", "About ...", None))
        self.action1_Raw_Data.setText(_translate("MainWindow", "1. Raw Data", None))
        self.action2_Normalization_2.setText(_translate("MainWindow", "2. Normalization", None))
        self.action3_Normalized_Data.setText(_translate("MainWindow", "3. Normalized Data", None))

