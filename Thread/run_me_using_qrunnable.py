import sys
import time
from PyQt4 import QtGui, QtCore, Qt
from runnable import Runnable

from main_window_interface import Ui_MainWindow

#include this try/except block to remap QString needed when using IPython
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
class ThreadApplication(QtGui.QMainWindow):

    obj = None
    objThread = None

    #initialize app
    def __init__(self, objThread, parent=None):
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.setWindowTitle("Using moveToThread")
        self.objThread = objThread

        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.noThread)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.threadMethod)
        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.displayMessageInBox)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clearTextEdit)  

    def displayMessageInBox(self):
        self.ui.textEdit.append("Printing message here")
    
    def threadMethod(self):
        self.ui.textEdit.append("== Thread method 3 ==")
        runnable = Runnable()
        runnable.setUpGui(self)
        QtCore.QThreadPool.globalInstance().start(runnable)

    def threadMethodDone(self):
        self.ui.textEdit.append("done with thread method 3!")

    def noThread(self):
        self.ui.textEdit.append("Starting No Thread")
        QtGui.QApplication.processEvents()
        for i in range(5):
            time.sleep(2)
            self.ui.textEdit.append("-> index loop %d" %i)
            QtGui.QApplication.processEvents()
        self.ui.textEdit.append("done with noThread method")
            
    def clearTextEdit(self):
        self.ui.textEdit.clear()
    
    #def closeEvent(self, event=None):
        ## triggered when user exit application using top corner button (exit button)
        #reply = QtGui.QMessageBox.question(self, 'Message',
                                           #"Are you sure to quit?", QtGui.QMessageBox.Yes | 
                                           #QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    
        #if reply == QtGui.QMessageBox.Yes:
        ##close application
            #event.accept()
        #else:
        ##do nothing and return
            #event.ignore()

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    objThread = QtCore.QThread()
    myapp = ThreadApplication(objThread)
    myapp.show()
    sys.exit(app.exec_())