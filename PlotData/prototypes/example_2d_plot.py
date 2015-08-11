import matplotlib
if matplotlib.get_backend() != 'QT4Agg':
    matplotlib.use('QT4Agg')
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar

import matplotlib.pyplot as plt
import numpy as np

import time

#create figure
# fig=plt.figure()
#define image x and y size
Nx=500
Ny=600
#turn on interactive plotting (makes figures non-blocking)
plt.ion()
img_data = np.random.normal(size=(Nx, Ny)) #create image data
plt.imshow(img_data,cmap='gray',extent=[0,Nx,0,Ny]) #show image data to a specific extent
plt.hold(True) #hold for the plot
plt.plot(range(Nx/2),color='r') #show line plot in red
plt.hold(False) #disable plot hold
plt.pause(0.0001) #seems that a very short delay is necessary for plot to function properly in this mode
#plt.draw()


time.sleep(3)

img_data = np.random.normal(size=(Nx, Ny))
plt.imshow(img_data,cmap='gray',extent=[0,Nx,0,Ny])
plt.hold(True)
plt.plot(range(Nx))
plt.hold(False)
plt.pause(0.0001)
time.sleep(3)
plt.clf()
plt.pause(0.0001)
time.sleep(3)
#plt.draw()


