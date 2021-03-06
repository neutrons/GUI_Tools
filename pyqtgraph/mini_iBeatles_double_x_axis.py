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



class CustomAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        return ['{:.4f}'.format(i) for i in values]


def update_bottom_plot():
    global roi, data, top_plot, general_data
    region = roi.getArraySlice(data, top_plot.imageItem)

    x0 = region[0][0].start
    x1 = region[0][0].stop
    
    y0 = region[0][1].start
    y1 = region[0][1].stop

    bragg_edge = []
    for _data in general_data:
        _sum_data = np.sum(_data[y0:y1, x0:x1])
        bragg_edge.append(_sum_data)

    bottom_plot_widget.clear()
    bottom_plot_widget.plot(bragg_edge)

#    print("Region from ({},{}) to ({},{})".format(x0,y0,x1,y1))

    #selection = roi.getArrayRegion(data, top_plot.imageItem)
    #print(np.shape(selection))
    
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

general_data = data
data = data[-1]

x_axis_1 = np.arange(len(general_data))
x_axis_2 = np.arange(len(general_data))*0.01

# create Main GUI
app = QtGui.QApplication([])
win = QtGui.QMainWindow()
win.resize(800, 800)
win.setWindowTitle('My iBeatles examples')
#top_widget = QtGui.QWidget()
top_widget = pg.GraphicsLayoutWidget()

# make plot prettier
pg.setConfigOptions(antialias=True)


win.setCentralWidget(top_widget)
I = QtGui.QVBoxLayout()
top_widget.setLayout(I)

# top pyqtgraph plot
top_plot = pg.ImageView(name='top_plot')
top_plot.ui.roiBtn.hide()
top_plot.ui.menuBtn.hide()
top_plot.setImage(data)
I.addWidget(top_plot)
roi = pg.ROI([50, 50], [200, 200])
roi.addScaleHandle([1, 1], [0, 0])
top_plot.addItem(roi)
roi.sigRegionChanged.connect(update_bottom_plot)

# bottom plot
bottom_plot_widget = pg.PlotWidget()
bottom_plot_widget.plot()
p1 = bottom_plot_widget.plotItem
p1.setLabels(left='Counts')
p1.setLabels(bottom='TOF')
#p1.setLabels(top='Lambda')

#get rid of the item at the gris position
p1.layout.removeItem(p1.getAxis('top'))
# make our own top axis
caxis = CustomAxis(orientation = 'top', parent = p1)
caxis.setLabel('Lambda_2')
caxis.linkToView(p1.vb)
p1.layout.addItem(caxis, 1, 1)

I.addWidget(bottom_plot_widget)


win.show()










## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
