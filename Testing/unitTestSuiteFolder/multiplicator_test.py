import unittest
from multiplicator import Multiplicator

class TestMultiplicator(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_list_by_number(self):
        multi1 = Multiplicator([3,4],2)
        self.assertEqual(multi1.result, [6,8])
        

    def test_list_by_list(self):
        multi2 = Multiplicator([3,4],[10,11])
        self.assertEqual(multi2.result, [30,44])


suite=unittest.TestLoader().loadTestsFromTestCase(TestMultiplicator)
        