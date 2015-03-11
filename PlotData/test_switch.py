import os
import sys

from PyQt4 import QtCore,  QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

class QtMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width = 6.5, height = 5.5, dpi = 100, sharex = None, sharey = None, fig = None):
        if fig == None:
            self.fig = Figure(figsize = (width, height), dpi=dpi, facecolor = '#FFFFFF')
            # Add one axis
            self.ax = self.fig.add_subplot(111)
            #self.fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)
            self.ax.hold(True)
        else:
            self.fig = fig

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        dim2array = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])

        print dim2array

        r = self.ax.imshow(dim2array, extent=[1,2,3,3.8])
        print str(type(r))


    def sizeHint(self):
        w, h = self.get_width_height()
        return QtCore.QSize(w, h)

    def minimumSizeHint(self):
        return QtCore.QSize(10, 10)

    def sizeHint(self):
        w, h = self.get_width_height()
        return QtCore.QSize(w, h)

    def minimumSizeHint(self):
        return QtCore.QSize(10, 10)


class MyNavigationToolbar(NavigationToolbar) :
    def __init__(self, parent, canvas, direction = 'h' ) :

        self.canvas = canvas
        QtGui.QWidget.__init__( self, parent )

        if direction=='h' :
            self.layout = QtGui.QHBoxLayout( self )
        else :
            self.layout = QtGui.QVBoxLayout( self )

        self.layout.setMargin( 2 )
        self.layout.setSpacing( 0 )

        NavigationToolbar.__init__( self, canvas, canvas )


    def set_message( self, s ):
        pass


class MPL_WIDGET_2D(QtGui.QWidget):
    def __init__(self, parent = None, enableAutoScale = False, enableCSV = False, enableEdit = False, fig = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = QtMplCanvas(fig)
        #self.canvas.ax.mouse_init()
        self.toolbar = MyNavigationToolbar(self.canvas, self.canvas)
        self.button = QtGui.QPushButton(self)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.canvas)
        self.vbox.addWidget(self.toolbar)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)


        ###########SAVING FIGURE TO CLIPBOARD##########
        self.cb = None #will be used for the clipboard
        self.tempPath = getHomeDir()
        self.tempPath = os.path.join(self.tempPath,'tempMPL.png')

        self.mpl2ClipAction = QtGui.QAction("Save to Clipboard",  self)
        self.mpl2ClipAction.setShortcut("Ctrl+C")
        self.addAction(self.mpl2ClipAction)
        QtCore.QObject.connect(self.mpl2ClipAction,QtCore.SIGNAL("triggered()"), self.mpl2Clip)

        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.changeFigure)

    def mpl2Clip(self):
        try:
            self.canvas.fig.savefig(self.tempPath)
            tempImg = QtGui.QImage(self.tempPath)
            self.cb = QtGui.QApplication.clipboard()
            self.cb.setImage(tempImg)
        except:
            print 'Error copying figure to clipboard'
            errorMsg = "Sorry: %s\n\n:%s\n"%(sys.exc_type, sys.exc_value)
            print errorMsg


    def changeFigure(self):
        """ Test to change figure to 1D
        """
        import time
        print "change figure"

        dim2array = np.array([[30, 40, 1, 2, 3], [30, 40, 10, 5, 1]])

        print dim2array

        # Clear figure
        import matplotlib.pyplot as plt
        self.canvas.ax.cla() #: not useful
        #plt.hold(True)
        #plt.clf()

        # self.canvas.fig.remove()

        # plt.draw()

        # self.canvas.ax = self.fig.add_subplot(111)     
        self.canvas.ax.imshow(dim2array, extent=[1,2,1,2])
        plt.draw()

        r = self.size() 
        w = r.width()
        h = r.height()
        self.resize(w+1, h+1)
        self.resize(w, h)

        return


####USED TO GET THE USERS HOME DIRECTORY FOR USE OF A TEMP FILE

def valid(path):
    if path and os.path.isdir(path):
        return True
    return False

def env(name):
    return os.environ.get( name, '' )

def getHomeDir():
    if sys.platform != 'win32':
        return os.path.expanduser( '~' )

    homeDir = env( 'USERPROFILE' )
    if not valid(homeDir):
        homeDir = env( 'HOME' )
        if not valid(homeDir) :
            homeDir = '%s%s' % (env('HOMEDRIVE'),env('HOMEPATH'))
            if not valid(homeDir) :
                homeDir = env( 'SYSTEMDRIVE' )
                if homeDir and (not homeDir.endswith('\\')) :
                    homeDir += '\\'
                if not valid(homeDir) :
                    homeDir = 'C:\\'
    return homeDir


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mplQt = MPL_WIDGET_2D()
    mplQt.show()
    sys.exit(app.exec_())
