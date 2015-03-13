###############################################################################
#
# Main Application for 1D Image
#
###############################################################################
import sys
import numpy 
from math import *

from PyQt4 import QtCore,  QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s 

from MplFigureCanvas import Qt4MplCanvas

# from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
# 
# from matplotlib.figure import Figure
# from mpl_toolkits.mplot3d import Axes3D


#class MainApp1D(QtGui.QMainWindow): QMainWindow has a self-defined layout.  No more layout can be declared on it
class MainApp1Dextent(QtGui.QWidget):
    """ Main application for 1-D (x-y) plot
    """
    def __init__(self, parent=None):
        """ Initialization
        """
        # call constructor
        #QtGui.QMainWindow.__init__(self, parent)
        QtGui.QWidget.__init__(self, parent)

        # set up GUI 
        self.resize(800,600)

        # - functional widget
        self.ui_canvas = Qt4MplCanvas(self)
        self.ui_lineEdit1 = QtGui.QLineEdit(self)
        self.ui_button1 = QtGui.QPushButton(self)
        self.ui_button1.setText("Add Line")
        self.ui_button2 = QtGui.QPushButton(self)
        self.ui_button2.setObjectName(_fromUtf8("ui_button2"))
        self.ui_button2.setText('Delete Last Line')
        self.ui_button3 = QtGui.QPushButton(self)
        self.ui_button3.setObjectName(_fromUtf8("ui_button3"))
        self.ui_button3.setText('Change Last Line Style')

        self.ui_combobox_lineStyle = QtGui.QComboBox(self)
        self.ui_combobox_lineStyle.addItems(self.ui_canvas.getLineStyleList())

        self.ui_combobox_color = QtGui.QComboBox(self)
        self.ui_combobox_color.addItems(self.ui_canvas.getLineBasicColorList())

        self.ui_combobox_marker = QtGui.QComboBox(self)
        self.ui_combobox_marker.addItems(self.ui_canvas.getLineMarkerList())


        # - layout
        self.ui_hbox = QtGui.QHBoxLayout(self)

        self.ui_vbox = QtGui.QVBoxLayout()
        self.ui_hbox.addLayout(self.ui_vbox)
        self.ui_vbox_ctrl= QtGui.QVBoxLayout()
        self.ui_hbox.addLayout(self.ui_vbox_ctrl)

        self.ui_vbox.addWidget(self.ui_canvas)
        self.ui_vbox.addWidget(self.ui_button1)
        self.ui_vbox.addWidget(self.ui_lineEdit1)

        self.ui_vbox_ctrl.addWidget(self.ui_button2)
        self.ui_vbox_ctrl.addWidget(self.ui_button3)
        self.ui_vbox_ctrl.addWidget(self.ui_combobox_lineStyle)
        self.ui_vbox_ctrl.addWidget(self.ui_combobox_color)
        self.ui_vbox_ctrl.addWidget(self.ui_combobox_marker)

        # define event handlers
        self.connect(self.ui_button1, QtCore.SIGNAL('clicked()'),
                self.doPlot)

        self.connect(self.ui_button2, QtCore.SIGNAL('clicked()'),
                self.doDeleteLine)

        self.connect(self.ui_button3, QtCore.SIGNAL('clicked()'),
                self.doChangeLine)

        return

    def doDeleteLine(self):
        """ Delete last added line
        """
        ikey = self.ui_canvas.getLastPlotIndexKey()
        self.ui_canvas.removePlot(ikey)
        self.ui_canvas.draw()

        return


    def doChangeLine(self):
        """ Change the color and value of last line
        """
        # Line value
        vecx = None
        vecy = None
        linelist = str(self.ui_lineEdit1.text()).split(";")
        for line in linelist:
            line = line.strip()
            if len(line) == 0:
                continue
            print "Parse: ", line

            terms = line.split(",")
            if len(terms) != 4: 
                print "Unsupported.. must be : y=f(x), xmin, dx, xmax"

            equation = terms[0].strip()
            if equation.count('=') > 0:
                equation = equation.split('=')[1]
            xmin = float(terms[1])
            dx = float(terms[2])
            xmax = float(terms[3])
    
            # initialize vecx and vecy
            vecx = numpy.arange(xmin, xmax, dx)
            vecy = numpy.empty(len(vecx))

            for i in xrange(len(vecx)):
                x = vecx[i]
                vecy[i] = eval(equation)
                print x, vecy[i]

            break
        # ENDFOR

        # Get last line
        ikey = self.ui_canvas.getLastPlotIndexKey()

        # Do something
        linestyle = str(self.ui_combobox_lineStyle.currentText())
        color = str(self.ui_combobox_color.currentText())
        linemarker = str(self.ui_combobox_marker.currentText())

        # extra process on color
        if linemarker.count(' (') > 0:
            linemarker = linemarker.split(' (')[0]

        self.ui_canvas.updateLine(ikey, vecx, vecy, linecolor=color, linestyle=linestyle, marker=linemarker, markercolor=color)

        # Commit
        self.ui_canvas.draw()

        return



    def doPlot(self):
        """ Plot
        """
        # parse input
        linelist = str(self.ui_lineEdit1.text()).split(";")
        for line in linelist:
            line = line.strip()
            if len(line) == 0:
                continue
            print "Parse: ", line

            terms = line.split(",")
            if len(terms) != 4: 
                print "Unsupported.. must be : y=f(x), xmin, dx, xmax"

            equation = terms[0].strip()
            if equation.count('=') > 0:
                equation = equation.split('=')[1]
            xmin = float(terms[1])
            dx = float(terms[2])
            xmax = float(terms[3])
    
            # initialize vecx and vecy
            vecx = numpy.arange(xmin, xmax, dx)
            vecy = numpy.empty(len(vecx))
            #print "vecx: ", vecx
            #print "vecy: ", vecy

            print "Size of X = %d" % (len(vecx))
            for i in xrange(len(vecx)):
                x = vecx[i]
                vecy[i] = eval(equation)
                print x, vecy[i]

            self.ui_canvas.addPlot(vecx, vecy)
        # ENDFOR

        # Draw !
        self.ui_canvas.draw()


if __name__ == "__main__":
    mainApp = QtGui.QApplication(sys.argv)

    myapp = MainApp1Dextent()
    myapp.show()

    sys.exit(mainApp.exec_())
