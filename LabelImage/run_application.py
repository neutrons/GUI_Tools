from interface_example import Ui_MainWindow
from PyQt4 import QtGui, QtCore
import sys


class MyApplication(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        image = 'check_icon.png'
        pixmap = QtGui.QPixmap(image)
        self.ui.label.setFixedWidth(25)
        self.ui.label.setFixedHeight(25)
        self.ui.label.setPixmap(pixmap)
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mplQt = MyApplication()
    mplQt.show()
    sys.exit(app.exec_())