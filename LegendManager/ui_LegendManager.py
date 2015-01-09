# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_LegendManager.ui'
#
# Created: Thu Jan 08 14:49:46 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindowLegend(object):
    def setupUi(self, MainWindowLegend):
        MainWindowLegend.setObjectName(_fromUtf8("MainWindowLegend"))
        MainWindowLegend.resize(410, 264)
        self.centralwidget = QtGui.QWidget(MainWindowLegend)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidgetLegend = QtGui.QTableWidget(self.centralwidget)
        self.tableWidgetLegend.setGeometry(QtCore.QRect(20, 20, 291, 192))
        self.tableWidgetLegend.setRowCount(4)
        self.tableWidgetLegend.setColumnCount(2)
        self.tableWidgetLegend.setObjectName(_fromUtf8("tableWidgetLegend"))
        self.tableWidgetLegend.setColumnCount(2)
        self.tableWidgetLegend.setRowCount(4)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetLegend.setItem(0, 0, item)
        self.pushButtonSelectAll = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSelectAll.setGeometry(QtCore.QRect(320, 50, 75, 23))
        self.pushButtonSelectAll.setObjectName(_fromUtf8("pushButtonSelectAll"))
        self.pushButtonClearAll = QtGui.QPushButton(self.centralwidget)
        self.pushButtonClearAll.setGeometry(QtCore.QRect(320, 80, 75, 23))
        self.pushButtonClearAll.setObjectName(_fromUtf8("pushButtonClearAll"))
        self.pushButtonUpdatePlot = QtGui.QPushButton(self.centralwidget)
        self.pushButtonUpdatePlot.setGeometry(QtCore.QRect(320, 110, 75, 23))
        self.pushButtonUpdatePlot.setObjectName(_fromUtf8("pushButtonUpdatePlot"))
        self.pushButtonExit = QtGui.QPushButton(self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(320, 190, 75, 23))
        self.pushButtonExit.setObjectName(_fromUtf8("pushButtonExit"))
        MainWindowLegend.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowLegend)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindowLegend.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowLegend)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowLegend.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowLegend)
        QtCore.QMetaObject.connectSlotsByName(MainWindowLegend)

    def retranslateUi(self, MainWindowLegend):
        MainWindowLegend.setWindowTitle(QtGui.QApplication.translate("MainWindowLegend", "Legend Manager", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tableWidgetLegend.isSortingEnabled()
        self.tableWidgetLegend.setSortingEnabled(False)
        self.tableWidgetLegend.setSortingEnabled(__sortingEnabled)
        self.pushButtonSelectAll.setText(QtGui.QApplication.translate("MainWindowLegend", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonClearAll.setText(QtGui.QApplication.translate("MainWindowLegend", "Clear All", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUpdatePlot.setText(QtGui.QApplication.translate("MainWindowLegend", "Update Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonExit.setText(QtGui.QApplication.translate("MainWindowLegend", "Exit", None, QtGui.QApplication.UnicodeUTF8))

