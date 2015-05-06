import sys
from PyQt4 import QtGui, QtCore, Qt

from main_window_interface import Ui_MainWindow

class ThreadApplication(QtGui.QMainWindow):

    #initialize app
    def __init__(self, parent=None):
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
    
    def exit(self):
        print 'in exit'

    def closeEvent(self, event=None):
        # triggered when user exit application using top corner button (exit button)
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes | 
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    
        if reply == QtGui.QMessageBox.Yes:
        #close application
            event.accept()
        else:
        #do nothing and return
            event.ignore()

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = ThreadApplication()
    myapp.show()

    exit_code=app.exec_()
    sys.exit(exit_code)