#!/usr/bin/python

"""
LoggingChild.py

This application instantiated via the Logging.py main application.  The intent 
here is to illustrate how lean and straightforward it is to extend logging into
child applications by taking advantage of the global scope of logging within
the python interpreter session.  


"""

#import utility modules
import sys, os

#import PyQt modules
from PyQt4 import QtGui, QtCore, Qt

#include this try/except block to remap QString needed when using IPython
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


#import GUI components generated from Qt Designer .ui file
from ui_LoggingChild import *

#Though logging is global in scope, it is still necessary to import the 
#logging modules to make the connections.
import logging
import logging.config

#as logging is global to the interpreter, logging here finds 'ChildApp' as 
#defined via the logging.conf file loaded in the main application - magic!
Log=logging.getLogger('ChildApp')
#Notice in this case that only one logger is used for the child application
#though the developer can embed geographic information into the log message
#if so desired.
#Put initial entries in logs for the child app
Log.critical("*************************************************************")
Log.critical("Child App - New Log Entry")
Log.critical("Effective Logging Level: "+str(Log.getEffectiveLevel()))

class LoggingChild(QtGui.QMainWindow):
    
    #initialize app
    def __init__(self, parent=None):
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow() #defined in ui_AppTemplate.py
        self.ui.setupUi(self)
        self.setWindowTitle("Logging Child")

        #add action exit for File --> Exit menu option
        self.connect(self.ui.actionExit, QtCore.SIGNAL('triggered()'), self.confirmExit)
        #add signal/slot connection for pushbutton exit request
        self.connect(self.ui.pushButtonExit, QtCore.SIGNAL('released()'), self.confirmExit)
        
        Log=logging.getLogger('MainApp_Init')
        Log.info("LoggingMain Initialized")
                
        #define button callbacks
        self.connect(self.ui.pushButtonDebug, QtCore.SIGNAL('released()'), self.Debug)
        self.connect(self.ui.pushButtonInfo, QtCore.SIGNAL('released()'), self.Info)
        self.connect(self.ui.pushButtonWarning, QtCore.SIGNAL('released()'), self.Warning)
        self.connect(self.ui.pushButtonError, QtCore.SIGNAL('released()'), self.Error)
        self.connect(self.ui.pushButtonCritical, QtCore.SIGNAL('released()'), self.Critical)
        self.connect(self.ui.pushButtonException, QtCore.SIGNAL('released()'), self.Exception)
        self.connect(self.ui.pushButtonAll, QtCore.SIGNAL('released()'), self.LogAll)        
        
    #define callbacks for the child app buttons
    def Debug(self):
        Log.debug("Debug button pressed")
    def Info(self):
        Log.info("Info button pressed")
    def Warning(self):
        Log.warning("Warning button pressed")
    def Error(self):
        Log.error("Error button pressed")
    def Critical(self):
        Log.critical("Critical button pressed")
    def Exception(self):
        Log.info("Exception button pressed") #show that you can use different logs whereever 
        try:
            #induce an exception - ZeroDivisionError
            A=2/0
        except:
            #Need to use the except clause in order to capture the exception 
            #and place its info into the log file.  Reason being that program
            #execution stops at the point of the exception and the log entry
            #call will not be made.
            Log.exception("Encountered an exception: ")
    def LogAll(self):
        Log.debug("LogAll button pressed")
        Log.info("info check")
        Log.debug("debug check")
        Log.warning("warning check")
        Log.error("error check")
        Log.critical("critical check")
        Log.exception("exception check - next line(s) in log give exception info")

        
        
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
    
