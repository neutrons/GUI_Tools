#pylint: disable=invalid-name,too-many-public-methods,too-many-arguments,non-parent-init-called, too-many-branches
import os
import numpy as np

from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.image

MplLineStyles = ['-' , '--' , '-.' , ':' , 'None' , ' ' , '']
MplLineMarkers = [
    ". (point         )",
    "* (star          )",
    "x (x             )",
    "o (circle        )",
    "s (square        )",
    "D (diamond       )",
    ", (pixel         )",
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
    "h (hexagon1      )",
    "H (hexagon2      )",
    "+ (plus          )",
    "d (thin_diamond  )",
    "| (vline         )",
    "_ (hline         )",
    "None (nothing    )"]

# Note: in colors, "white" is removed
MplBasicColors = [
    "black",
    "red",
    "blue",
    "green",
    "cyan",
    "magenta",
    "yellow"] 

class IndicatorLine(object):
    """ A picker line """
    # TODO - To be implemented


class MplGraphicsView(QtGui.QWidget):
    """ A combined graphics view including matplotlib canvas and
    a navigation tool bar

    Note: Merged with HFIR_Powder_Reduction.MplFigureCAnvas
    """
    def __init__(self, parent):
        """ Initialization
        """
        # Initialize parent
        QtGui.QWidget.__init__(self, parent)

        # set up canvas
        self.canvas = Qt4MplCanvas(self)
        self.toolbar = MyNavigationToolbar(self.canvas, self.canvas)

        # set up layout
        self.vbox = QtGui.QVBoxLayout(self)
        self.vbox.addWidget(self.canvas)
        self.vbox.addWidget(self.toolbar)

        # auto line's maker+color list
        self._myLineMarkerColorList = []
        self._myLineMarkerColorIndex = 0
        self.setAutoLineMarkerColorCombo()

        return

    def add_plot_1d(self, vec_x, vec_y, y_err=None, color=None, label="", x_label=None, y_label=None, marker=None,
                    line_style=None, line_width=1):
        """ Add a new plot
        """
        self.canvas.add_plot_1d(vec_x, vec_y, y_err, color, label, x_label, y_label, marker, line_style, line_width)

        #self.canvas.addPlotY2(x, y*100)
        #self.canvas.addPlotY2([0, 1, 2], [50, 30, 15])

        return
    
    def addHorizontalIndicator(self, y, color):
        """ Add an indicator line
        """
        xmin, xmax = self.canvas.getXLimit()
        vecx = numpy.array([xmin, xmax])
        vecy = numpy.array([y, y])
        
        self._indicatorKey = self.canvas.add_plot_1d(vecx, vecy, color, line_style='--')

        return
            
    def addVerticalIndicator(self, x, color):
        """ Add a vertical indicator line """
        ymin, ymax = self.canvas.getYLimit()

        return

    def add_plot_2d(self, array2d, x_min, x_max, y_min, y_max, hold_prev_image=True, y_tick_label=None):
        """
        Add a 2D image to canvas
        :param array2d: numpy 2D array
        :param x_min:
        :param x_max:
        :param y_min:
        :param y_max:
        :param hold_prev_image:
        :param y_tick_label:
        :return:
        """
        self.canvas.addPlot2D(array2d, x_min, x_max, y_min, y_max, hold_prev_image, y_tick_label)

        return


    def addImage(self, imagefilename):
        """ Add an image by file
        """
        # check
        if os.path.exists(imagefilename) is False:
            raise NotImplementedError("Image file %s does not exist." % (imagefilename))

        self.canvas.addImage(imagefilename)

        return


    def clear_all_lines(self):
        """
        """
        self.canvas.clear_all_1d_plots()

    def clear_canvas(self):
        """ Clear canvas
        """
        return self.canvas.clear_canvas()

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

    def getXLimit(self):
        """ Get limit of Y-axis
        """
        return self.canvas.getXLimit()

    def getYLimit(self):
        """ Get limit of Y-axis
        """
        return self.canvas.getYLimit()

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
    
    def updateIndicator(self, vecx, vecy, ikey=None):
        """
        """
        if ikey is None:
            ikey = self._indicatorKey 


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

    def getNextLineMarkerColorCombo(self):
        """ As auto line's marker and color combo list is used,
        get the NEXT marker/color combo
        """
        # get from list
        marker, color = self._myLineMarkerColorList[self._myLineMarkerColorIndex]
        # process marker if it has information
        if marker.count(' (') > 0:
            marker = marker.split(' (')[0]
        print "[DB] Print line %d: marker = %s, color = %s" % (self._myLineMarkerColorIndex, marker, color)

        # update the index
        self._myLineMarkerColorIndex += 1
        if self._myLineMarkerColorIndex == len(self._myLineMarkerColorList):
            self._myLineMarkerColorIndex = 0

        return marker, color

    def resetLineColorStyle(self):
        """ Reset the auto index for line's color and style
        """
        self._myLineMarkerColorIndex = 0
        return

    def setXYLimit(self, xmin, xmax, ymin, ymax):
        """ Set X-Y limit automatically
        """
        self.canvas.axes.set_xlim([xmin, xmax])
        self.canvas.axes.set_ylim([ymin, ymax])

        self.canvas.draw()

        return

    def setAutoLineMarkerColorCombo(self):
        """
        """
        self._myLineMarkerColorList = []
        for marker in MplLineMarkers:
            for color in MplBasicColors:
                self._myLineMarkerColorList.append( (marker, color) )

        return

    def setLineMarkerColorIndex(self, newindex):
        """
        """
        self._myLineMarkerColorIndex = newindex

        return


