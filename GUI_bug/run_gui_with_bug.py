from guiWithBug import Ui_Dialog
from PyQt4 import QtGui, QtCore
import sys
import numpy as np

class MyApplication(QtGui.QDialog):
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
#        self.initGui()
        
    def initGui(self):
        magIcon = QtGui.QPixmap('magnifier.png')
        self.ui.magnifierLabel.setPixmap(magIcon)
        clearIcon = QtGui.QIcon('clear.png')
        self.ui.clearButton.setIcon(clearIcon)
        sz = QtCore.QSize(15,15)
        self.ui.clearButton.setIconSize(sz)

    def unselectAll(self):
        print 'in unselectAll'
        
    def userChangedTab(self):
        print 'in unserChangedTab'
        
    def searchLineEditLive(self):
        print 'in searchLineEditLive'
        
    def saveMetadataListAsAsciiFile(self):
        print 'in saveMetadataListAsAsciiFile'
        
    def runNumberEditEvent(self):
        print 'in runNumberEditEvent'
        
    def importConfiguration(self):
        print 'in importConfiguration'
        
    def exportConfiguration(self):
        print 'in exportConfiguration'
        
    def searchLineEditClear(self):
        print 'in searchLineEditClear'

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mplQt = MyApplication()
    mplQt.show()
    sys.exit(app.exec_())