import unittest
from morelia import run
import os

class CalculatorTestCase(unittest.TestCase):
    
    def test_addition(self):
        ''' Addition feature '''
        filename = os.path.join(os.path.dirname(__file__), 'calculator.feature')
        run(filename, self, verbose=True, show_all_missing=True)
        
    def step_I_have_powered_calculator_on(self):
        r'I have powered calculator on'
        self.stack = []
    
    def step_I_enter_number_into_the_calculator(self, number):
        r'I enter "([^"]+)" into the calculator'
        self.stack.append(int(number))

    def step_I_press_add(self):
        r'I press add'
        self.result = sum(self.stack)

    def step_the_result_should_be_number_on_the_screen(self, number):
        r'the result should be "([^"]+)" on the screen'
        self.assertEqual(int(number), self.result)