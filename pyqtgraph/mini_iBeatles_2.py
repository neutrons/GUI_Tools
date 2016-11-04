# -*- coding: utf-8 -*-
"""
Demonstrates a variety of uses for ROI. This class provides a user-adjustable
region of interest marker. It is possible to customize the layout and 
function of the scale/rotate handles in very flexible ways. 
"""

#import initExample ## Add path to library (just for examples; you do not need this)

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import glob
import pyfits
import os

# list of files
list_files = glob.glob('/Volumes/my_book_thunderbolt_duo/iBeatles/test_data/Run19_On_Load_Frame_all_COL_15MPA/Image019_[0-9]*.fits')

# data files
data = []
for _file in list_files[1000:1050]:
    assert os.path.isfile(_file)
    _hdu_list = pyfits.open(_file)
    _hdu_0 = _hdu_list[0]
    _data = np.array(_hdu_0.data)
    data.append(_data)
    _hdu_list.close()

data = data[-1]

## create GUI
app = QtGui.QApplication([])
win = QtGui.QMainWindow()
win.resize(800, 800)

#pg.mkQApp()

window = pg.GraphicsLayoutWidget()
centralwidget = QtGui.QWidget(window)
vertical_layout = QtGui.QVBoxLayout(centralwidget)

# A plot area (ViewBox + axes) for displaying the image
p1 = window.addPlot()

# Item for displaying image data
img = pg.ImageItem()
p1.addItem(img)

# Custom ROI for selecting an image region
roi = pg.ROI([50, 50], [200, 200])
roi.addScaleHandle([0.5, 1], [0.5, 0.5])
roi.addScaleHandle([0, 0.5], [0.5, 0.5])
p1.addItem(roi)
roi.setZValue(10)  # make sure ROI is drawn above image

# Isocurve drawing
#iso = pg.IsocurveItem(level=0.8, pen='g')
#iso.setParentItem(img)
#iso.setZValue(5)

# Contrast/color control
hist = pg.HistogramLUTItem()
hist.setImageItem(img)
window.addItem(hist)

# Draggable line for setting isocurve level
#isoLine = pg.InfiniteLine(angle=0, movable=True, pen='g')
#hist.vb.addItem(isoLine)
#hist.vb.setMouseEnabled(y=False) # makes user interaction a little easier
#isoLine.setValue(0.8)
#isoLine.setZValue(1000) # bring iso line above contrast controls

# Another plot area for displaying ROI data
window.nextRow()
p2 = window.addPlot(colspan=2)
p2.setMaximumHeight(250)
window.resize(800, 800)

window.show()


# Generate image data
img.setImage(data)
hist.setLevels(data.min(), data.max())

# build isocurves from smoothed data
#iso.setData(pg.gaussianFilter(data, (2, 2)))

# set position and scale of image
#img.scale(0.2, 0.2)
#img.translate(-50, 0)

# zoom to fit imageo
p1.autoRange()  


# Callbacks for handling user interaction
def updatePlot():
    print("update_plot")
    global img, roi, data, p2
    selected = roi.getArrayRegion(data, img)
    #p2.plot(selected.mean(axis=1), clear=True)


roi.sigRegionChanged.connect(updatePlot)
updatePlot()

def updateIsocurve():
    print('updating iisocurve')
    #global isoLine, iso
    #iso.setLevel(isoLine.value())

#isoLine.sigDragged.connect(updateIsocurve)













#win.setCentralWidget(centralwidget)
#win.setWindowTitle('pyqtgraph example: ROI Examples')
#win.show()






## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
