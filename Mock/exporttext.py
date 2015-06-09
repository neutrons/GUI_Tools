from PyQt4.QtGui import QFileDialog
import os

class ExportText(object):
    
    def __init__(cls, parent=None):
        cls.parent = parent
        
    def retrieveBottomText(cls):
        cls.input_text = str(cls.parent.ui.textEditBottom.toPlainText())

    def getFilename(cls):
        cls.filename = QFileDialog.getSaveFileName(cls.parent, "Select file name", "", "ASCII (*.txt)")

    def exportToFile(cls):
        if not str(cls.filename):
            return
        
        text_array = cls.input_text.split('\n')
        new_text = [str(text) for text in text_array]
        new_text = '\n'.join(new_text)
        cls.export_status = cls.createAsciiFile(cls.filename, new_text)
        
    def createAsciiFile(cls, filename, str_list):
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
        
        