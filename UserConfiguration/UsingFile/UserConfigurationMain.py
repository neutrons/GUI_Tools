#!/usr/bin/python

# The goal of this program was to be able to restart an application and find it in the same state as when we left it

# The state of all the widgets is saved when user quit the application and are loaded automatically when the 
# application is launched


# ps: more try/catch should be added to the program but the only goal of this program was to show its funtionality

import sys, os
from PyQt4 import QtGui, QtCore, Qt
import ConfigParser

from ui_UserConfiguration import *

class Config():

    file = 'my_config.cfg'
    configPath = ''

    def __init__(self, parent=None):
        self.configPath = os.path.expanduser('~/.GUI_Tools')
        if not os.path.exists(self.configPath):
            os.mkdir(self.configPath)
            
    def load(self, parent):
        fullFileName = self.configPath + "/" + self.file
        if os.path.exists(fullFileName):
            config = ConfigParser.RawConfigParser()
            config.read(fullFileName)
            
            parent.ui.radioButton1.setChecked(False)
            parent.ui.radioButton2.setChecked(False)
            parent.ui.radioButton3.setChecked(False)
            parent.ui.radioButton4.setChecked(False)
            
            radioButtonChecked = config.getint('Section1','radioButtonChecked')
            if radioButtonChecked == 1:
                parent.ui.radioButton1.setChecked(True)
            elif radioButtonChecked == 2:
                parent.ui.radioButton2.setChecked(True)
            elif radioButtonChecked == 3:
                parent.ui.radioButton3.setChecked(True)
            else:
                parent.ui.radioButton4.setChecked(True)
                
            checkbox1Checked = config.getboolean('Section1','checkbox1Checked')
            parent.ui.checkBox1.setChecked(checkbox1Checked)
            checkbox2Checked = config.getboolean('Section1','checkbox2Checked')
            parent.ui.checkBox2.setChecked(checkbox2Checked)
            checkbox3Checked = config.getboolean('Section1','checkbox3Checked')
            parent.ui.checkBox3.setChecked(checkbox3Checked)
            
            text = config.get('Section2','textEdit')
            parent.ui.textEdit.setText(text)


    def save(self, parent):
        fullFileName = self.configPath + "/" + self.file
        
        # which radiobutton is checked
        radiobuttonChecked = -1
        if parent.ui.radioButton1.isChecked():
            radiobuttonChecked = 1
        elif parent.ui.radioButton2.isChecked():
            radiobuttonChecked = 2
        elif parent.ui.radioButton3.isChecked():
            radiobuttonChecked = 3
        else:
            radiobuttonChecked = 4
            
        config = ConfigParser.RawConfigParser()
        config.add_section('Section1')
        config.set('Section1','radioButtonChecked', str(radiobuttonChecked))
        
        # checkboxes
        checkbox1Checked = False
        if parent.ui.checkBox1.isChecked():
            checkbox1Checked = True
        checkbox2Checked = False
        if parent.ui.checkBox2.isChecked():
            checkbox2Checked = True
        checkbox3Checked = False
        if parent.ui.checkBox3.isChecked():
            checkbox3Checked = True
        
        config.set('Section1','checkBox1Checked', str(checkbox1Checked))
        config.set('Section1','checkBox2Checked', str(checkbox2Checked))
        config.set('Section1','checkBox3Checked', str(checkbox3Checked))

        # text field
        text = parent.ui.textEdit.toPlainText()
        config.add_section('Section2')
        config.set('Section2','textEdit',text)
            
        with open(fullFileName, 'wb') as configFile:
            config.write(configFile)


class UserConfiguration(QtGui.QMainWindow):

    _config = None

    #initialize app
    def __init__(self, parent=None):
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle("User Configuration Main")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initGui()

    def initGui(self):
        self._config = Config()
        self._config.load(self)
        
    def saveGui(self):
        self._config.save(self)

    def closeEvent(self, event=None):
        self.saveGui()

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = UserConfiguration()
    myapp.show()

    exit_code=app.exec_()
    sys.exit(exit_code)