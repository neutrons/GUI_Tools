from PyQt4 import QtCore
import time

class AThread(QtCore.QThread):

    top_gui = None
    def setUpGui(self, top_gui):
        self.top_gui = top_gui
    
    def run(self):
        self.top_gui.ui.textEdit.append('Starting AThread')
        count = 0
        for i in range(5):
            time.sleep(2)
            self.top_gui.ui.textEdit.append("thread method 1, index %d" %i)
            