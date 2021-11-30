#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:05:27 2021

@author: kollisrivenkataphaniabhishek
"""

import problem3_my
import statistics
def test_mymodule():
    """ testing on a given set of numbers 
    median is slightly different when the length of the array is even. I take the average
    whereas the statistics takes the mid value even then"""
    test = [1,2,3,4,5,7,8,7,9,10,120]
    my_mean, my_median, my_mode, my_variance, my_std_dev = problem3_my.stats(test)
    assert my_mean == statistics.mean(test)
    assert my_mode == statistics.mode(test)
    assert my_variance == round(statistics.variance(test),2)
    assert my_std_dev == round(statistics.stdev(test),2)

if __name__ == "__main__":
    test_mymodule()