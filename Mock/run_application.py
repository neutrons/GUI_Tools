from interface_example import Ui_MainWindow
from PyQt4 import QtGui, QtCore
import sys
import numpy as np
from transformtoptext import TransformTopText
from exporttext import ExportText

class MyApplication(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    def moveTopTextToBottomButton(self):
        newText = TransformTopText(self)
        
    def exportBottomTextButton(self):
        exportText = ExportText(self)
        exportText.getFilename()
        exportText.exportToFile()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mplQt = MyApplication()
    mplQt.show()
    sys.exit(app.exec_())