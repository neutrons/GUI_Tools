import unittest
from exporttext import ExportText
from mock import MagicMock, patch
from PyQt4.QtGui import QFileDialog

class ExportText_test(unittest.TestCase):
    
    def setUp(self):
        self.input_text = '-> first line\n-> secondline\n-> third line\n-> \n-> last line'
        self.filename = 'remove_me.txt'
    
    def test_getfilename(self):
        '''Assert filename is correctly retrieved'''
        parent = MagicMock()
        parent.ui.textEditBottom = MagicMock(toPlainText = lambda: self.input_text)
        _my_object = ExportText(parent=parent)
        _my_object.filename = self.filename
        self.assertEqual(_my_object.filename, self.filename)
        
    def test_retrieveBottomText(self):
        '''Assert bottom text is correctly retrieved'''
        parent = MagicMock()
        parent.ui.textEditBottom = MagicMock(toPlainText = lambda: self.input_text)
        _my_object = ExportText(parent=parent)
        _my_object.filename = self.filename
        self.assertEqual(_my_object.input_text, self.input_text)
    
    #@patch('exporttext.ExportText.createAsciiFile', MagicMock(return_value=True))
    #def test_exportToFile(self):
        #mock_createAsciiFile = MagicMock()
        #mock_createAsciiFile.return_value(True)
        #with patch('exporttext.createAsciiFile') as mock_createAsciiFile:
            #parent = MagicMock()
            #parent.ui.textEditBottom = MagicMock(toPlainText = lambda: self.input_text)
            #_my_object = ExportText(parent=parent)
        
    
if __name__ == '__main__':
    unittest.main()
    