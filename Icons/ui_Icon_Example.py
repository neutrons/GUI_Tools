# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Icon_Example.ui'
#
# Created: Mon Feb 02 17:02:32 2015
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
        MainWindow.resize(791, 909)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 790, 131, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/PNG Files/resources/Qt_logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 651, 751))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.widget = QtGui.QWidget()
        self.widget.setObjectName(_fromUtf8("widget"))
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 621, 691))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget.addTab(self.widget, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textEdit_2 = QtGui.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 10, 621, 691))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 800, 191, 16))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 21))
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "My Push Button", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Process for Creating a resource file for PyQt: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:10pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-size:10pt;\">In a python project directory, create a &lt;resource&gt;.qrc file: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:11pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:11pt;\">   </span><span style=\" font-size:11pt;\">qrc </span><span style=\" font-family:\'Wingdings\'; font-size:11pt;\">à</span><span style=\" font-size:11pt;\"> Qt Resource Collection </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:11pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:11pt;\">   Example qrc file template </span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">resourcesIcons.qrc</span><span style=\" font-family:\'Times New Roman\'; font-size:11pt;\">:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">&lt;!DOCTYPE RCC&gt;&lt;RCC version=&quot;1.0&quot;&gt;</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">&lt;qresource prefix=&quot;PNG Files&quot;&gt;</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">     &lt;file&gt;resources/Riverbank_logo.png&lt;/file&gt;</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">&lt;/qresource&gt;</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">&lt;qresource prefix=&quot;JPG Files&quot;&gt;</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">     &lt;file&gt;resources/calendar.jpg&lt;/file&gt;</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">&lt;/qresource&gt;</span><span style=\" font-size:10pt;\"> </span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">&lt;/RCC&gt;</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-size:10pt;\">Note in future may chose prefixs to be functional rather than by file type </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:10pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">    </span><span style=\" font-size:10pt;\">Create a subdirectory named \'resources\' within the python development directory </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-size:10pt;\">Place image files in the resources subdirectory </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:10pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-size:10pt;\">Compile resources: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">pyrcc4 -o resourcesIcons_rc.py resourcesIcons.qrc</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:10pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   Resulting products</span><span style=\" font-size:10pt;\">: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-size:10pt;\">&lt;resource&gt;.qrc  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   resources/&lt;files&gt;</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   resourcesIcons_rc.py</span><span style=\" font-size:10pt;\"> </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QtGui.QApplication.translate("MainWindow", "Create Resources", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit_2.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">How to use resources previously created for your project: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:10pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">    Create your</span><span style=\" font-size:10pt;\"> new python project (Icon_Example.py): </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   copy GUI_Tools/Icons/</span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">resourcesIcons.qrc</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\"> to your new  &lt;</span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">project directory</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   copyGUI_Tools/Icons/</span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">resources </span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">subdirectory to  &lt;</span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">project directory</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">&gt;/</span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">resources</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   copy GUI_Tools/Icons/</span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">resourcesIcons_rc.py</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\"> to  &lt;</span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">project directory</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   Full URL: https://github.com/neutrons/GUI_Tools/Icons</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:10pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">    </span><span style=\" font-size:10pt;\">Using Qt Designer </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   Create file</span><span style=\" font-size:10pt;\">: </span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">ui_Icon_Example.py</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   Qt Designer discovers the .qrc file previously located in the python project directory</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-size:10pt;\">Resource Browser </span><span style=\" font-family:\'Wingdings\'; font-size:10pt;\">à</span><span style=\" font-size:10pt;\"> Edit Resources </span><span style=\" font-family:\'Wingdings\'; font-size:10pt;\">à</span><span style=\" font-size:10pt;\"> Open Resource file </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-size:10pt;\">Add icon to button via Qt Designer: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-size:10pt;\">        §</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">  </span><span style=\" font-size:10pt;\">Choose Resource: Select from resources </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:10pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">Compile ui file as usual:</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">pyuic4 -o ui_Icon_Example.py Icon_Example.ui</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:10pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-size:10pt;\">Note that</span><span style=\" font-family:\'Courier New\'; font-size:10pt;\"> ui_Icons_Examples.py </span><span style=\" font-size:10pt;\">will include</span><span style=\" font-family:\'Courier New\'; font-size:10pt;\"> import resourcesIcons_rc.py</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:10pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">Run code as usual:</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-family:\'Courier New\'; font-size:10pt;\">python Icon_Example.py</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">    o</span><span style=\" font-family:\'Times New Roman\'; font-size:10pt;\">   </span><span style=\" font-size:10pt;\">Icon enabled buttons should appear </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Using Resources", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Button with Resource Example:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

import resourcesIcons_rc
