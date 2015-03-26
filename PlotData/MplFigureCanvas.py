#pylint: disable=invalid-name
import sys
import os

from PyQt4 import QtGui, QtCore

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

MplLineStyles = ['-' , '--' , '-.' , ':' , 'None' , ' ' , '']
MplLineMarkers = [
        "o (circle        )",
        "s (square        )",
        "D (diamond       )",
        ", (pixel         )",
        ". (point         )",
        "v (triangle_down )",
        "^ (triangle_up   )",
        "< (triangle_left )",
        "> (triangle_right)",
        "1 (tri_down      )",
        "2 (tri_up        )",
        "3 (tri_left      )",
        "4 (tri_right     )",
        "8 (octagon       )",
        "p (pentagon      )",
        "* (star          )",
        "h (hexagon1      )",
        "H (hexagon2      )",
        "+ (plus          )",
        "x (x             )",
        "d (thin_diamond  )",
        "| (vline         )",
        "_ (hline         )",
        "None (nothing    )"]

MplBasicColors = [
        "black",
        "red",
        "blue",
        "green",
        "cyan",
        "magenta",
        "yellow",
        "white"]
        
        
class Qt4MplPlotView(QtGui.QWidget):
    """ A combined graphics view including matplotlib canvas and 
    a navigation tool bar
    """
    def __init__(self, parent):
        """ Initialization
        """
        # instantianize parent
        QtGui.QWidget.__init__(self, parent)
        
        # set up canvas
        self.canvas = Qt4MplCanvas(self)
        self.toolbar = MyNavigationToolbar(self.canvas, self.canvas)
        
        # set up layout
        self.vbox = QtGui.QVBoxLayout(self)
        self.vbox.addWidget(self.canvas)
        self.vbox.addWidget(self.toolbar)
        
        return
        
    def addPlot(self, x, y, color=None, label="", xlabel=None, ylabel=None, marker=None, linestyle=None, linewidth=1):
        """ Add a new plot
        """
        self.canvas.addPlot(x, y, color, label, xlabel, ylabel, marker, linestyle, linewidth)
        
        return


    def addPlot2D(self, array2d, xmin, xmax, ymin, ymax, holdprev=True):
        """ Plot a 2D image
        Arguments
         - array2d :: numpy 2D array
        """
        self.canvas.addPlot2D(array2d, xmin, xmax, ymin, ymax, holdprev)

        return


    def addImage(self, imagefilename):
        """ Add an image by file
        """
        # check
        if os.path.exists(imagefilename) is False:
            raise NotImplementedError("Image file %s does not exist." % (imagefilename))

        self.canvas.addImage(imagefilename)

        return


    def clearAllLines(self):
        """
        """
        self.canvas.clearAllLines()

    def clearCanvas(self):
        """ Clear canvas
        """
        return self.canvas.clearCanvas()
        
    def draw(self):
        """ Draw to commit the change
        """
        return self.canvas.draw()

    def getPlot(self):
        """
        """
        return self.canvas.getPlot()
        
    def getLastPlotIndexKey(self):
        """ Get ...
        """
        return self.canvas.getLastPlotIndexKey()
        
    def removePlot(self, ikey):
        """
        """
        return self.canvas.removePlot(ikey)

    def setXYLimits(self, xmin=None, xmax=None, ymin=None, ymax=None):
        """ 
        """
        return self.canvas.setXYLimit(xmin, xmax, ymin, ymax)

        
    def updateLine(self, ikey, vecx, vecy, linestyle=None, linecolor=None, marker=None, markercolor=None):
        """
        """
        return self.canvas.updateLine(ikey, vecx, vecy, linestyle, linecolor, marker, markercolor)


    def getLineStyleList(self):
        """
        """
        return MplLineStyles


    def getLineMarkerList(self):
        """
        """
        return MplLineMarkers

    def getLineBasicColorList(self):
        """
        """
        return MplBasicColors 
        
    def getDefaultColorMarkerComboList(self):
        """ Get a list of line/marker color and marker style combination 
        as default to add more and more line to plot
        """
        return self.canvas.getDefaultColorMarkerComboList()


