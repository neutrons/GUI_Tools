#!/usr/bin/python
# -*- coding: utf-8 -*-

#import utility modules
import sys, os
import inspect

#import PyQt modules
from PyQt4 import QtGui, QtCore, Qt


#include this try/except block to remap QString needed when using IPython
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    


#import GUI components generated from Qt Designer .ui file
from ui_TestTranslate import *

class TestTranslate(QtGui.QMainWindow):
    
    #initialize app
    def __init__(self, parent=None):
        super(TestTranslate,self).__init__(parent)
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow() #defined in ui_AppTemplate.py
        self.ui.setupUi(self)
        self.setWindowTitle("Test Translation")
    
        #add action exit for File --> Exit menu option
        self.connect(self.ui.actionExit, QtCore.SIGNAL('triggered()'), self.confirmExit)
        
        #add actions for language translation:
        self.connect(self.ui.actionEnglish, QtCore.SIGNAL('triggered()'), self.english)
        self.connect(self.ui.actionFrench, QtCore.SIGNAL('triggered()'), self.french)        
        self.connect(self.ui.actionSpanish, QtCore.SIGNAL('triggered()'), self.spanish)
        self.connect(self.ui.actionChinese, QtCore.SIGNAL('triggered()'), self.chinese)
                
        #add signal/slot connection for pushbutton exit request
        #self.connect(self.ui.pushButtonExit, QtCore.SIGNAL('clicked()'), self.confirmExit)
        
        
        qmFiles = self.findQmFiles()
        print "qmFiles: ",qmFiles
        self.ui.qmFiles=qmFiles
        
        
    def english(self):
        srch='_en.qm'
        self.doTranslate(srch)


    def french(self):
        srch='_fr.qm'
        self.doTranslate(srch)
        
    def spanish(self):
        srch='_sp.qm'
        self.doTranslate(srch)
        
    def chinese(self):
        srch='_cn.qm'
        self.doTranslate(srch)
        
    def doTranslate(self,srch):
        
        indx=-1
        for cntr,qmFile in enumerate(self.ui.qmFiles):
            if srch in qmFile:
                indx=cntr
        print "indx: ",indx
        if indx==-1:
            #don't translate if translation file not found
            return

        pass        
        qmFile=self.ui.qmFiles[indx]
        print "qmFile: ",qmFile
        obj=self.ui.centralwidget.children()
        
        translator = QtCore.QTranslator() 
        print "Loaded qmFile: ",qmFile
        translator.load(qmFile)
        stat2=QtGui.qApp.installTranslator(translator)
        
        self.ui.retranslateUi(self)        
        self.setWindowTitle(QtGui.QApplication.translate("Test","Hello World!"))
        
    def findQmFiles(self):
        trans_dir = QtCore.QDir('translations')
        #trans_dir = QtCore.QDir('C:/Python27/Lib/site-packages/PyQt4/examples/tools/i18n/translations')

        entryList=trans_dir.entryList(['*.qm'], QtCore.QDir.Files,QtCore.QDir.Name)
        fileNames = trans_dir.entryList(['*.qm'], QtCore.QDir.Files,
                QtCore.QDir.Name)

        return [trans_dir.filePath(fn) for fn in fileNames]
        
                
    def confirmExit(self):
        reply = QtGui.QMessageBox.question(self, 'Message',
        "Are you sure to quit?", QtGui.QMessageBox.Yes | 
        QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        
        if reply == QtGui.QMessageBox.Yes:
        #close application
            self.close()
        else:
        #do nothing and return
            pass     

    
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = TestTranslate()
    myapp.show()

    exit_code=app.exec_()
    #print "exit code: ",exit_code
    sys.exit(exit_code)