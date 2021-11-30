#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 20:38:52 2021

@author: kollisrivenkataphaniabhishek
"""

import problem2

def test_is_number():
    assert problem2.is_number("35") == True
    assert problem2.is_number("12") == True
#    assert problem2.is_number("-12") == False
    
def test_input_to_number():
    assert problem2.input_to_number("32") == 32
#    assert problem2.input_to_number("-12") == -12
    
def test_gcd_numbers():
    assert problem2.greatest_common_divisor(12, 3) == 3
    assert problem2.greatest_common_divisor(97, 2) == 1

if __name__ == "__main__":
    test_is_number()
    test_input_to_number()
    test_gcd_numbers()
    
    
    