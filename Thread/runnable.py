from PyQt4 import QtCore
import time

class Runnable(QtCore.QRunnable):

    top_gui = None
    def setUpGui(self, top_gui):
        self.top_gui = top_gui

    def run(self):
        self.top_gui.ui.textEdit.append('Starting QRunnable')
        count = 0
        while count < 5:
            time.sleep(2)
            self.top_gui.ui.textEdit.append("thread method 3, index %d" %count)
            count += 1
        self.top_gui.ui.textEdit.append('done with QRunnable thread!')
            