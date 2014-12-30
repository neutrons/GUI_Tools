#!/usr/bin/python

#import utility modules
import sys

#import PyQt modules
from PyQt4 import QtGui, QtCore, Qt

#include this try/except block to remap QString needed when using IPython
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

#import GUI components generated from Qt Designer .ui file
from ui_AppTemplate import *

class AppTemplateMain(QtGui.QMainWindow):
    
    #initialize app
    def __init__(self, parent=None):
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle("App Template Main")
        self.ui = Ui_MainWindow() #defined in ui_AppTemplate.py
        self.ui.setupUi(self)
    
        #add action exit for File --> Exit menu option
        self.connect(self.ui.actionExit, QtCore.SIGNAL('triggered()'), self.confirmExit)
        #add signal/slot connection for pushbutton exit request
        self.connect(self.ui.pushButtonExit, QtCore.SIGNAL('clicked()'), self.confirmExit)
        
    def confirmExit(self):
        reply = QtGui.QMessageBox.question(self, 'Message',
        "Are you sure to quit?", QtGui.QMessageBox.Yes | 
        QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        
        if reply == QtGui.QMessageBox.Yes:
        #close application
            self.close()
        else:
        #do nothing and return
            pass     
    
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AppTemplateMain()
    myapp.show()

    exit_code=app.exec_()
    #print "exit code: ",exit_code
    sys.exit(exit_code)