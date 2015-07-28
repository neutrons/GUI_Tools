from PyQt4 import QtCore
import time

class AThread(QtCore.QThread):

    top_gui = None
    thread_index = 1
    stop_flag = False
    pause_flag = False
    
    def setUpGui(self, top_gui, thread_index):
        self.top_gui = top_gui
        self.thread_index = thread_index
    
    def run(self):
        self.top_gui.ui.textEdit.append('Starting AThread')
        count = 0
        for i in range(5):
            if self.stop_flag:
                return
            while self.pause_flag:
                QtCore.QThread.msleep(100)
            time.sleep(2)
            self.top_gui.ui.textEdit.append("thread method %d, index %d" %(self.thread_index,i))
            
    def stop(self):
        self.top_gui.ui.textEdit.append('Stopping thread #%d' %self.thread_index);
        self.stop_flag = True
        self.top_gui.ui.pushbutton_7.setEnabled(False)
        self.top_gui.ui.pushbutton_8.setEnabled(False)
        self.top_gui.ui.pushbutton_2.setEnabled(True)
        
    def pause(self):
        if self.pause_flag:
            self.top_gui.ui.textEdit.append('Resuming thread #%d' %self.thread_index);
        else:
            self.top_gui.ui.textEdit.append('Pausing thread #%d' %self.thread_index);
        self.pause_flag = not self.pause_flag
        