#!/usr/bin/env python
###############################################################################
#
# Main Application for both 1D and 2D Image
#
# Version 2.0
# - Focus on interacting with GUI
#
# Use cases
# (1) Add a vertical picker line and move it by push buttons;
# (2) Add a vertical picker line and move it by mouse;
#
# * Use case 1:
#   1. User clicks button 'Pick Mode';
#   2. App enters mode SELECTPOINTNEW from NOINTERACTION ;
#   3. User moves mouse cursor on to canvas and click mouse's button 1 (left);
#   4. App draw a vertical line crossing the cursor's position upon mouse's button being released;
#   5. User specifies step size in the line editor between button 'move left' and 'move right';
#   6. ... ...
#
# * Use case 2:
#   1. ...
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

class GraphInteractMode:
    NOINTERACTION = 0
    SELECTPOINTNEW = 1
    SELECTPOINTMID = 2
    
class MouseStatus:
    RELEASED = 0
    PRESSED = 1

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

        # define event handlers for matplotlib canvas
        self.ui.canvas.canvas.mpl_connect('button_press_event', self.on_mousePressEvent)
        self.ui.canvas.canvas.mpl_connect('button_release_event', self.on_mouseReleaseEvent)
        self.ui.canvas.canvas.mpl_connect('motion_notify_event', self.on_mouseMotion)
        
        # Interaction operation
        self.connect(self.ui.pushButton_intoPickMode, QtCore.SIGNAL('clicked()'),
                     self.do_enter_pick_mode)
        self.connect(self.ui.pushButton_moveLeft, QtCore.SIGNAL('clicked()'),
                     self.do_move_picker_left)        
        self.connect(self.ui.pushButton_moveRight, QtCore.SIGNAL('clicked()'),
                     self.do_move_picker_right)
        self.connect(self.ui.pushButton_select, QtCore.SIGNAL('clicked()'),
                     self.do_add_picker)
        
        self.connect(self.ui.pushButton_cancelInteractMode, QtCore.SIGNAL('clicked()'),
                     self.do_leave_interact_mode)

        # Mode
        self._interactMode = GraphInteractMode.NOINTERACTION
        self._mouseStatus = MouseStatus.RELEASED

        return
    
    def do_add_picker(self):
        """ Decide to add the picker 
        """
        if self._interactMode != GraphInteractMode.SELECTPOINTMID:
            raise NotImplementedError('Interaction mode must be SELECTPOINTMID.')

        self._interactMode = GraphInteractMode.SELECTPOINTNEW
        
        return
    
    def do_enter_pick_mode(self):
        """Enter interaction/selection mode
        """
        # Check current status
        if self._interactMode != GraphInteractMode.NOINTERACTION:
            raise NotImplementedError('Interaction mode is not NONITERACTION.  Operation invalid.')
        
        self._interactMode = GraphInteractMode.SELECTPOINTNEW
        
        return
    
    def do_leave_interact_mode(self):
        """
        """
        self._interactMode = GraphInteractMode.NOINTERACTION
        print "[DB] Mode is set back to NONITERACTION"
    
    def do_move_picker_left(self):
        """ Move picker line left by 1 step 
        """
        if self._interactMode != GraphInteractMode.SELECTPOINTMID:
            raise NotImplementedError('Must be in state SELECTPOINTMID')
        
    def do_move_picker_right(self):
        """ Move picker line left by 1 step 
        """
        if self._interactMode != GraphInteractMode.SELECTPOINTMID:
            raise NotImplementedError('Must be in state SELECTPOINTMID')        
        

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

    def on_mousePressEvent(self, event):
        """ Respond to pick up a value with mouse down event if it is on MplGraphicsView's canvas
        Definition of button_press_event is:
          button_press_event(x, y, button, dblclick=False, guiEvent=None)
        Thus event has x, y and button.

        event.button has 3 values:
         1: left
         2: middle
         3: right
        """
        self._mouseStatus = MouseStatus.PRESSED
        
        x = event.xdata
        y = event.ydata
        button = event.button
        print "[DB] Button %d is (pressed) down."%(button)
        
        # NOTE: on Linux, button 1 is left button, buton 3 is right button

        # In case of mouse is in the canvas' region
        if x is not None and y is not None:
            if button == 1:
                msg = "You've pressed on canvas with coords:\n %f, %f\n and button %d" % (x, y, button)
                print "Button 1: ", msg
                # QtGui.QMessageBox.information(self, "Click!", msg)
                self._mouseStatus = MouseStatus.PRESSED
                
            elif button == 3:
                # right click of mouse will pop up a context-menu
                self.ui.menu = QtGui.QMenu(self) 

                addAction = QtGui.QAction('Add', self) 
                addAction.triggered.connect(self.addSomething) 
                self.ui.menu.addAction(addAction)

                rmAction = QtGui.QAction('Remove', self) 
                rmAction.triggered.connect(self.rmSomething) 
                self.ui.menu.addAction(rmAction) 
                
                # add other required actions 
                self.ui.menu.popup(QtGui.QCursor.pos())

        return
    
    def on_mouseReleaseEvent(self, event):
        """
        """
        self._mouseStatus = MouseStatus.RELEASED
        
        print "Released... "
        
        x = event.xdata
        y = event.ydata
        button = event.button
        
        msg = "You've released mouse button %d @ (%.5f, %.5f)" % (button, x, y)
        print msg
        
        return
        
        if self._interactMode == GraphInteractMode.SELECTPOINTNEW:
            self._do_add_picker(x, y)
        elif self._interactMode == GraphInteractMode.SELECTPOINTMID:
            self._do_move_picker(x, y)          
        
      
        

    def on_mouseMotion(self, event):
        """
        """
        # print "Mouse is moving to ", event.xdata, event.ydata

        return


    def addSomething(self):
        """
        """
        print "Add something?"

        return


    def rmSomething(self):
        """
        """
        print "Remove something?"

        return
    
    
    def _do_add_picker(self, x, y):
        """ Pick add a picker line 
        """
        # Plot 2 new lines dashed and etc. 
        self.ui.canvas.addHorizontalIndicator(y, 'blue')
        
    def _do_move_picker(self, x, y):
        """ Move the picker line
        """
        # Move 
    


if __name__ == "__main__":
    mainApp = QtGui.QApplication(sys.argv)

    myapp = MainAppNDim()
    myapp.show()

    sys.exit(mainApp.exec_())
