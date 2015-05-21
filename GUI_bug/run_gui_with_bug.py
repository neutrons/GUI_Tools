from myGUI import Ui_MainWindow
from PyQt4 import QtGui, QtCore
import sys
import numpy as np

class MyApplication(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.initGui()
        
    def initGui(self):
        magIcon = QtGui.QPixmap('magnifier.png')
        self.ui.magnifierLabel.setPixmap(magIcon)
        clearIcon = QtGui.QIcon('clear.png')
        self.ui.clearButton.setIcon(clearIcon)
        sz = QtCore.QSize(15,15)
        self.ui.clearButton.setIconSize(sz)

    def lineEditFieldModified(self):
        print 'inside lineEditFieldModified'
        
    def clearButtonClicked(self):
        print 'just clicked clearButtonClicked'


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mplQt = MyApplication()
    mplQt.show()
    sys.exit(app.exec_())