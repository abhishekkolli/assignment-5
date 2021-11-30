#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:50:52 2021

@author: kollisrivenkataphaniabhishek
"""

import problem6

def test_dateformat():
    assert problem6.rename("10-31-2019.jpg") == "31-10-2019.jpg"
    assert problem6.rename("10-31-2019.jpg") != "31-10-2019"
    assert problem6.rename("01-01-2014.png") == "01-01-2014.png"

if __name__ == "__main__" :
    test_dateformat()
    print(problem6.rename("1-10-2090.jpg"))