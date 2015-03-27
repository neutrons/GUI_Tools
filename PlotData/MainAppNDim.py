###############################################################################
#
# Main Application for both 1D and 2D Image
#
###############################################################################
import sys
import os
import numpy 
import numpy as np
import math
from math import *


from PyQt4 import QtCore,  QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s 

from ui_MainWindowNDim import *


class MainAppNDim(QtGui.QMainWindow):
    """ Main application for 1-D (x-y) plot
    """
    def __init__(self, parent=None):
        """ Initialization
        """
        # call constructor
        QtGui.QMainWindow.__init__(self, parent)

        # call GUI setup
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # define event handlers
        self.connect(self.ui.pushButton_plot1D, QtCore.SIGNAL('clicked()'),
                self.doPlot)
        self.connect(self.ui.pushButton_delLastLine, QtCore.SIGNAL('clicked()'),
                self.doDeleteLastLine)
        self.connect(self.ui.pushButton_changeLastLine, QtCore.SIGNAL('clicked()'),
                self.doChangeLastLine)
        self.connect(self.ui.pushButton_plot2D, QtCore.SIGNAL('clicked()'),
                self.doDraw2D)
        self.connect(self.ui.pushButton_rescale, QtCore.SIGNAL('clicked()'),
                self.doRescaleCanvas)
        self.connect(self.ui.pushButton_clear2D, QtCore.SIGNAL('clicked()'),
                self.doClear2D) 
        self.connect(self.ui.pushButton_plotImage, QtCore.SIGNAL('clicked()'),
                self.doPlotImage)

        self.connect(self.ui.actionQuit, QtCore.SIGNAL('triggered()'),
                self.doQuit)

        # set up initial values to widgets
        self.ui.comboBox_lineStyle.addItems(self.ui.canvas.getLineStyleList())
        self.ui.comboBox_color.addItems(self.ui.canvas.getLineBasicColorList())
        self.ui.comboBox_marker.addItems(self.ui.canvas.getLineMarkerList())

        return

    def doChangeLastLine(self):
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
        ikey = self.ui.canvas.getLastPlotIndexKey()

        # Do something
        linestyle = str(self.ui.comboBox_lineStyle.currentText())
        color = str(self.ui.comboBox_color.currentText())
        linemarker = str(self.ui.comboBox_marker.currentText())

        # extra process on color
        if linemarker.count(' (') > 0:
            linemarker = linemarker.split(' (')[0]

        self.ui.canvas.updateLine(ikey, vecx, vecy, linecolor=color, linestyle=linestyle, 
                marker=linemarker, markercolor=color)

        # Commit
        self.ui.canvas.draw()

        return

    def doClear2D(self):
        """ Clear 2D image (2D plot and image from imshow)
        """
        self.ui.canvas.clearCanvas()

        return


    def doDeleteLastLine(self):
        """ Delete last added line
        """
        ikey = self.ui.canvas.getLastPlotIndexKey()
        self.ui.canvas.removePlot(ikey)
        self.ui.canvas.draw()

        return

    def doDraw2D(self):
        """ Draw a picture of 2D
        Can specify input as (number of line), x0, dx, xf, x1, x2, x3, ....
        """
        def gauss(vecx, x0, s):
            """ A Gaussian 
            """
            listy = []
            for i in xrange(len(vecx)):
                y = s*math.exp(-2*(vecx[i]-x0)**2)
                listy.append(y)
                
            vecy = numpy.array(listy)

            return vecy
       
        listx = []
        x0 = 0
        xf = 100
        dx = 0.01
        x = 0
        while x < xf:
            listx.append(x)
            x += dx
        vecx = numpy.array(listx)
        vecy1 = gauss(vecx, 20, 5)
        vecy2 = gauss(vecx, 40, 10)
        vecy3 = gauss(vecx, 60, 10)
        vecy4 = gauss(vecx, 80, 60)
        vecy5 = gauss(vecx, 90, 60) + gauss(vecx, 10, 20)
        dim2array = numpy.array([vecy1, vecy2, vecy3, vecy4, vecy5])

        yticklabels = ['a', 'b', 'c', 'd', 'e']
        holdprev=True
        self.ui.canvas.addPlot2D(dim2array, xmin=x0, xmax=xf, ymin=0, ymax=4+1, holdprev=True, yticklabels=yticklabels)

        return


    def doPlot(self):
        """ Plot
        """
        # parse input
        linelist = str(self.ui.lineEdit_formular.text()).split(";")
        for line in linelist:
            # get formular, x-range and bin size
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

            self.ui.canvas.addPlot(vecx, vecy)
        # ENDFOR

        # Draw !
        self.ui.canvas.draw()

        return

    def doPlotImage(self):
        """ Plot an image file .png, .jpg, .gif
        """
        # get file name
        imagefilename = str(self.ui.lineEdit_imagefile.text()).strip()
        if os.path.exists(imagefilename) is False:
            dogetfile = True
        else:
            if imagefilename.lower().endswith(".png") is False and \
                    imagefilename.lower().endswith(".jpg") is False and \
                    imagefilename.lower().endswith(".jpeg") is False and \
                    imagefilename.lower().endswith(".gif") is False:
                dogetfile = True
            else:
                dogetfile = False
        # ENDIF

        if dogetfile is True: 
            curdir = os.getcwd()
            filefilter = "jpg (*.jpg);;gif (*.gif);;png (*.png);;All files (*.*)" 
            fileList = QtGui.QFileDialog.getOpenFileNames(self, 'Open File(s)', curdir, filefilter)
            imagefilename = fileList[0]
           
        print "Plot image file %s." % (imagefilename)

        self.ui.canvas.addImage(imagefilename)
        self.ui.lineEdit_imagefile.setText(imagefilename)

        return

    def doQuit(self):
        """ Quit!
        """
        self.close()

        return


    def doRescaleCanvas(self):
        """
        """
        try:
            minx = float(self.ui.lineEdit_minX.text())
        except ValueError:
            minx = None

        try: 
            maxx = float(self.ui.lineEdit_maxX.text())
        except ValueError:
            maxx = None

        try: 
            miny = float(self.ui.lineEdit_minY.text())
        except ValueError:
            miny = None

        try: 
            maxy = float(self.ui.lineEdit_maxY.text())
        except ValueError:
            maxy = None

        self.ui.canvas.setXYLimits(minx, maxx, miny, maxy)

        return


if __name__ == "__main__":
    mainApp = QtGui.QApplication(sys.argv)

    myapp = MainAppNDim()
    myapp.show()

    sys.exit(mainApp.exec_())
