# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainWindowNDim.ui'
#
# Created: Tue Aug 11 17:08:17 2015
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
        MainWindow.resize(1207, 853)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.canvas = MplGraphicsView(self.centralwidget)
        self.canvas.setObjectName(_fromUtf8("canvas"))
        self.horizontalLayout_2.addWidget(self.canvas)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.pushButton_intoPickMode = QtGui.QPushButton(self.centralwidget)
        self.pushButton_intoPickMode.setObjectName(_fromUtf8("pushButton_intoPickMode"))
        self.horizontalLayout_9.addWidget(self.pushButton_intoPickMode)
        self.pushButton_moveLeft = QtGui.QPushButton(self.centralwidget)
        self.pushButton_moveLeft.setObjectName(_fromUtf8("pushButton_moveLeft"))
        self.horizontalLayout_9.addWidget(self.pushButton_moveLeft)
        self.lineEdit_step = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_step.sizePolicy().hasHeightForWidth())
        self.lineEdit_step.setSizePolicy(sizePolicy)
        self.lineEdit_step.setMinimumSize(QtCore.QSize(20, 0))
        self.lineEdit_step.setObjectName(_fromUtf8("lineEdit_step"))
        self.horizontalLayout_9.addWidget(self.lineEdit_step)
        self.pushButton_moveRight = QtGui.QPushButton(self.centralwidget)
        self.pushButton_moveRight.setObjectName(_fromUtf8("pushButton_moveRight"))
        self.horizontalLayout_9.addWidget(self.pushButton_moveRight)
        self.pushButton_select = QtGui.QPushButton(self.centralwidget)
        self.pushButton_select.setObjectName(_fromUtf8("pushButton_select"))
        self.horizontalLayout_9.addWidget(self.pushButton_select)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.pushButton_cancelInteractMode = QtGui.QPushButton(self.centralwidget)
        self.pushButton_cancelInteractMode.setObjectName(_fromUtf8("pushButton_cancelInteractMode"))
        self.horizontalLayout_9.addWidget(self.pushButton_cancelInteractMode)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lineEdit_maxX = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_maxX.sizePolicy().hasHeightForWidth())
        self.lineEdit_maxX.setSizePolicy(sizePolicy)
        self.lineEdit_maxX.setObjectName(_fromUtf8("lineEdit_maxX"))
        self.gridLayout_4.addWidget(self.lineEdit_maxX, 0, 3, 1, 1)
        self.lineEdit_minX = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_minX.sizePolicy().hasHeightForWidth())
        self.lineEdit_minX.setSizePolicy(sizePolicy)
        self.lineEdit_minX.setObjectName(_fromUtf8("lineEdit_minX"))
        self.gridLayout_4.addWidget(self.lineEdit_minX, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_minY = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_minY.sizePolicy().hasHeightForWidth())
        self.lineEdit_minY.setSizePolicy(sizePolicy)
        self.lineEdit_minY.setObjectName(_fromUtf8("lineEdit_minY"))
        self.gridLayout_4.addWidget(self.lineEdit_minY, 1, 1, 1, 1)
        self.lineEdit_maxY = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_maxY.sizePolicy().hasHeightForWidth())
        self.lineEdit_maxY.setSizePolicy(sizePolicy)
        self.lineEdit_maxY.setObjectName(_fromUtf8("lineEdit_maxY"))
        self.gridLayout_4.addWidget(self.lineEdit_maxY, 1, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 5, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 5, 1, 1)
        self.pushButton_rescale = QtGui.QPushButton(self.centralwidget)
        self.pushButton_rescale.setObjectName(_fromUtf8("pushButton_rescale"))
        self.gridLayout_4.addWidget(self.pushButton_rescale, 0, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit_formular = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_formular.sizePolicy().hasHeightForWidth())
        self.lineEdit_formular.setSizePolicy(sizePolicy)
        self.lineEdit_formular.setObjectName(_fromUtf8("lineEdit_formular"))
        self.horizontalLayout_4.addWidget(self.lineEdit_formular)
        self.pushButton_plot1D = QtGui.QPushButton(self.centralwidget)
        self.pushButton_plot1D.setObjectName(_fromUtf8("pushButton_plot1D"))
        self.horizontalLayout_4.addWidget(self.pushButton_plot1D)
        self.checkBox_overplotF = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_overplotF.setObjectName(_fromUtf8("checkBox_overplotF"))
        self.horizontalLayout_4.addWidget(self.checkBox_overplotF)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_2darrayfile = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2darrayfile.sizePolicy().hasHeightForWidth())
        self.lineEdit_2darrayfile.setSizePolicy(sizePolicy)
        self.lineEdit_2darrayfile.setObjectName(_fromUtf8("lineEdit_2darrayfile"))
        self.horizontalLayout_5.addWidget(self.lineEdit_2darrayfile)
        self.pushButton_plot2D = QtGui.QPushButton(self.centralwidget)
        self.pushButton_plot2D.setObjectName(_fromUtf8("pushButton_plot2D"))
        self.horizontalLayout_5.addWidget(self.pushButton_plot2D)
        self.checkBox_overplot2D = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_overplot2D.setObjectName(_fromUtf8("checkBox_overplot2D"))
        self.horizontalLayout_5.addWidget(self.checkBox_overplot2D)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_imagefile = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_imagefile.sizePolicy().hasHeightForWidth())
        self.lineEdit_imagefile.setSizePolicy(sizePolicy)
        self.lineEdit_imagefile.setObjectName(_fromUtf8("lineEdit_imagefile"))
        self.horizontalLayout_3.addWidget(self.lineEdit_imagefile)
        self.pushButton_plotImage = QtGui.QPushButton(self.centralwidget)
        self.pushButton_plotImage.setObjectName(_fromUtf8("pushButton_plotImage"))
        self.horizontalLayout_3.addWidget(self.pushButton_plotImage)
        self.checkBox_overplotImage = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_overplotImage.setObjectName(_fromUtf8("checkBox_overplotImage"))
        self.horizontalLayout_3.addWidget(self.checkBox_overplotImage)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.pushButton_prevLine = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_prevLine.setObjectName(_fromUtf8("pushButton_prevLine"))
        self.horizontalLayout_8.addWidget(self.pushButton_prevLine)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.pushButton_nextLine = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_nextLine.setObjectName(_fromUtf8("pushButton_nextLine"))
        self.horizontalLayout_8.addWidget(self.pushButton_nextLine)
        self.gridLayout_5.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_delLastLine = QtGui.QPushButton(self.groupBox)
        self.pushButton_delLastLine.setObjectName(_fromUtf8("pushButton_delLastLine"))
        self.gridLayout_2.addWidget(self.pushButton_delLastLine, 1, 0, 1, 1)
        self.pushButton_clear2D = QtGui.QPushButton(self.groupBox)
        self.pushButton_clear2D.setObjectName(_fromUtf8("pushButton_clear2D"))
        self.gridLayout_2.addWidget(self.pushButton_clear2D, 5, 0, 1, 1)
        self.pushButton_delAllLine = QtGui.QPushButton(self.groupBox)
        self.pushButton_delAllLine.setObjectName(_fromUtf8("pushButton_delAllLine"))
        self.gridLayout_2.addWidget(self.pushButton_delAllLine, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.comboBox_lineList = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_lineList.sizePolicy().hasHeightForWidth())
        self.comboBox_lineList.setSizePolicy(sizePolicy)
        self.comboBox_lineList.setObjectName(_fromUtf8("comboBox_lineList"))
        self.horizontalLayout_6.addWidget(self.comboBox_lineList)
        self.pushButton_del1Line = QtGui.QPushButton(self.groupBox)
        self.pushButton_del1Line.setObjectName(_fromUtf8("pushButton_del1Line"))
        self.horizontalLayout_6.addWidget(self.pushButton_del1Line)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 6, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 5, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.comboBox_lineList2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_lineList2.setObjectName(_fromUtf8("comboBox_lineList2"))
        self.horizontalLayout_7.addWidget(self.comboBox_lineList2)
        self.pushButton_changeLine = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_changeLine.setObjectName(_fromUtf8("pushButton_changeLine"))
        self.horizontalLayout_7.addWidget(self.pushButton_changeLine)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)
        self.comboBox_color = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_color.setObjectName(_fromUtf8("comboBox_color"))
        self.gridLayout_3.addWidget(self.comboBox_color, 1, 0, 1, 1)
        self.comboBox_marker = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_marker.setObjectName(_fromUtf8("comboBox_marker"))
        self.gridLayout_3.addWidget(self.comboBox_marker, 2, 0, 1, 1)
        self.comboBox_lineStyle = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_lineStyle.setObjectName(_fromUtf8("comboBox_lineStyle"))
        self.gridLayout_3.addWidget(self.comboBox_lineStyle, 0, 0, 1, 1)
        self.pushButton_changeLastLine = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_changeLastLine.setObjectName(_fromUtf8("pushButton_changeLastLine"))
        self.gridLayout_3.addWidget(self.pushButton_changeLastLine, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1207, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_intoPickMode.setText(_translate("MainWindow", "Pick Mode", None))
        self.pushButton_moveLeft.setText(_translate("MainWindow", "Move Left", None))
        self.lineEdit_step.setToolTip(_translate("MainWindow", "<html><head/><body><p>Step for moving cursor</p></body></html>", None))
        self.pushButton_moveRight.setText(_translate("MainWindow", "Move Right", None))
        self.pushButton_select.setText(_translate("MainWindow", "Select", None))
        self.pushButton_cancelInteractMode.setText(_translate("MainWindow", "Cancel", None))
        self.label_5.setText(_translate("MainWindow", "Min X", None))
        self.label_4.setText(_translate("MainWindow", "Min Y", None))
        self.label_6.setText(_translate("MainWindow", "Max X", None))
        self.label_7.setText(_translate("MainWindow", "Max Y", None))
        self.pushButton_rescale.setText(_translate("MainWindow", "Scale", None))
        self.label.setText(_translate("MainWindow", "Formular", None))
        self.pushButton_plot1D.setText(_translate("MainWindow", "Plot 1D", None))
        self.checkBox_overplotF.setText(_translate("MainWindow", "over plot", None))
        self.label_3.setText(_translate("MainWindow", "2D Array", None))
        self.pushButton_plot2D.setText(_translate("MainWindow", "Fill Plot", None))
        self.checkBox_overplot2D.setText(_translate("MainWindow", "over plot", None))
        self.label_2.setText(_translate("MainWindow", "Location", None))
        self.pushButton_plotImage.setText(_translate("MainWindow", "Plot Image", None))
        self.checkBox_overplotImage.setText(_translate("MainWindow", "over plot", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Viewing", None))
        self.pushButton_prevLine.setText(_translate("MainWindow", "Previous", None))
        self.pushButton_nextLine.setText(_translate("MainWindow", "Next", None))
        self.groupBox.setTitle(_translate("MainWindow", "Add/Delete Line", None))
        self.pushButton_delLastLine.setText(_translate("MainWindow", "Delete Last Line", None))
        self.pushButton_clear2D.setText(_translate("MainWindow", "Clear Image", None))
        self.pushButton_delAllLine.setText(_translate("MainWindow", "Delete All Lines", None))
        self.pushButton_del1Line.setText(_translate("MainWindow", "Delete Line", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Line Style", None))
        self.pushButton_changeLine.setText(_translate("MainWindow", "Change Line Style", None))
        self.pushButton_changeLastLine.setText(_translate("MainWindow", "Change Last Line Style", None))
        self.pushButton_2.setText(_translate("MainWindow", "Empty Slot", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))

from mplgraphicsview import MplGraphicsView
