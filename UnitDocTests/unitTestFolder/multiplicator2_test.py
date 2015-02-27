import unittest
from multiplicator import Multiplicator

class TestMultiplicator2(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_list_by_list(self):
        multi2 = Multiplicator([3,4],[10,11])
        self.assertEqual(multi2.result, [30,44])

if __name__ == '__main__':
    unittest.main()
    
    