from PyQt4.QtGui import QFileDialog
import os

class ExportText(object):
    
    def __init__(self, parent=None):
        self.parent = parent
        
    def retrieveBottomText(self):
        self.input_text = str(self.parent.ui.textEditBottom.toPlainText())

    def getFilename(self):
        self.filename = QFileDialog.getSaveFileName(self.parent, "Select file name", "", "ASCII (*.txt)")

    def exportToFile(self):
        if not str(self.filename):
            return
        
        text_array = self.input_text.split('\n')
        new_text = [str(text) for text in text_array]
        new_text = '\n'.join(new_text)
        self.export_status = self.createAsciiFile(self.filename, new_text)
        
    def createAsciiFile(self, filename, str_list):
        _status = True
        try:
            if os.path.isfile(filename):
                os.remove(filename)
            f = open(filename,'w')
            for _line in str_list:
                f.write(_line)
        except:
            _status = False
        finally:
            f.close()    
        
        