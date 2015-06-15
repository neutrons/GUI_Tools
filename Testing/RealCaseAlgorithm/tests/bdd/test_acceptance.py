# -*- coding: utf-8 -*-
from lettuce import *
from nose.tools import assert_equals
import os
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from peakfinderalgorithms.file_loading_utility import loadCsvFile
from peakfinderalgorithms.peakfinderderivation import PeakFinderDerivation


@step(u'Given the easy data set "([^"]*)"')
def given_the_easy_data_set_group1(step, group1):
    [world.xdata, world.ydata, world.edata] = loadCsvFile(group1)

@step(u'Then the peak range should be "([^"]*)" and "([^"]*)"')
def then_the_peak_range_should_be_group1_and_group2(step, group1, group2):
    peakfinder1 = PeakFinderDerivation(world.xdata, world.ydata, world.edata)
    peaks = peakfinder1.getPeaks()
    assert_equals(peaks, [int(group1), int(group2)])


## using Morelia
#import unittest
#from morelia import run
#import os
#import sys
#from os import path
#sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
#from peakfinderalgorithms.file_loading_utility import loadCsvFile
#from peakfinderalgorithms.peakfinderderivation import PeakFinderDerivation

#class PeakFinderTestCase(unittest.TestCase):
    
    #def test_peak_finder(self):
        #""" peak finder feature """
        #filename = os.path.join(os.path.dirname(__file__), 'peakfinder.feature')
        #run(filename, self, verbose=True, show_all_missing=True)
        
    #def step_the_easy_data_set_tests_data_easy_data_set_csv(self, tests_data_easy_data_set_csv):
        #r'the easy data set "([^"]+)"'
        #[self.xdata, self.ydata, self.edata] = loadCsvFile(tests_data_easy_data_set_csv)
    
    #def step_the_peak_range_should_be_number_and_number(self, number1, number2):
        #r'the peak range should be "([^"]+)" and "([^"]+)"'
        #peakfinder1 = PeakFinderDerivation(self.xdata, self.ydata, self.edata)
        #peaks = peakfinder1.getPeaks()
        #self.assertEqual(peaks, [int(number1), int(number2)])




    