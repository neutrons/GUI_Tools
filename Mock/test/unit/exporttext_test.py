import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from myMock.exporttext import ExportText
from mock import MagicMock, patch
from PyQt4.QtGui import QFileDialog
from PyQt4 import QtGui

class ExportText_test(unittest.TestCase):
    
    def setUp(self):
        self.input_text = '-> first line\n-> secondline\n-> third line\n-> \n-> last line'
        self.filename = '/top/users/remove_me.txt'
    
    def test_retrieve_bottom_text(self):
        '''Assert bottom text is correctly retrieved'''
        parent = MagicMock()
        parent.ui.textEditBottom = MagicMock(toPlainText = lambda: self.input_text)
        _my_object = ExportText(parent=parent)
        _my_object.retrieveBottomText()
        _my_object.filename = self.filename
        self.assertEqual(_my_object.input_text, self.input_text)
    
    def test_retrieve_output_filename_method1(self):
        with patch('PyQt4.QtGui.QFileDialog.getSaveFileName', MagicMock(return_value=self.filename)) as mock:
            parent = MagicMock()
            _my_object = ExportText(parent=parent)
            _my_object.getFilename()
            self.assertEqual(self.filename, _my_object.filename)
            
    @patch('PyQt4.QtGui.QFileDialog.getSaveFileName', MagicMock(return_value='/top/users/remove_me.txt')) 
    def test_retrieve_output_filename_method2(self):
        '''assert using global path to QFileDialog'''
        parent = MagicMock()
        _my_object = ExportText(parent=parent)
        _my_object.getFilename()
        self.assertEqual(self.filename, _my_object.filename)
    
    @patch('myMock.exporttext.QFileDialog.getSaveFileName', MagicMock(return_value='/top/users/remove_me.txt')) 
    def test_retrieve_output_filename_method3(self):
        '''assert using package path to QFileDialog'''
        parent = MagicMock()
        _my_object = ExportText(parent=parent)
        _my_object.getFilename()
        self.assertEqual(self.filename, _my_object.filename)

    def test_export_file(self):
        with patch('myMock.exporttext.ExportText.createAsciiFile', MagicMock(return_value=True)) as mock:
            parent = MagicMock()
            _my_object = ExportText(parent=parent)
            _my_object.input_text = self.input_text
            _my_object.filename = self.filename
            _my_object.exportToFile()
            self.assertEqual(_my_object.export_status, True)
            
if __name__ == '__main__':
    unittest.main()
    