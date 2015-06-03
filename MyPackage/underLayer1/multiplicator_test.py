import unittest
from underFolder.multiplicator import Multiplicator

class TestMultiplicator(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_list_by_number(self):
        '''This message will be displayed if this test fails'''
        multi1 = Multiplicator([3,4],2)
        self.assertEqual(multi1.result, [6,8])
        
    def test_list_by_list(self):
        '''explain here what this test is doing'''
        multi2 = Multiplicator([3,4],[10,11])
        self.assertEqual(multi2.result, [30,44])
        
    def test_missing_one_argument_exception_thrown(self):
        '''tell here what we are doing in this test'''
        self.assertRaises(TypeError, Multiplicator([10,11]))

suite=unittest.TestLoader().loadTestsFromTestCase(TestMultiplicator)

        