import unittest
from multiplicator import Multiplicator

class TestMultiplicator(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_list_by_number(self):
        multi1 = Multiplicator([3,4],2)
        self.assertEqual(multi1.result, [6,8])
        
if __name__ == '__main__':
    unittest.main()