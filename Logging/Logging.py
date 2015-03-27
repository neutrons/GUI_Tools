#!/usr/bin/python

"""
Logging.py

S. Miller  20Mar15

Example GUI to introduce utilizing logging for a main GUI application plus
including child apps it may create.

Disclaimer: this example strives to achieve demonstrating how to include
basic logging capabilities into GUI applications and does not attepmt to 
demonstrate all logging features.

Logging here utilizes a logging.conf file as the configuration of loggers,
handlers, and formatters can then be modified apart from the python code which
includes it.  In this way, logging configuration changes can be made without
affecting the python code which is servers.

Logging levels:
DEBUG     Detailed information, typically of interest only when diagnosing problems.
INFO      Confirmation that things are working as expected.
WARNING   An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
ERROR     Due to a more serious problem, the software has not been able to perform some function.
CRITICAL  A serious error, indicating that the program itself may be unable to continue running.

Example calls:
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

Introduction on logging can be found here:
https://docs.python.org/2/library/logging.html

Logging Tutorial here:
https://docs.python.org/2/howto/logging.html#logging-basic-tutorial

Logging cookbook:
https://docs.python.org/2/howto/logging-cookbook.html#logging-cookbook

Config file format:
https://docs.python.org/2/library/logging.config.html#logging-config-api

Advantages of using logging:
* should significantly reduce the need for using print statements within code
* logging levels can be controlled from the logging.conf file
* console and file loggers can be at different logging levels, may show more in the log files than on the console when using in production
* loggers are global in scope across the current interpreter session
* - reduces overhead in setting up logging within objects and across child apps
* - enables log info from different places to be consolidated 
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

#Initiate logging
import logging
import logging.config
from loggingHelpers import *

#setup for logging
try:
    #determine the logging directory from logging.conf
    baseFilename=parseLoggingConf()
    #then check if the logging directories are created and create them if not
    stat=checkLogDirs(baseFilename)   
except:
    #only get here if logging directory structure could not be established
    print "Failure here indicates that logging may not occur - please check"
#indicate the status for checking logging directory existance
if stat:
    print "Logging directories created"
else:
    print "Logging directories already in place"

#logging.conf defines how logging will operate - usually placed in app home dir
#logging will look in the current directory for the logging.conf file
#hard coded logging.conf name as this is the standard logging configuration file name
logging.config.fileConfig('logging.conf') 
#else the full path can be specified if you prefer and shown below for illustration
#logging.config.fileConfig('c:/Users/mid/Documents/PyQt/GUI_Tools/Logging/logging.conf')
#open the main logging instance using the module __name__ as the logger name
#this logger will typically use the root logger
Log=logging.getLogger(__name__)
#place some initial entries into the logging files so we can check if things are working
Log.critical("*************************************************************")
Log.critical("Main App - New Log Entry")
Log.critical("Effective Logging Level: "+str(Log.getEffectiveLevel()))
Log.critical("  Logging Levels:")
Log.critical("   0 - NOTSET")
Log.critical("  10 - DEBUG")
Log.critical("  20 - INFO")
Log.critical("  30 - WARNING")
Log.critical("  40 - ERROR")
Log.critical("  50 - CRITICAL")
Log.critical(" ")
#define all of the application specific loggers we'll use in the main application - enables for fine grain determination of where logging occurs
#suggest setting up the loggers before running the main application:
# - consolidates where to find the various loggers
# - taking advantage that loggers are global in scope across the interpreter session
LogDebug=logging.getLogger('MainApp_Debug')
LogInfo=logging.getLogger('MainApp_Info')
LogWarning=logging.getLogger('MainApp_Warning')
LogError=logging.getLogger('MainApp_Error')
LogCritical=logging.getLogger('MainApp_Critical')
LogException=logging.getLogger('MainApp_Exception')
LogLA=logging.getLogger('MainApp_LogAll')
LogLCA=logging.getLogger('MainApp_LCA')

#import GUI components generated from Qt Designer .ui file
from ui_Logging import *
#import object for the child application that can be created from the main app
import LoggingChild 

class LoggingMain(QtGui.QMainWindow):
    
    #initialize app
    def __init__(self, parent=None):
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow() #defined in ui_AppTemplate.py
        self.ui.setupUi(self)
        self.setWindowTitle("Logging GUI Example")

        #add action exit for File --> Exit menu option
        self.connect(self.ui.actionExit, QtCore.SIGNAL('triggered()'), self.confirmExit)
        #add signal/slot connection for pushbutton exit request
        self.connect(self.ui.pushButtonExit, QtCore.SIGNAL('released()'), self.confirmExit)
                        
        #define button callbacks
        self.connect(self.ui.pushButtonDebug, QtCore.SIGNAL('released()'), self.Debug)
        self.connect(self.ui.pushButtonInfo, QtCore.SIGNAL('released()'), self.Info)
        self.connect(self.ui.pushButtonWarning, QtCore.SIGNAL('released()'), self.Warning)
        self.connect(self.ui.pushButtonError, QtCore.SIGNAL('released()'), self.Error)
        self.connect(self.ui.pushButtonCritical, QtCore.SIGNAL('released()'), self.Critical)
        self.connect(self.ui.pushButtonException, QtCore.SIGNAL('released()'), self.Exception)
        self.connect(self.ui.pushButtonAll, QtCore.SIGNAL('released()'), self.LogAll)        
        self.connect(self.ui.pushButtonLaunchChildApp, QtCore.SIGNAL('released()'), self.LaunchChildApp)
        
        Log=logging.getLogger('MainApp_Init')
        Log.info("LoggingMain Initialized")
        
    #setup the callbacks for each button in the main application.
    #To illustrate how fine grained logging can be, each callback has been
    #given its own logger.
    def Debug(self):
        LogDebug.debug("Debug button pressed")
    def Info(self):
        LogInfo.info("Info button pressed")
        LogInfo.info(" Incorporating variables into the log: ")
        Astr = 'String Variable named Astr'
        LogInfo.info(" A string: %s",Astr)
        Aflt = 3.456
        LogInfo.info(" A floating point variable: %f",Aflt)
        LogInfo.info(" A floating point variable limited to two decimal places - with rounding: %.2f", Aflt)
        C=3.1415
        Alst = ['A',1234,C]
        LogInfo.info(" A list: %s",str(Alst))
        #Now limit floats to 2 decimal places in the list:
        LogInfo.info(" A list limiting floats to 2 decimal places: %s",str([a if type(a) is not float else float('%.2f' % a) for a in Alst]))
        self.ui.statusbar.showMessage("This message shows up in the statusbar")
        
    def Warning(self):
        LogWarning.warning("Warning button pressed")
    def Error(self):
        LogError.error("Error button pressed")
    def Critical(self):
        LogCritical.critical("Critical button pressed")
    def Exception(self):
        #logs can be used functionally rather than geographically if desired
        #here using the info log within the exception callback for instance 
        LogInfo.info("Exception button pressed") 
        try:
            #induce an exception - ZeroDivisionError
            A=3/0
        except:
            #Need to use the except clause in order to capture the exception 
            #and place its info into the log file.  Reason being that program
            #execution stops at the point of the exception and the log entry
            #call will not be made.
            LogException.exception("Encountered an exception: ")
    def LogAll(self):
        #log a number of things to build up the log file a bit faster to help
        #illustrate log file rollover
        LogLA.debug("LogAll button pressed")
        LogLA.info("info check")
        LogLA.debug("debug check")
        LogLA.warning("warning check")
        LogLA.error("error check")
        LogLA.critical("critical check")
        LogLA.exception("exception check - next line(s) in log give exception info")
    def LaunchChildApp(self):
        #launch a child app to illustrate how logging extends into child apps
        LogLCA.debug("LaunchChildApp button pressed")
        #instantiate the child app
        self.childApp = LoggingChild.LoggingChild(self)
        self.childApp.show()   
        
        
    def confirmExit(self):
        #case where user is asked to confirm exiting application
        reply = QtGui.QMessageBox.question(self, 'Message',
        "Are you sure to quit?", QtGui.QMessageBox.Yes | 
        QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        
        if reply == QtGui.QMessageBox.Yes:
            #close application
            Log.info("Closing Main Application")
            self.close()
        else:
            #do nothing and return
            pass     
            
    def closeEvent(self,event):
        #case where user hits 'X' on GUI to close it
        Log.info("Forced Closing of Main Application")
    
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    logapp = LoggingMain()
    logapp.show()

    exit_code=app.exec_()
    #print "exit code: ",exit_code
    sys.exit(exit_code)