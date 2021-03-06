import unittest
if __package__ == None:
    import sys
    from os import path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from multiplicator import Multiplicator

class TestMultiplicatorClassAbove(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_list_by_number(self):
        multi1 = Multiplicator([3,4],2)
        self.assertEqual(multi1.result, [6,8])
        
#if __name__ == '__main__':
    #unittest.main()
    
suite=unittest.TestLoader().loadTestsFromTestCase(TestMultiplicatorClassAbove)
