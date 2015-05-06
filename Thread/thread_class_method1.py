from PyQt4 import QtCore
import time

class AThread(QtCore.QThread):

    top_gui = None
    thread_index = 1
    
    def setUpGui(self, top_gui, thread_index):
        self.top_gui = top_gui
        self.thread_index = thread_index
    
    def run(self):
        self.top_gui.ui.textEdit.append('Starting AThread')
        count = 0
        for i in range(5):
            time.sleep(2)
            self.top_gui.ui.textEdit.append("thread method %d, index %d" %(self.thread_index,i))
            