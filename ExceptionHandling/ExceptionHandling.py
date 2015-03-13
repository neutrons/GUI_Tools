#!/usr/bin/python
"""
ExceptionHandling.py

Python exception handling example applied to PyQt development.
This example illustrates how to bullet proof (well, almost...) your GUI so 
that issues that arise when running the code can be handled without crashing
or compromising the application.  

This simple example enables the user to input values and select an operator to
perform on those values.  As initial checks are not performed on the values and
operator selection, the user can induce various types of exceptions which are
handled below.  Some illustrative exceptions handled here:

* ValueError occurs if user does not give numbers for A and B
* UserError occurs if the user does not select an operator
* ZeroDivisionError occurs if B set to zero and division selected

A complete list of possible exception types can be found here:
https://docs.python.org/3/library/exceptions.html 

S. Miller 13Mar15


"""

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
from ui_ExceptionHandling import *

class AppTemplateMain(QtGui.QMainWindow):
    
    #initialize app
    def __init__(self, parent=None):
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow() #defined in ui_AppTemplate.py
        self.ui.setupUi(self)
        self.setWindowTitle("Exception Handling Example")
                
        #add signal/slot for Calculate Button
        self.connect(self.ui.pushButtonCalc, QtCore.SIGNAL('clicked()'), self.calc)
        #initialize a counter for how many calculations we do
        self.ui.trys=0 
        self.ui.successful=0
        self.ui.result=0 #placeholder for results
    
        #add action exit for File --> Exit menu option
        self.connect(self.ui.actionExit, QtCore.SIGNAL('triggered()'), self.confirmExit)
        #add signal/slot connection for pushbutton exit request
        self.connect(self.ui.pushButtonExit, QtCore.SIGNAL('clicked()'), self.confirmExit)
        
    def calc(self):
        
        #now let's "try" to do something with these parameters
        try:
            self.ui.trys += 1 #increment trys counter
            self.ui.textEditOutLog.append('************************')
            #get values from GUI
            self.ui.textEditOutLog.append('Getting values from Gui')
            A = self.ui.lineEditA.text()
            B = self.ui.lineEditB.text()    
            OpIndex=self.ui.comboBoxOperator.currentIndex()
        

            self.ui.textEditOutLog.append('Initiating Try Block')
            self.ui.textEditOutLog.append('  - converting values to float()')
            A=float(A)
            B=float(B)
            self.ui.textEditOutLog.append('  - checking operator selection')
            if OpIndex == 0:
                self.ui.textEditOutLog.append('  - Please select an operator')
                #throw our own exception if no operator selected
                #exceptions thrown here will be handled in the same except block as which this try is associated
                raise Exception('UserError','Need a better user') 
            elif OpIndex == 1:
                self.ui.result=A+B
            elif OpIndex == 2:
                self.ui.result=A-B
            elif OpIndex == 3:
                self.ui.result=A*B
            elif OpIndex == 4:
                self.ui.result=A/B
            else:
                self.ui.textEditOutLog.append('  - Invalid Operator: try selecting again')
            self.ui.textEditOutLog.append('  - OpIndex: '+str(OpIndex))
            self.ui.textEditOutLog.append('  - completed try block')
            
        except Exception as e:
            
            self.ui.textEditOutLog.append('** Received an exception!')
            #exception types found here: https://docs.python.org/3/library/exceptions.html 
            #parse error messages and provide info to user
            #typical etypes include: ValueError, SyntaxError, NameError, TypeError, ZeroDivisionError, etc.
            #can set specific exceptions for each - example: 
            #except ValueError:
            #However here we're handling exceptions ourselves
            
            #get the exception type:
            etype=e.__class__.__name__
            #get the message that came along with the exception"
            emsg=e.args[0] 
            
            #add my additional messages
            mymsg='  '
            if etype == 'ZeroDivisionError':
                mymsg="B cannot be zero for division"
            
            if 'could not convert string to float' in emsg:
                mymsg="Must enter numbers for A and B"
                
            if e.args[0] == 'UserError':
                mymsg=e.args[1]
            
            msg="Exception type: "+etype+"  Message: "+emsg+"  Info: "+mymsg
            
            #put exception message in a dialog to the user
            dialog=QtGui.QMessageBox(self)
            dialog.setText(msg)
            dialog.exec_()
            
            #clear A and B
            self.ui.lineEditA.setText('')
            self.ui.lineEditB.setText('')
            
        else:
            #This else clause executes if the corresponding try block executes correctly
            #Important note: any exceptions that occur in this else clause are NOT handled by the except clause for the corresponding try!
            #Thus separate try/except blocks would need to be incorporated within this else block as appropriate.
            self.ui.textEditOutLog.append('  - running try - else code')
            #Increment success counter
            self.ui.successful += 1 #increment success counter if we get here
            #update Result
            self.ui.labelResult.setText("Result: "+str(self.ui.result))
            
        finally:
            #This code to execute if either the try or except blocks execute
            #Note may not get here if an unhandled exception occurs in either the except or else blocks
            #Again, utilize try/except blocks within the finally block as appropriate.
            
            #log that we've been succssful
            self.ui.textEditOutLog.append('Executing finally code')
            #log try/success results to display:
            self.ui.textEditOutLog.append('Number of Attempts: '+str(self.ui.trys))
            self.ui.textEditOutLog.append('Number of Successes: '+str(self.ui.successful))
        
        
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