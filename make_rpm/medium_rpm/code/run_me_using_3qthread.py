import sys
import os
import time
from PyQt4 import QtGui, QtCore, Qt

from code.thread.thread_class_method1 import AThread
from code.main_window_interface import Ui_MainWindow


#include this try/except block to remap QString needed when using IPython
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
class ThreadApplication(QtGui.QMainWindow):

    thread = None
    thread1_paused_flag = False

    #initialize app
    def __init__(self, parent=None):
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.setWindowTitle("Using QThread method")

        self.thread1 = AThread()
        self.thread2 = AThread()
        self.thread3 = AThread()

        self.thread1.finished.connect(self.threadMethodDone1)
        self.thread2.finished.connect(self.threadMethodDone2)
        self.thread3.finished.connect(self.threadMethodDone3)
        
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.noThread)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.threadMethod1)
        QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.threadMethod2)
        QtCore.QObject.connect(self.ui.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.threadMethod3)
        QtCore.QObject.connect(self.ui.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.stopThreadMethod1)
        QtCore.QObject.connect(self.ui.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pauseThreadMethod1)

        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.displayMessageInBox)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clearTextEdit)  

    def displayMessageInBox(self):
        self.ui.textEdit.append("Printing message here")
    
    def threadMethod1(self):
        self.ui.textEdit.append("== Thread method 1 ==")
        self.thread1.setUpGui(self, 1)
        self.thread1.start()
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_7.setEnabled(True)
        self.ui.pushButton_8.setEnabled(True)

    def threadMethod2(self):
        self.ui.textEdit.append("== Thread method 2 ==")
        self.thread2.setUpGui(self, 2)
        self.thread2.start()

    def threadMethod3(self):
        self.ui.textEdit.append("== Thread method 3 ==")
        self.thread3.setUpGui(self, 3)
        self.thread3.start()

    def stopThreadMethod1(self):
        self.thread1.stop()
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_8.setEnabled(False)
        
    def pauseThreadMethod1(self):
        if self.thread1_paused_flag:
            self.ui.pushButton_8.setText("Pause Thread1")
            self.thread1_paused_flag = False
        else:
            self.ui.pushButton_8.setText("Resume Thread1")
            self.thread1_paused_flag = True
        self.thread1.pause()

    def threadMethodDone1(self):
        self.ui.textEdit.append("done with thread method 1!")

    def threadMethodDone2(self):
        self.ui.textEdit.append("done with thread method 2!")

    def threadMethodDone3(self):
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
    
if __name__=="__main__":

    app = QtGui.QApplication(sys.argv)
    myapp = ThreadApplication()
    myapp.show()
    sys.exit(app.exec_())