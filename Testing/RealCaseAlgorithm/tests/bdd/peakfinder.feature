Feature: peak finder
    Using secondary derivation 
    and using a data set
    this program will return the location
    of the peak by giving
    peak_min and peak_max
    
Scenario: locate peak for easy data set
    Given the easy data set "tests/data/easy_data_set.csv"
    Then the peak range should be "151" and "159"
    
    