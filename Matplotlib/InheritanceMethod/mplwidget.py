#!/usr/bin/env python
import os
import tempfile
from PyQt4 import QtCore, QtGui
import matplotlib.cm
#import matplotlib.colors

#cmap=matplotlib.colors.LinearSegmentedColormap.from_list('default',
#                                                         ['#0000ff', '#00ff00', '#ffff00', '#ff0000', '#bd7efc', '#000000'], N=256)
#matplotlib.cm.register_cmap('default', cmap=cmap)

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT
#from matplotlib.cbook import Stack
#from matplotlib.colors import LogNorm, Normalize
from matplotlib.figure import Figure
#try:
    #import matplotlib.backends.qt4_editor.figureoptions as figureoptions
#except ImportError:
    #figureoptions=None

class NavigationToolbar(NavigationToolbar2QT):
    '''
      A small change to the original navigation toolbar.
    '''
    _auto_toggle=False
    #logtog = QtCore.pyqtSignal(str)
    #homeClicked = QtCore.pyqtSignal()
    exportClicked = QtCore.pyqtSignal()

    #isPanActivated = False
    #isZoomActivated = False

    home_settings = None

    def __init__(self, canvas, parent, coordinates=False):
        NavigationToolbar2QT.__init__(self, canvas, parent, coordinates)
        self.setIconSize(QtCore.QSize(20, 20)) # to change size of icons in toolbar

    def _init_toolbar(self):
        NavigationToolbar2QT._init_toolbar(self) 
       
        # adding a new icon
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MPL Toolbar/export_ascii.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        a=self.addAction(icon, "Export", self.export_ascii)
        a.setToolTip('Export the plot into ASCII file')
     
    def export_ascii(self):
        self.exportClicked.emit()

class MplCanvas(FigureCanvas):

    #trigger_click = QtCore.pyqtSignal()
    #trigger_figure_left = QtCore.pyqtSignal()

    def __init__(self, parent=None, width=3, height=3, dpi=100, sharex=None, sharey=None, adjust={}):
        self.fig=Figure(figsize=(width, height), dpi=dpi, facecolor='#FFFFFF')
        self.ax=self.fig.add_subplot(111, sharex=sharex, sharey=sharey)
        self.fig.subplots_adjust(left=0.15, bottom=0.1, right=0.95, top=0.95)
        self.xtitle=""
        self.ytitle=""
        self.PlotTitle=""
        self.grid_status=True
        self.xaxis_style='linear'
        self.yaxis_style='linear'
        self.format_labels()
        self.ax.hold(True)
        FigureCanvas.__init__(self, self.fig)
        #self.fc = FigureCanvas(self.fig)
        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        #self.fig.canvas.mpl_connect('button_press_event', self.button_pressed)
        #self.fig.canvas.mpl_connect('figure_leave_event', self.figure_leave)

    #def button_pressed(self, event):
        #self.trigger_click.emit()

    #def figure_leave(self, event):
        #self.trigger_figure_left.emit()

    def format_labels(self):
        self.ax.set_title(self.PlotTitle)
        self.ax.title.set_fontsize(10)
        self.ax.set_xlabel(self.xtitle, fontsize=9)
        self.ax.set_ylabel(self.ytitle, fontsize=9)
        labels_x=self.ax.get_xticklabels()
        labels_y=self.ax.get_yticklabels()
        
        for xlabel in labels_x:
            xlabel.set_fontsize(8)
        for ylabel in labels_y:
            ylabel.set_fontsize(8)

    def sizeHint(self):
        w, h=self.get_width_height()
        w=max(w, self.height())
        h=max(h, self.width())
        return QtCore.QSize(w, h)

    def minimumSizeHint(self):
        return QtCore.QSize(40, 40)

    def get_default_filetype(self):
        return 'png'


