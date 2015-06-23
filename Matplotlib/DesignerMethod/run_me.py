from myGUI import Ui_MainWindow
from PyQt4 import QtGui
import sys
import numpy as np

class MyApplication(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.myPlot.singleClick.connect(self.single_click)
        self.ui.myPlot.toolbar.homeClicked.connect(self.home_click)
        
        self.plotData()
        
    def plotData(self):
        self.ui.myPlot.imshow(np.random.rand(42,42))
        
    def single_click(self):
        print 'single click'
        
    def home_click(self):
        print 'home click'

    def spinBoxValueChanged(self, value):
        print 'value is %d' %value


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mplQt = MyApplication()
    mplQt.show()
    sys.exit(app.exec_())