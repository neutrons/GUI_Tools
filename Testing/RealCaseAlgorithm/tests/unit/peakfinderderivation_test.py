import unittest
import os
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from peakfinderalgorithms.peakfinderderivation import PeakFinderDerivation
from peakfinderalgorithms.file_loading_utility import load_csv_file

class TestPeakFinderDerivation(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_load_csv_file_xaxis(self):
        '''Step1 - Loading: checking that load_csv_file works correctly on xaxis'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        xdata10 = xdata[0:10]
        self.assertEqual(xdata10, [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
    
    def test_load_csv_file_yaxis(self):
        '''Step1 - Loading: checking that load_csv_file works correctly on yaxis'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        ydata10 = ydata[0:10]
        self.assertEqual(ydata10, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 5.0])

    def test_load_csv_file_eaxis(self):
        '''Step1 - Loading: checking that load_csv_file works correctly on eaxis'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        edata10 = edata[0:10]
        self.assertEqual(edata10, [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.236067977])

    def test_get5HighestPoints_xdata(self):
        '''Step2 - 5highest points: using run 125682 to check calculation of 5 highest points - xdata '''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder1 = PeakFinderDerivation(xdata, ydata, edata)
        high_x = peakfinder1.five_highest_xdata
        high_x = high_x.tolist()
        self.assertEqual(high_x, [155., 156., 154., 157., 153.])
        
    def test_get5HighestPoints_ydata(self):
        '''Step2 - 5highest points: using run 125682 to check calculation of 5 highest points - ydata '''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder1 = PeakFinderDerivation(xdata, ydata, edata)
        high_y = peakfinder1.five_highest_ydata
        high_y = high_y.tolist()
        self.assertEqual(high_y, [32351., 28999., 19351., 9503., 2796.])

    def test_calculatePeakPixel_sumPeakCounts(self):
        '''Step3 - calculate peak pixel using run 125682 to check calculation of 5 highest points - sum_xdata '''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder1 = PeakFinderDerivation(xdata, ydata, edata)
        sum_five_highest_xdata = peakfinder1.sum_peak_counts
        self.assertEqual(sum_five_highest_xdata, 93000.0)

    def test_calcuatePeakPixel_sumPeakCountTimePixel(self):
        '''Step3 - calculate peak pixel using run 125682 to check calculation of 5 highest points - sum_ydata '''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder1 = PeakFinderDerivation(xdata, ydata, edata)
        sum_five_highest_ydata = peakfinder1.sum_peak_counts_time_pixel
        self.assertEqual(sum_five_highest_ydata, 14438061.0)

    def test_calculatePeakPixel_peakPixelValue(self):
        '''Step3 - calculate peak pixel value using run 125682'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder1 = PeakFinderDerivation(xdata, ydata, edata)
        peak_pixel = peakfinder1.peak_pixel
        self.assertEqual(peak_pixel, 155.0)

    def test_calculatefirstderivative_xaxis(self):
        '''Step4 - derivative: testing the first derivative calculation - axis x'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder = PeakFinderDerivation(xdata, ydata, edata)
        [xdata_first, ydata_first] = [peakfinder.xdata_firstderi, peakfinder.ydata_firstderi]
        xdata10= xdata_first[0:10]
        self.assertEqual(xdata10, [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5])
    
    def test_calculatefirstderivative_yaxis(self):
        '''Step4 - derivative: testing the first derivative calculation - axis y'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder = PeakFinderDerivation(xdata, ydata, edata)
        [xdata_first, ydata_first] = [peakfinder.xdata_firstderi, peakfinder.ydata_firstderi]
        ydata10= ydata_first[0:10]
        self.assertEqual(ydata10, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 1.0, -1.0])

    def test_calculateMinMaxDervativePixels_minValue(self):
        '''Step5 - calculate min derivative counts value'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder = PeakFinderDerivation(xdata, ydata, edata)
        min_derivative_value = peakfinder.deri_min
        self.assertEqual(min_derivative_value, -19496.0)

    def test_calculateMinMaxDervativePixels_maxValue(self):
        '''Step5 - calculate max derivative counts value'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder = PeakFinderDerivation(xdata, ydata, edata)
        max_derivative_value = peakfinder.deri_max
        self.assertEqual(max_derivative_value, 16555.0)

    def test_calculateMinMaxDervativePixels_minPixelValue(self):
        '''Step5 - calculate pixel of min derivative counts value'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder = PeakFinderDerivation(xdata, ydata, edata)
        min_pixel_derivative_value = peakfinder.deri_min_pixel_value
        self.assertEqual(min_pixel_derivative_value, 153.5)

    def test_calculateMinMaxDervativePixels_maxPixelValue(self):
        '''Step5 - calculate pixel of max derivative counts value'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder = PeakFinderDerivation(xdata, ydata, edata)
        max_pixel_derivative_value = peakfinder.deri_max_pixel_value
        self.assertEqual(max_pixel_derivative_value, 156.5)

    def test_calculateAvgAndStdDerivation_mean_counts_firstderi(self):
        '''Step6 - calculate average of first derivation counts'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder = PeakFinderDerivation(xdata, ydata, edata)
        mean_counts_firstderi = peakfinder.mean_counts_firstderi
        self.assertEqual(mean_counts_firstderi, 0)

    def test_calculateAvgAndStdDerivation_std_deviation_counts_firstderi(self):
        '''Step6 - calculate standard deviation of first derivation counts'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder = PeakFinderDerivation(xdata, ydata, edata)
        std_deviation_counts_firstderi = peakfinder.std_deviation_counts_firstderi
        self.assertAlmostEqual(std_deviation_counts_firstderi, 1741.838, delta=0.001)

    def test_case_easy_data_set(self):
        '''Step7 - calculate final peak range using run 125682 (easy data set)'''
        [xdata, ydata, edata] = load_csv_file('tests/data/easy_data_set.csv')
        peakfinder1 = PeakFinderDerivation(xdata, ydata, edata)
        peaks = peakfinder1.peaks
        self.assertEqual(peaks, [151, 159])
    
    def test_case_medium_data_set(self):
        '''Step7 - calculate final peak range using run 124211 (medium data set)'''
        [xdata, ydata, edata] = load_csv_file('tests/data/medium_data_set.csv')
        peakfinder1 = PeakFinderDerivation(xdata, ydata, edata)
        peaks = peakfinder1.peaks
        self.assertEqual(peaks, [151, 159])
    
    def test_case_hard_data_set(self):
        '''Step7 - calculate final peak range using run 124135 (hard data set)'''
        [xdata, ydata, edata] = load_csv_file('tests/data/hard_data_set.csv')
        peakfinder1 = PeakFinderDerivation(xdata, ydata, edata)
        peaks = peakfinder1.peaks
        self.assertEqual(peaks, [145,164])
    
if __name__ == '__main__':
    unittest.main()