class Qt4MplCanvas(FigureCanvas):
    """  A customized Qt widget for matplotlib figure.
    It can be used to replace GraphicsView of QtGui
    """
    def __init__(self, parent):
        """  Initialization
        """
        from mpl_toolkits.axes_grid1 import host_subplot 
        # import mpl_toolkits.axisartist as AA
        import matplotlib.pyplot as plt

        # Instantialize matplotlib Figure
        self.fig = Figure() 
        self.fig.patch.set_facecolor('white')
        
        if True:
            self.axes = self.fig.add_subplot(111) # return: matplotlib.axes.AxesSubplot
            self.axes2 = None
        else:
            self.axes = self.fig.add_host_subplot(111)

        # Initialize parent class and set parent
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        # Set size policy to be able to expanding and resizable with frame
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        # Variables to manage all lines/subplot
        self._lineDict = {}
        self._lineIndex = 0

        # legend and color bar
        self._colorBar = None

        return

    def add_plot_1d(self, vec_x, vec_y, y_err=None, color=None, label="", x_label=None, y_label=None,
                    marker=None, line_style=None, line_width=1):
        """

        :param vec_x: numpy array X
        :param vec_y: numpy array Y
        :param y_err:
        :param color:
        :param label:
        :param x_label:
        :param y_label:
        :param marker:
        :param line_style:
        :param line_width:
        :return: new key
        """
        # Check input
        if isinstance(vec_x, np.ndarray) is False or isinstance(vec_y, np.ndarray) is False:
            raise NotImplementedError('Input vec_x or vec_y for addPlot() must be numpy.array.')
        plot_error = y_err is not None
        if plot_error is True:
            if isinstance(y_err, np.ndarray) is False:
                raise NotImplementedError('Input y_err must be either None or numpy.array.')

        if len(vec_x) != len(vec_y):
            raise NotImplementedError('Input vec_x and vec_y must have same size.')
        if plot_error is True and len(y_err) != len(vec_x):
            raise NotImplementedError('Input vec_x, vec_y and y_error must have same size.')

        # Hold previous data
        self.axes.hold(True)

        # process inputs and defaults
        if color is None:
            color = (0,1,0,1)
        if marker is None:
            marker = 'o'
        if line_style is None:
            line_style = '-'

        # color must be RGBA (4-tuple)
        if plot_error is False:
            print "[DB] line_style = ", line_style, "line_width = ", line_width, "marker = ", marker, "color = ", color
            r = self.axes.plot(vec_x, vec_y, color=color, marker=marker, linestyle=line_style,
                               label=label, linewidth=line_width)
            # return: list of matplotlib.lines.Line2D object
        else:
            r = self.axes.errorbar(vec_x, vec_y, yerr=y_err, color=color, marker=marker, linestyle=line_style,
                                   label=label, linewidth=line_width)

        self.axes.set_aspect('auto')

        # set x-axis and y-axis label
        if x_label is not None:
            self.axes.set_xlabel(x_label, fontsize=20)
        if y_label is not None:
            self.axes.set_ylabel(y_label, fontsize=20)

        # set/update legend
        self._setupLegend()

        # Register
        line_key = self._lineIndex
        if len(r) == 1:
            self._lineDict[line_key] = r[0]
            self._lineIndex += 1    
        else:
            print "Impoooooooooooooooosible!  Return from plot is a %d-tuple. " % (len(r))

        # Flush/commit
        self.draw()

        return line_key


    def addPlotY2(self, x, y, color=None, label="", xlabel=None, ylabel=None, marker=None, linestyle=None, linewidth=1):
        """ Add second plot
        """
        if self.axes2 is None:
            self.axes2 = self.axes.twinx()
            # print self.par1, type(self.par1)

        # Hold previous data
        self.axes2.hold(True)

        # process inputs and defaults
        self._x2 = x
        self._y2 = y

        if color is None:
            color = (0,1,0,1)
        if marker is None:
            marker = 'o'
        if linestyle is None:
            linestyle = '-'

        # color must be RGBA (4-tuple)
        r = self.axes2.plot(x, y, color=color, marker=marker, linestyle=linestyle,
                label=label, linewidth=linewidth) # return: list of matplotlib.lines.Line2D object

        self.axes2.set_aspect('auto')

        # set x-axis and y-axis label
        if xlabel is not None:
            self.axes2.set_xlabel(xlabel, fontsize=20)
        if ylabel is not None:
            self.axes2.set_ylabel(ylabel, fontsize=20)

        # set/update legend
        self._setupLegend()

        # Register
        if len(r) == 1:
            self._lineDict[self._lineIndex] = r[0]
        else:
            print "Impoooooooooooooooosible!"
        self._lineIndex += 1

        # Flush/commit
        self.draw()

        return


    def addPlot2D(self, array2d, xmin, xmax, ymin, ymax, holdprev, yticklabels=None):
        """ Add a 2D plot

        Arguments:
         - yticklabels :: list of string for y ticks
        """
        # Release the current image
        self.axes.hold(holdprev)

        # Do plot
        # y ticks will be shown on line 1, 4, 23, 24 and 30
        # yticks = [1, 4, 23, 24, 30]
        # self.axes.set_yticks(yticks)

        # show image
        imgplot = self.axes.imshow(array2d, extent=[xmin,xmax,ymin,ymax], interpolation='none')
        # set y ticks as an option:
        if yticklabels is not None:
            # it will always label the first N ticks even image is zoomed in
            print "--------> [FixMe]: Set up the Y-axis ticks is erroreous"
            #self.axes.set_yticklabels(yticklabels)

        # explicitly set aspect ratio of the image
        self.axes.set_aspect('auto')

        # Set color bar.  plt.colorbar() does not work!
        if self._colorBar is None:
            # set color map type
            imgplot.set_cmap('spectral')
            self._colorBar = self.fig.colorbar(imgplot)
        else:
            self._colorBar.update_bruteforce(imgplot)

        # Flush...
        self._flush()

        return

    def addImage(self, imagefilename):
        """ Add an image by file
        """
        #import matplotlib.image as mpimg

        # set aspect to auto mode
        self.axes.set_aspect('auto')

        img = matplotlib.image.imread(str(imagefilename))
        # lum_img = img[:,:,0]
        # FUTURE : refactor for image size, interpolation and origin
        imgplot = self.axes.imshow(img, extent=[0, 1000, 800, 0], interpolation='none', origin='lower')

        # Set color bar.  plt.colorbar() does not work!
        if self._colorBar is None:
            # set color map type
            imgplot.set_cmap('spectral')
            self._colorBar = self.fig.colorbar(imgplot)
        else:
            self._colorBar.update_bruteforce(imgplot)

        self._flush()

        return

    def clear_all_1d_plots(self):
        """ Remove all lines from the canvas
        """
        for ikey in self._lineDict.keys():
            plot = self._lineDict[ikey]
            if plot is None:
                continue
            if isinstance(plot, tuple) is False:
                try:
                    self.axes.lines.remove(plot)
                except ValueError as e:
                    print "[Error] Plot %s is not in axes.lines which has %d lines. Error mesage: %s" % (
                        str(plot), len(self.axes.lines), str(e))
                self._lineDict[ikey] = None
            else:
                # error bar
                plot[0].remove()
                for line in plot[1]:
                    line.remove()
                for line in plot[2]:
                    line.remove()
                self._lineDict[ikey] = None
            # ENDIF(plot)
        # ENDFOR

        self._setupLegend()

        self.draw()

        return

    def clear_canvas(self):
        """ Clear data including lines and image from canvas
        """
        # clear the image for next operation
        self.axes.hold(False)

        # Clear all lines
        self.clear_all_1d_plots()

        # clear image
        self.axes.cla()
        # Try to clear the color bar
        if len(self.fig.axes) > 1:
            self.fig.delaxes(self.fig.axes[1])
            self.colorBar = None
            # This clears the space claimed by color bar but destroys sub_plot too.
            self.fig.clear()
            # Re-create subplot
            self.axes = self.fig.add_subplot(111)

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

    def getXLimit(self):
        """ Get limit of Y-axis
        """
        return self.axes.get_xlim()

    def getYLimit(self):
        """ Get limit of Y-axis
        """
        return self.axes.get_ylim()

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

        return


    def _setupLegend(self, location='best'):
        """ Set up legend
        self.axes.legend()
        Handler is a Line2D object. Lable maps to the line object
        """
        loclist = [
            "best",
            "upper right",
            "upper left",
            "lower left",
            "lower right",
            "right",
            "center left",
            "center right",
            "lower center",
            "upper center",
            "center"]

        # Check legend location valid or not
        if location not in loclist:
            location = 'best'

        handles, labels = self.axes.get_legend_handles_labels()
        self.axes.legend(handles, labels, loc=location)
        # print handles
        # print labels
        #self.axes.legend(self._myLegendHandlers, self._myLegentLabels)

        return



class MyNavigationToolbar(NavigationToolbar):
    """ A customized navigation tool bar attached to canvas
    """
    def __init__(self, parent, canvas):
        """ Initialization
        FUTURE: direction='h'
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
