from MainWindow import Ui_MainWindow

from PyQt4 import QtGui
import sys
import numpy as np

class MyApplication(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mplQt = MyApplication()
    mplQt.show()
    sys.exit(app.exec_())