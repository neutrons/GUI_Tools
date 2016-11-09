import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

class CustomAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        return ['{:.4f}'.format(1./i) for i in values]

pg.mkQApp()

pw = pg.PlotWidget()
pw.show()
pw.setWindowTitle('pyqtgraph example: MultipleXAxes')
p1 = pw.plotItem
p1.setLabels(left='axis 1')


# Get rid of the item at the grid position where the top should be
p1.layout.removeItem(p1.getAxis('top'))
# make our own, setting the parent and orientation
caxis = CustomAxis(orientation='top', parent=p1)
caxis.setLabel('inverted')
caxis.linkToView(p1.vb)
# set the new one for internal plotitem
p1.axes['top']['item'] = caxis
# and add it to the layout
p1.layout.addItem(caxis, 1, 1)



p1.plot(np.arange(1, 7), [1,2,4,8,16,32])
#p2.addItem(pg.PlotCurveItem(1./np.arange(1, 7), [1,2,4,8,16,32], pen='b'))

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()