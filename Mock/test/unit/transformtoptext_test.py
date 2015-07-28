import unittest
from mock import MagicMock
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from myMock.transformtoptext import TransformTopText

class TransformTopText_test(unittest.TestCase):
    
    def setUp(self):
        self.input_text = 'first line\nsecondline\nthird line\n\nlast line'
        self.prefix_text = '-> '
    
    def test_retrieve_top_text_from_gui_true(self):
        parent = MagicMock()
        parent.ui.textEditTop = MagicMock(toPlainText = lambda: self.input_text)
        _my_object = TransformTopText(parent=parent)
        input_text = _my_object.input_text
        self.assertEqual(input_text, self.input_text)

    def test_retrieve_top_text_from_gui_false(self):
        parent = MagicMock()
        parent.ui.textEditTop = MagicMock(toPlainText = lambda: self.input_text)
        _my_object = TransformTopText(parent=parent)
        input_text = _my_object.input_text
        self.assertNotEqual(input_text, 'not same text')

    def test_retrieve_prefix_from_gui_true(self):
        parent = MagicMock()
        parent.ui.prefixValue = MagicMock(text = lambda: self.prefix_text)
        _my_object = TransformTopText(parent=parent)
        prefix_text = _my_object.prefix_text
        self.assertEqual(prefix_text, self.prefix_text)
        
    def test_retrieve_prefix_from_gui_false(self):
        parent = MagicMock()
        parent.ui.prefixValue = MagicMock(text = lambda: self.prefix_text)
        _my_object = TransformTopText(parent=parent)
        prefix_text = _my_object.prefix_text
        self.assertNotEqual(prefix_text, 'wrong text')

if __name__ == '__main__':
    unittest.main()
    