class Qt4MplCanvas(FigureCanvas):
    """  A customized Qt widget for matplotlib figure.
    It can be used to replace GraphicsView of QtGui
    """
    def __init__(self, parent):
        """  Initialization
        """
        # Instantialize matplotlib Figure
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111) # return: matplotlib.axes.AxesSubplot

        # Initialize parent class and set parent
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        # Set size policy to be able to expanding and resizable with frame
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding,\
                QtGui.QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)

        # Variables to manage all lines/subplot
        self._lineDict = {}
        self._lineIndex = 0

        self.colorbar = None

        return

    def addPlot(self, x, y, color=None, label="", xlabel=None, ylabel=None, marker=None, linestyle=None, linewidth=1):
        """ Plot a set of data
        Argument:
        - x: numpy array X
        - y: numpy array Y
        """
        # Test... FIXME 
        self.axes.hold(True)

        # process inputs and defaults
        self.x = x
        self.y = y
        
        if color is None:
            color = (0,1,0,1)
        if marker is None:
            marker = 'o'
        if linestyle is None:
            linestyle = '-'
            
        # color must be RGBA (4-tuple)
        r = self.axes.plot(x, y, color=color, marker=marker, linestyle=linestyle,
                label=label, linewidth=1) # return: list of matplotlib.lines.Line2D object

        # set x-axis and y-axis label
        if xlabel is not None:
            self.axes.set_xlabel(xlabel, fontsize=20)  
        if ylabel is not None:
            self.axes.set_ylabel(ylabel, fontsize=20)

        # set/update legend
        self.axes.legend()

        # Register
        if len(r) == 1: 
            self._lineDict[self._lineIndex] = r[0]
        else:
            print "Impoooooooooooooooosible!"
        self._lineIndex += 1

        # Flush/commit
        self.draw()

        return


    def addPlot2D(self, array2d, xmin, xmax, ymin, ymax, holdprev):
        """ Add a 2D plot
        """
        # Release the current image
        self.axes.hold(holdprev)

        # Do plot
        imgplot = self.axes.imshow(array2d, extent=[xmin,xmax,ymin,ymax])

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

    def addImage(self, imagefilename):
        """ Add an image by file
        """
        import matplotlib.image as mpimg 
        img = mpimg.imread(str(imagefilename))
        lum_img = img[:,:,0] 
        imgplot = self.axes.imshow(lum_img) 

        # Set color bar.  plt.colorbar() does not work!
        if self.colorbar is None:
            # set color map type
            imgplot.set_cmap('spectral')
            self.colorbar = self.fig.colorbar(imgplot)
        else:
            self.colorbar.update_bruteforce(imgplot)

        self._flush()

        return

        
    def clearAllLines(self):
        """ Remove all lines from the canvas
        """
        for ikey in self._lineDict.keys():
            plot = self._lineDict[ikey]
            if plot is not None:
                self.axes.lines.remove(plot)
                self._lineDict[ikey] = None
            # ENDIF(plot)
        # ENDFOR
        
        self.draw()

        return


    def clearCanvas(self):
        """ Clear data from canvas
        """
        # clear the image for next operation
        self.axes.hold(False)

        # clear image
        self.axes.cla()

        # flush/commit
        self._flush()

        return


    def getLastPlotIndexKey(self):
        """ Get the index/key of the last added line
        """
        return self._lineIndex-1


    def getPlot(self):
        """ reture figure's axes to expose the matplotlib figure to PyQt client
        """
        return self.axes

    def setXYLimit(self, xmin, xmax, ymin, ymax):
        """
        """
        # for X
        xlims = self.axes.get_xlim() 
        xlims = list(xlims)
        if xmin is not None:
            xlims[0] = xmin
        if xmax is not None:
            xlims[1] = xmax
        self.axes.set_xlim(xlims)

        # for Y 
        ylims = self.axes.get_ylim() 
        ylims = list(ylims)
        if ymin is not None:
            ylims[0] = ymin
        if ymax is not None:
            ylims[1] = ymax
        self.axes.set_ylim(ylims)

        # try draw
        self.draw()

        return



    def removePlot(self, ikey):
        """ Remove the line with its index as key
        """
        # self._lineDict[ikey].remove()
        lines = self.axes.lines
        print str(type(lines)), lines
        print "ikey = ", ikey, self._lineDict[ikey]
        self.axes.lines.remove(self._lineDict[ikey])
        #self.axes.remove(self._lineDict[ikey])
        print self._lineDict[ikey]
        self._lineDict[ikey] = None

        return

    def updateLine(self, ikey, vecx, vecy, linestyle=None, linecolor=None, marker=None, markercolor=None):
        """
        """
        line = self._lineDict[ikey]

        if vecx is not None and vecy is not None:
            line.set_xdata(vecx)
            line.set_ydata(vecy)

        if linecolor is not None:
            line.set_color(linecolor)

        if linestyle is not None:
            line.set_linestyle(linestyle)

        if marker is not None:
            line.set_marker(marker)

        if markercolor is not None:
            line.set_markerfacecolor(markercolor)

        oldlabel = line.get_label()
        line.set_label(oldlabel)

        self.axes.legend()

        # commit
        self.draw()

        return

    def getLineStyleList(self):
        """
        """
        return MplLineStyles


    def getLineMarkerList(self):
        """
        """
        return MplLineMarkers

    def getLineBasicColorList(self):
        """
        """
        return MplBasicColors 
        
    def getDefaultColorMarkerComboList(self):
        """ Get a list of line/marker color and marker style combination 
        as default to add more and more line to plot
        """
        combolist = []
        nummarkers = len(MplLineMarkers)
        numcolors = len(MplBasicColors)
        
        for i in xrange(nummarkers):
            marker = MplLineMarkers[i]
            for j in xrange(numcolors):
                color = MplBasicColors[j]
                combolist.append( (marker, color) )
            # ENDFOR (j)
        # ENDFOR(i)
        
        return combolist


    def _flush(self):
        """ A dirty hack to flush the image
        """
        w, h = self.get_width_height()
        self.resize(w+1,h)
        self.resize(w,h)


class MyNavigationToolbar(NavigationToolbar):
    """ A customized navigation tool bar attached to canvas
    """
    def __init__(self, parent, canvas, direction='h'):
        """ Initialization
        """
        self.canvas = canvas
        QtGui.QWidget.__init__(self, parent)

        #if direction=='h' :
        #    self.layout = QtGui.QHBoxLayout(self)
        #else :
        #    self.layout = QtGui.QVBoxLayout(self)

        #self.layout.setMargin(2)
        #self.layout.setSpacing(0)

        NavigationToolbar.__init__( self, canvas, canvas )

        return
