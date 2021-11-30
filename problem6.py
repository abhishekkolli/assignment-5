#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:26:12 2021

@author: kollisrivenkataphaniabhishek
"""
import re

def rename(string):
    """
    

    Parameters
    ----------
    string : input is string a date format MM-DD-YYYY

    Returns
    -------
    TYPE: DD-MM-YYYY

    """
    match1 = re.search(r'\d+\-',string)
    match2 = re.search(r'-\d+\-', string)
    match3 = re.search(r'-\d+\.\w+', string)
    
    return match2.group()[1:-1]+ "-" + match1.group()[0:-1]+ "-" + match3.group()[1:]
#    return match1.group()[0:-1], match2.group()[1:-1], match3.group()[1:]


if __name__ == "__main__":
    input1="12-15-2014.jpg"
    print(rename(input1))
    
    