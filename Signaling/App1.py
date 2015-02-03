#!/usr/bin/python
#
#app1.py (appone.py)
#
#Main program app1 enables a user to transfer text from a line edit widget to a
#text edit widget.  
#app2 can be launched from app1 where the user can enter text on app2 then have
#it transferred to the app1 text edit box.
#subsequent apps can be launched following app2 and app1 numbers and keeps track
#of each of them independently.

#import utility modules
import sys

#import PyQt modules
from PyQt4 import QtGui, QtCore, Qt

#include this try/except block to remap QString needed when using IPython
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

import config

#import app1 GUI components generated from Qt Designer .ui file
from ui_App1 import *
#import class for app2 to be instantiated
from App2 import *

class App1(QtGui.QMainWindow):
    #initialize app
    def __init__(self, parent=None):
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_mainWindow() #defined in ui_AppTemplate.py
        self.ui.setupUi(self)
    
        #add action exit for File --> Exit menu option
        self.connect(self.ui.actionExit, QtCore.SIGNAL('triggered()'), self.confirmExit)
        #add signal/slot connection for pushbutton exit request
        self.connect(self.ui.pushButtonLaunchApp2, QtCore.SIGNAL('clicked()'), self.launchApp2)
        self.connect(self.ui.pushButtonUpdate, QtCore.SIGNAL('clicked()'), self.updateLocal)        
        
        self.ui.text=self.ui.lineEditEnterText.text()  #initiate placeholder for text to be passed between applications
        self.ui.appCntr=config.app1val  #app2 to N counter

        
    def launchApp2(self):
        #method to enable launching of app2 and following applications
        self.ui.appCntr+=1
        self.ui.pushButtonLaunchApp2.setText(_fromUtf8("Launch App "+str(self.ui.appCntr+1)))
        self.App2_obj = App2(self)  #instantiate app2
        self.App2_obj.show()        #now make it visible

        
    def updateLocal(self):
        #update text in app1 line edit to text edit fields (staying all within app1)
        self.ui.text=self.ui.lineEditEnterText.text()
        self.updateTextEdit(config.app1val)

    #add slot for App2 signal to connect to
    @QtCore.pyqtSlot(int)    
    def updateTextEdit(self,val):
        #signal capable of passing an integer value back
        prepend="App"+str(val)+": " #create an app identifier based upon the returned integer
        self.ui.textEditDisplayText.append(prepend+self.ui.text) #update app1 text edit box

        
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

    def closeEvent(self, event=None):
        # always executed when leaving application
        print "whatever you do to me here... I am going to quit anyway!"

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = App1()
    myapp.show()

    exit_code=app.exec_()
    #print "exit code: ",exit_code
    sys.exit(exit_code)