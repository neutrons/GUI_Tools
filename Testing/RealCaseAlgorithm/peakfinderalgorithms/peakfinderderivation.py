''' Example of full algorithm to test pyling, nosetests '''
import numpy as np
import math

class PeakFinderDerivation(object): #pylint: disable=R0902
    ''' This algorithm calculate the peak min and max value of a given
    data set '''

    def __init__(self, xdata, ydata, edata=None):
        self.init_arrays()

        self.xdata = np.array(xdata) #pylint: disable=E1101
        self.ydata = np.array(ydata) #pylint: disable=E1101
        self.edata = np.array(edata) #pylint: disable=E1101

        self.calculate_5_highest_points() #step2
        self.calculate_peak_pixel() #step3

        self.calculate_first_derivative() #step4
        self.calculate_min_max_derivative_pixels() #step5
        self.calculate_avg_and_std_derivative() #step6
        self.calculate_min_max_signal_pixel() #step7

    def init_arrays(self):
        ''' initialize the arrays '''
        self.xdata_firstderi = []
        self.ydata_firstderi = []
        self.edata_firstderi = []
        self.peaks = [-1, -1]
        self.five_highest_ydata = []
        self.five_highest_xdata = []
        self.sum_five_highest_ydata = -1
        self.peak_pixel = -1
        self.deri_min = 1
        self.deri_max = -1
        self.deri_min_pixel_value = -1
        self.deri_max_pixel_value = -1
        self.mean_counts_firstderi = -1
        self.std_deviation_counts_firstderi = -1
        self.peak_max_final_value = -1
        self.peak_min_final_value = -1

    def calculate_5_highest_points(self):
        ''' find the 5 highest points of the data set '''
        _xdata = self.xdata
        _ydata = self.ydata

        _sort_ydata = np.sort(_ydata) #pylint: disable=E1101
        _decreasing_sort_ydata = _sort_ydata[::-1]
        self.five_highest_ydata = _decreasing_sort_ydata[0:5]

        _sort_index = np.argsort(_ydata) #pylint: disable=E1101
        _decreasing_sort_index = _sort_index[::-1]
        _5decreasing_sort_index = _decreasing_sort_index[0:5]
        self.five_highest_xdata = _xdata[_5decreasing_sort_index]

    def calculate_peak_pixel(self):
        ''' sum (x1y1 + x2y2 + x3y3 + x4y4 + x5y5) / (y1+y2+y3+y4+y5) '''
        self.sum_peak_counts = sum(self.five_highest_ydata)
        _sum_peak_counts_time_pixel = -1
        for index, yvalue in enumerate(self.five_highest_ydata):
            _sum_peak_counts_time_pixel += yvalue * self.five_highest_xdata[index]
        self.sum_peak_counts_time_pixel = _sum_peak_counts_time_pixel
        self.peak_pixel = round(self.sum_peak_counts_time_pixel / self.sum_peak_counts)

    def calculate_first_derivative(self):
        ''' calculate first derivative '''
        xdata = self.xdata
        ydata = self.ydata

        _xdata_firstderi = []
        _ydata_firstderi = []
        for i in range(len(xdata)-1):
            _left_x = xdata[i]
            _right_x = xdata[i+1]
            _xdata_firstderi.append(np.mean([_left_x, _right_x])) #pylint: disable=E1101

            _left_y = ydata[i]
            _right_y = ydata[i+1]
            _ydata_firstderi.append((_right_y - _left_y)/(_right_x - _left_x))

        self.xdata_firstderi = _xdata_firstderi
        self.ydata_firstderi = _ydata_firstderi

    def calculate_min_max_derivative_pixels(self): #pylint: disable=C0103
        ''' get min and max derivative values '''
        _pixel = self.xdata_firstderi
        _counts_firstderi = self.ydata_firstderi

        _sort_counts_firstderi = np.sort(_counts_firstderi) #pylint: disable=E1101
        self.deri_min = _sort_counts_firstderi[0]
        self.deri_max = _sort_counts_firstderi[-1]

        _sort_index = np.argsort(_counts_firstderi) #pylint: disable=E1101
        self.deri_min_pixel_value = min([_pixel[_sort_index[0]], _pixel[_sort_index[-1]]])
        self.deri_max_pixel_value = max([_pixel[_sort_index[0]], _pixel[_sort_index[-1]]])

    def calculate_avg_and_std_derivative(self): #pylint: disable=C0103
        ''' average and standard derivation of first derivative '''
        _counts_firstderi = np.array(self.ydata_firstderi) #pylint: disable=E1101
        self.mean_counts_firstderi = np.mean(_counts_firstderi) #pylint: disable=E1101
        _mean_counts_firstderi = np.mean(_counts_firstderi * _counts_firstderi) #pylint: disable=E1101
        self.std_deviation_counts_firstderi = math.sqrt(_mean_counts_firstderi)

    def calculate_min_max_signal_pixel(self):
        ''' min and max signal pixel '''
        _counts = self.ydata_firstderi
        _pixel = self.xdata_firstderi

        _deri_min_pixel_value = self.deri_min_pixel_value
        _deri_max_pixel_value = self.deri_max_pixel_value

        _std_deviation_counts_firstderi = self.std_deviation_counts_firstderi

        px_offset = 0
        while abs(_counts[int(_deri_min_pixel_value - px_offset)]) > \
              _std_deviation_counts_firstderi:
            px_offset += 1
        _peak_min_final_value = _pixel[int(_deri_min_pixel_value - px_offset)]

        px_offset = 0
        while abs(_counts[int(round(_deri_max_pixel_value + px_offset))]) > \
              _std_deviation_counts_firstderi:
            px_offset += 1
        _peak_max_final_value = _pixel[int(round(_deri_max_pixel_value + px_offset))]

        self.peaks = [int(_peak_min_final_value), int(np.ceil(_peak_max_final_value))] #pylint: disable=E1101

#if __name__ == "__main__":
    #from file_loading_utility import loadCsvFile
    #[xdata, ydata, edata] = loadCsvFile('easy_data_set.csv')
    #peakfinder1 = PeakFinderDerivation(xdata, ydata, edata)
    #[high_x, high_y] = peakfinder1.get5HighestPoints()
    