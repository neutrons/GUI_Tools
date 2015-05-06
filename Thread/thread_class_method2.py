from PyQt4 import QtCore
import time

class someObject(QtCore.QObject):

    finished = QtCore.pyqtSignal()

    top_gui = None
    def setUpGui(self, top_gui):
        self.top_gui = top_gui

    def longRunning(self):
        self.top_gui.ui.textEdit.append('Starting AThread')
        count = 0
        while count < 5:
            time.sleep(2)
            self.top_gui.ui.textEdit.append("thread method 2, index %d" %count)
            count += 1
        self.finished.emit()
            