class MPLWidget(QtGui.QWidget):
    cplot=None
    cbar=None

    #logtogy = QtCore.pyqtSignal(str)
    #singleClick = QtCore.pyqtSignal(bool)
    #leaveFigure = QtCore.pyqtSignal()

    def __init__(self, parent=None, with_toolbar=True, coordinates=False):
        QtGui.QWidget.__init__(self, parent)
        self.canvas=MplCanvas()
        self.canvas.ax2=None
        self.vbox=QtGui.QVBoxLayout()
        self.vbox.setMargin(1)
        self.vbox.addWidget(self.canvas)
        if with_toolbar:
            self.toolbar=NavigationToolbar(self.canvas, self)
            self.toolbar.coordinates=coordinates
            self.vbox.addWidget(self.toolbar)
            #self.toolbar.logtog.connect(self.logtoggleylog)
        else:
            self.toolbar=None
        self.setLayout(self.vbox)

    def _singleClick(self):
        status = self.toolbar.isPanActivated or self.toolbar.isZoomActivated
        self.singleClick.emit(status)

    def _leaveFigure(self):
        self.leaveFigure.emit()

    def logtoggleylog(self, status):
        self.logtogy.emit(status)

    def leaveEvent(self, event):
        '''
        Make sure the cursor is reset to it's default when leaving the widget.
        In some cases the zoom cursor does not reset when leaving the plot.
        '''
        if self.toolbar:
            QtGui.QApplication.restoreOverrideCursor()
            self.toolbar._lastCursor=None
        return QtGui.QWidget.leaveEvent(self, event)

    def set_config(self, config):
        self.canvas.fig.subplots_adjust(**config)

    def get_config(self):
        spp=self.canvas.fig.subplotpars
        config=dict(left=spp.left,
                    right=spp.right,
                    bottom=spp.bottom,
                    top=spp.top)
        return config


    def draw(self):
        '''
          Convenience to redraw the graph.
        '''
        self.canvas.draw()

    def plot(self, *args, **opts):
        '''
          Convenience wrapper for self.canvas.ax.plot
        '''
        return self.canvas.ax.plot(*args, **opts)

    def semilogy(self, *args, **opts):
        '''
          Convenience wrapper for self.canvas.ax.semilogy
        '''
        return self.canvas.ax.semilogy(*args, **opts)

    def errorbar(self, *args, **opts):
        '''
          Convenience wrapper for self.canvas.ax.semilogy
        '''
        return self.canvas.ax.errorbar(*args, **opts)

    def pcolormesh(self, datax, datay, dataz, log=False, imin=None, imax=None, update=False, **opts):
        '''
          Convenience wrapper for self.canvas.ax.plot
        '''
        if self.cplot is None or not update:
            if log:
                self.cplot=self.canvas.ax.pcolormesh(datax, datay, dataz, norm=LogNorm(imin, imax), **opts)
            else:
                self.cplot=self.canvas.ax.pcolormesh(datax, datay, dataz, **opts)
        else:
            self.update(datax, datay, dataz)
        return self.cplot

    def imshow(self, data, log=False, imin=None, imax=None, update=True, **opts):
        '''
          Convenience wrapper for self.canvas.ax.plot
        '''
        if self.cplot is None or not update:
            if log:
                self.cplot=self.canvas.ax.imshow(data, norm=LogNorm(imin, imax), **opts)
            else:
                self.cplot=self.canvas.ax.imshow(data, **opts)
        else:
            self.update(data, **opts)
        return self.cplot

    def set_title(self, new_title):
        return self.canvas.ax.title.set_text(new_title)

    def set_xlabel(self, label):
        return self.canvas.ax.set_xlabel(label)

    def set_ylabel(self, label):
        return self.canvas.ax.set_ylabel(label)

    def set_xscale(self, scale):
        try:
            return self.canvas.ax.set_xscale(scale)
        except ValueError:
            pass

    def set_yscale(self, scale):
        try:
            return self.canvas.ax.set_yscale(scale)
        except ValueError:
            pass

    def clear_fig(self):
        self.cplot=None
        self.cbar=None
        self.canvas.fig.clear()
        self.canvas.ax=self.canvas.fig.add_subplot(111, sharex=None, sharey=None)

    def clear(self):
        self.cplot=None
        self.toolbar._views.clear()
        self.toolbar._positions.clear()
        self.canvas.ax.clear()
        if self.canvas.ax2 is not None:
            self.canvas.ax2.clear()

    def update(self, *data, **opts):
        self.cplot.set_data(*data)
        if 'extent' in opts:
            self.cplot.set_extent(opts['extent'])
            oldviews=self.toolbar._views
            if self.toolbar._views:
                # set the new extent as home for the new data
                newviews=Stack()
                newviews.push([tuple(opts['extent'])])
                for item in oldviews[1:]:
                    newviews.push(item)
                self.toolbar._views=newviews
            if not oldviews or oldviews[oldviews._pos]==oldviews[0]:
                self.canvas.ax.set_xlim(opts['extent'][0], opts['extent'][1])
                self.canvas.ax.set_ylim(opts['extent'][2], opts['extent'][3])

    def legend(self, *args, **opts):
        return self.canvas.ax.legend(*args, **opts)

    def adjust(self, **adjustment):
        return self.canvas.fig.subplots_adjust(**adjustment)
