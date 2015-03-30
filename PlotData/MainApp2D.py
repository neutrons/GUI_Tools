################################################################################
#
# This is an example to plot 2D data with matplotlib in pyqt
#
################################################################################
import os
import sys
import numpy as np

from PyQt4 import QtCore,  QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class QtMplCanvas2D(FigureCanvas):
    """ A class inherit from FigureCanvas for Qt4 and contains a matplotlib Figure
    """
    def __init__(self, parent=None, width = 6.5, height = 5.5, dpi = 100, sharex = None, sharey = None, fig = None):
        """ Init
        """
        if fig == None:
            # Create a Figure instance
            self.fig = Figure(figsize = (width, height), dpi=dpi, facecolor = '#FFFFFF')
            # Add one axis
            self.ax = self.fig.add_subplot(111)
            self.fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)
            self.colorbar = None
        else:
            # Use an existing figure 
            self.fig = fig

        # Initialize
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        return

    def sizeHint(self):
        w, h = self.get_width_height()
        return QtCore.QSize(w, h)

    def minimumSizeHint(self):
        return QtCore.QSize(10, 10)


    def clearCanvas(self):
        """ Clear data from canvas
        """
        # clear the image for next operation
        self.ax.hold(False)

        # clear image
        self.ax.cla()

        # flush/commit
        self._flush()
        # plt.draw() # this is not useful at all!

        return


    def plot2D(self, array2d, xmin, xmax, ymin, ymax):
        """ Plot a 2D image
        """
        # Release the current image
        self.ax.hold(False)

        # Do plot
        imgplot = self.ax.imshow(array2d, extent=[xmin,xmax,ymin,ymax])

        # Set color bar.  plt.colorbar() does not work!
        if self.colorbar is None:
            # set color map type
            imgplot.set_cmap('spectral')
            self.colorbar = self.fig.colorbar(imgplot)
        else:
            self.colorbar.update_bruteforce(imgplot)

        # Flush...
        self._flush() 

        return


    def _flush(self):
        """ A dirty hack to flush the image
        """
        w, h = self.get_width_height()
        if True:
            self.resize(w+1,h)
            self.resize(w,h)
        else:
            # not useful
            plt.draw()


class MyNavigationToolbar(NavigationToolbar):
    """ A customized navigation tool bar attached to canvas
    """
    def __init__(self, parent, canvas, direction='h'):
        """ Initialization
        """
        self.canvas = canvas
        QtGui.QWidget.__init__(self, parent)

        if direction=='h' :
            self.layout = QtGui.QHBoxLayout(self)
        else :
            self.layout = QtGui.QVBoxLayout(self)

        self.layout.setMargin(2)
        self.layout.setSpacing(0)

        NavigationToolbar.__init__( self, canvas, canvas )

        return


    def set_message( self, s ):
        pass


class Template2DMainWindow(QtGui.QWidget):
    """ Main window class to hold everything
    """
    def __init__(self, parent = None, enableAutoScale = False, enableCSV = False, enableEdit = False, fig = None):
        """ Initailization
        """
        # base class init
        QtGui.QWidget.__init__(self, parent)

        # set up GUI
        # -functionaly widgets
        self.canvas = QtMplCanvas2D(fig)
        self.toolbar = MyNavigationToolbar(self.canvas, self.canvas)
        self.buttonPlot = QtGui.QPushButton(self)
        self.buttonPlot.setText('Plot Image')
        self.lineEdit_Function = QtGui.QLineEdit(self)
        self.buttonClear = QtGui.QPushButton(self)
        self.buttonClear.setText('Clear Image')

        # - layout
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.canvas)
        self.vbox.addWidget(self.toolbar)
        self.vbox.addWidget(self.buttonPlot)
        self.vbox.addWidget(self.lineEdit_Function)
        self.vbox.addWidget(self.buttonClear)
        self.setLayout(self.vbox)

        # event handling
        self.connect(self.buttonPlot, QtCore.SIGNAL('clicked()'), self.doChangeFigure)
        self.connect(self.buttonClear, QtCore.SIGNAL('clicked()'), self.doClearFigure)

        # matplotlib canvas event handling
        self.canvas.canvas.mpl_connect('button_press_event', self.on_mouseDownEvent)
        self.canvas.canvas.mpl_connect('motion_notify_event', self.on_mouseMotion)



        ###########SAVING FIGURE TO CLIPBOARD##########
        self.cb = None #will be used for the clipboard
        self.tempPath = getHomeDir()
        self.tempPath = os.path.join(self.tempPath,'tempMPL.png')

        self.mpl2ClipAction = QtGui.QAction("Save to Clipboard",  self)
        self.mpl2ClipAction.setShortcut("Ctrl+C")
        self.addAction(self.mpl2ClipAction)
        QtCore.QObject.connect(self.mpl2ClipAction,QtCore.SIGNAL("triggered()"), self.mpl2Clip)

        # Plot something
        self._plotInit()

        return

    def _plotInit(self):
        """ Do some initial plot for future modification
        """
        # Array
        dim2array = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])

        print dim2array

        self.canvas.plot2D(dim2array, xmin=0, xmax=5,ymin=0,ymax=2)

        return

    #--------------------------------------------------------------------------


    def doClearFigure(self):
        """ Clear figure
        """
        self.canvas.clearCanvas()

        return

    def doChangeFigure(self):
        """ Test to change figure to 1D
        """
        import time

        dim2array = np.array([[1000, 40, 100], [500, 400, 200]])
        print "Change figure to: ", dim2array

        self.canvas.plot2D(dim2array, xmin=0, xmax=5, ymin=0,ymax=2)

        # # Clear figure
        # import matplotlib.pyplot as plt
        # self.canvas.ax.cla() #: not useful
        # #plt.hold(True)
        # #plt.clf()

        # # self.canvas.fig.remove()

        # # plt.draw()

        # # self.canvas.ax = self.fig.add_subplot(111)     
        # self.canvas.ax.imshow(dim2array, extent=[1,2,1,2])
        # plt.draw()

        # r = self.size() 
        # w = r.width()
        # h = r.height()
        # self.resize(w+1, h+1)
        # self.resize(w, h)

        return

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


    def on_mouseDownEvent(self, event):
        """ Respond to pick up a value with mouse down event
        """
        x = event.xdata
        y = event.ydata

        if x is not None and y is not None:
            msg = "You've clicked on a bar with coords:\n %f, %f" % (x, y)
            QtGui.QMessageBox.information(self, "Click!", msg)

        return

    def on_mouseMotion(self, event):
        """
        """
        print "Mouse is moving to ", event.xdata, event.ydata





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
    mplQt = Template2DMainWindow()
    mplQt.show()
    sys.exit(app.exec_())
