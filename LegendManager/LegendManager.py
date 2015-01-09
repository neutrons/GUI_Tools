#!/usr/bin/python

"""
LegendManager.py

Example Application to enable a user to edit content and display of matplotlib
plot labels.  The application creates a matplotlib.pyplot figure with three 
plots, and each plot has a label.  A basic PyQt4 GUI is presented which enables 
the user to select each label for display or not along with the ability to edit
the label text via the table in the GUI.

"""

#import utility modules
import sys

#import matplotlib to be compatible with PyQt4
import matplotlib
if matplotlib.get_backend() != 'QT4Agg':
    matplotlib.use('QT4Agg')
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar

import matplotlib.pyplot as plt

#import PyQt modules
from PyQt4 import QtGui, QtCore, Qt

#include this try/except block to remap QString needed when using IPython
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

#import GUI components generated from Qt Designer .ui file
from ui_LegendManager import *

class LegendManager(QtGui.QMainWindow):
    
    #initialize app
    def __init__(self, parent=None):
        
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle("App Template Main")
        self.ui = Ui_MainWindowLegend() #defined in ui_AppTemplate.py
        self.ui.setupUi(self)
    
        self.connect(self.ui.pushButtonSelectAll, QtCore.SIGNAL('clicked()'), self.SelectAll)
        self.connect(self.ui.pushButtonClearAll, QtCore.SIGNAL('clicked()'), self.ClearAll)
        self.connect(self.ui.pushButtonUpdatePlot, QtCore.SIGNAL('clicked()'), self.UpdatePlot)
    
        #add action exit for File --> Exit menu option
        self.connect(self.ui.pushButtonExit, QtCore.SIGNAL('clicked()'), self.Exit)
        
        
        #flag for testing and development
        doTst=True
        
        #check if we're using test plot or plot from MSlice
        if doTst:
            fig=plt.figure()
            ax=plt.subplot(111)
            #plot three lines on it
            plt.plot(range(10), label='Label 0')
            plt.plot(range(1,11), label='Label 1')
            plt.plot(range(2,12), label='Label 2')
            plt.legend()
            plt.ion()  #make plot non-blocking
            plt.show()
            
            self.ui.fig=fig
            self.ui.ax=ax
        #get handles and labels for current plots
        handles, LabLst = ax.get_legend_handles_labels()
        
        Nlabs=len(LabLst)
        #inform user if no legend labels to manage
        if Nlabs ==0:
            #case where there are no labels

            dialog=QtGui.QMessageBox(self)
            dialog.setText("There are no plot legends to manage - returning")
            dialog.exec_() 
            self.close()
            sys.exit()
        
        #Initialize table
        HzHeaders=['Label','Status']
        self.ui.tableWidgetLegend.setHorizontalHeaderLabels(HzHeaders)
        w=285
        self.ui.tableWidgetLegend.setColumnWidth(0,0.667*w) #Label
        self.ui.tableWidgetLegend.setColumnWidth(1,0.333*w) #Select Status
        self.ui.tableWidgetLegend.resizeRowsToContents()
        self.ui.tableWidgetLegend.setRowCount(Nlabs)

        #Now fill the rows
        Nrows=self.ui.tableWidgetLegend.rowCount()
        for i in range(Nrows):
            #add the labels
            item=QtGui.QTableWidgetItem()
            item.setData(QtCore.Qt.DisplayRole,LabLst[i]) 
            self.ui.tableWidgetLegend.setItem(i,0,item)
            #add the select checkboxes
            addCheckboxToWSTCell(self.ui.tableWidgetLegend,i,1,True)
            
        self.ui.tableWidgetLegend.verticalHeader().setVisible(False)
        

        
    def SelectAll(self):
        #Select all labels to display
        table=self.ui.tableWidgetLegend
        Nrows=table.rowCount()
        for i in range(Nrows):
            addCheckboxToWSTCell(table,i,1,True)
                
        
    def ClearAll(self):
        #Select no labels to display
        table=self.ui.tableWidgetLegend
        Nrows=table.rowCount()
        for i in range(Nrows):
            addCheckboxToWSTCell(table,i,1,False)
        
    def UpdatePlot(self):
        #Check the table for new label text and for which labels to show
        #Then put this new legend on the plot
        table=self.ui.tableWidgetLegend
        ax=self.ui.ax
        #code for checking which labels are selected to show
        Nrows=table.rowCount()
        selrow=[]
        handles, LabLst = ax.get_legend_handles_labels()
        for row in range(Nrows):
            #get checkbox status            
            cw=table.cellWidget(row,1) 
            #get new label text
            newLab=str(table.item(row,0).text())
            handles[row].set_label(newLab)
            
            try:
                cbstat=cw.isChecked()
                if cbstat == True:
                    #case to identify selected row number
                    selrow.append(row)
            except AttributeError:
                #case where rows have been deleted and nothing do check or do
                print "unexpected case"
        
        #show selected labels
        Nshow=len(selrow)
        
        if Nshow > 0:
            #show new legend if there's something to show
            handles, LabLst = ax.get_legend_handles_labels()
            newHand=[]
            newLab=[]
            if Nshow > 0:
                for i in range(Nshow):
                    newHand.append(handles[selrow[i]])
                    newLab.append(LabLst[selrow[i]])
                    plt.legend(newHand,newLab)
        else:
            #take the legend off of the plot
            plt.legend([],[])
            ax.legend_=None
        
    def Exit(self):
        #Exit application
        self.close()

def addCheckboxToWSTCell(table,row,col,state):
    
    if state == '':
        state=False
    
    checkbox = QtGui.QCheckBox()
    checkbox.setText('Select')
    checkbox.setChecked(state)
    
    #adding a widget which will be inserted into the table cell
    #then centering the checkbox within this widget which in turn,
    #centers it within the table column :-)
    QW=QtGui.QWidget()
    cbLayout=QtGui.QHBoxLayout(QW)
    cbLayout.addWidget(checkbox)
    cbLayout.setAlignment(QtCore.Qt.AlignCenter)
    cbLayout.setContentsMargins(0,0,0,0)
    
    table.setCellWidget(row,col, checkbox) #if just adding the checkbox directly
  
    
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = LegendManager()
    myapp.show()

    exit_code=app.exec_()
    #print "exit code: ",exit_code
    sys.exit(exit_code)