#!/usr/bin/python

#import utility modules
import sys,os

#import PyQt modules
from PyQt4 import QtGui, QtCore, Qt

#include this try/except block to remap QString needed when using IPython
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

#import GUI components generated from Qt Designer .ui file
from ui_PopupTemplate import *

class PopupTemplateMain(QtGui.QMainWindow):
    
    #initialize app
    def __init__(self, parent=None):
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle("Popup Template Main")
        self.ui = Ui_MainWindow() #defined in ui_AppTemplate.py
        self.ui.setupUi(self)
    
        #add action exit for File --> Exit menu option
        QtCore.QObject.connect(self.ui.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), self.confirmExit)
        #add signal/slot connection for pushbutton exit request
        QtCore.QObject.connect(self.ui.pushButtonExit, QtCore.SIGNAL(_fromUtf8("clicked()")), self.confirmExit)
        
        #add signals/slots for the various popup dialog boxes
        QtCore.QObject.connect(self.ui.pushButtonMessage, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doMessage)
        QtCore.QObject.connect(self.ui.pushButtonQuestion, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doQuestion)
        QtCore.QObject.connect(self.ui.pushButtonGetDirectory, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doGetDirectory)
        QtCore.QObject.connect(self.ui.pushButtonGetFile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doGetFile)
        QtCore.QObject.connect(self.ui.pushButtonSaveFile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doSaveFile)        
        QtCore.QObject.connect(self.ui.pushButtonListSelect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doListSelect)        
        
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
            
            
    def doMessage(self):
        dialog=QtGui.QMessageBox(self)
        dialog.setText("This is a message dialog")
        dialog.exec_()  
        pass
        
    def doQuestion(self):

        answer=QtGui.QMessageBox.question(self,'Message','Yes/No Question dialog',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        print "Answer: ",answer, " QtGui.QMessageBox.Yes: ",QtGui.QMessageBox.Yes, " QtGui.QMessageBox.No: ",QtGui.QMessageBox.No
        if answer == QtGui.QMessageBox.Yes:
            #do something
            pass
        else:
            #do something else
            pass
        
    def doGetDirectory(self):
        home=getHomeDir()
        dirs = str(QtGui.QFileDialog.getExistingDirectory(self,'Get Directory',home))
        print "Directory: ",dirs
        pass
        
    def doGetFile(self):
        curdir=os.curdir
        filter="All files (*.*);;NXS (*.nxs);;NXSPE (*.nxspe)" 
        fileList = QtGui.QFileDialog.getOpenFileNames(self, 'Open File(s)', curdir,filter)
        print [str(file) for file in fileList]
        pass
        
    def doSaveFile(self):
        sfile = str(QtGui.QFileDialog.getSaveFileName(self, 'Save File', home,filter))
        print "Save File: ",sfile
        pass
            
    def doListSelect(self):
        wslst=['ws0','ws1','ws2']
        wsSel,ok = QtGui.QInputDialog.getItem(self,"Available Workspaces","Select from the list:",wslst)
        print "Selected Workspace: ",wsSel
        print "ok status: ",ok
        
def getHomeDir():
        if sys.platform == 'win32':
            home = os.path.expanduser("~")
        else:
            home=os.getenv("HOME")
        return home
    
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = PopupTemplateMain()
    myapp.show()

    exit_code=app.exec_()
    #print "exit code: ",exit_code
    sys.exit(exit_code)