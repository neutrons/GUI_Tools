import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from unitTestFolder.multiplicator import Multiplicator

class TestMultiplicator1(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_list_by_number(self):
        multi1 = Multiplicator([3,4],2)
        self.assertEqual(multi1.result, [6,8])
        
if __name__ == '__main__':
    unittest.main()
    
    