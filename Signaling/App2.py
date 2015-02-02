#!/usr/bin/python
#
#app2.py
#
#Application called from app1.  This app enables text entered into it to be passed
#back to app1 for display.  This app also passes back its identifying number as 
#part of the signal response to the slot defined in app1.

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

#import GUI components generated from Qt Designer .ui file
from ui_App2 import *
        
class App2(QtGui.QMainWindow):
    
    mySignal = QtCore.pyqtSignal(int)  #establish signal for communicating from App2 to App1 - must be defined before the constructor
    #initialize app
    def __init__(self, parent=None):

        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_App2() #defined in ui_AppTemplate.py
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.appCnt=self.parent.ui.appCntr #set the integer corresponding to the instance number of this app
        self.setWindowTitle(_fromUtf8("App"+str(self.ui.appCnt)))
        
        #add action exit for File --> Exit menu option
        self.connect(self.ui.actionExit, QtCore.SIGNAL('triggered()'), self.confirmExit)
        #add signal/slot connection for pushbutton exit request
        self.connect(self.ui.pushButtonSignalApp1, QtCore.SIGNAL('clicked()'), self.signalApp1)        
        
        self.mySignal.connect(parent.updateTextEdit) #connect to the updateTextEdit slot defined in app1.py
        

    def signalApp1(self):
        self.parent.ui.text=self.ui.lineEditApp2.text() #place text from this app into the text field used by app1 to update the app1 text edit box
        sigVal=self.ui.appCnt    #reply with the integer representing this application instance
        self.mySignal.emit(sigVal)  #send sigval to inform main program which app responded

        
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

    def closeEvent(self,event):
        self.parent.ui.text=_fromUtf8("Closing App: "+str(self.ui.appCnt)) #place text from this app into the text field used by app1 to update the app1 text edit box
        sigVal=self.ui.appCnt    #reply with the integer representing this application instance
        self.mySignal.emit(sigVal)  #send sigval to inform main program which app responded
        

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    app2 = App2()
    app2.show()

    exit_code=app.exec_()
    #print "exit code: ",exit_code
    sys.exit(exit_code)