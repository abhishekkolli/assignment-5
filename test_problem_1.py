#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 19:06:52 2021

@author: kollisrivenkataphaniabhishek
"""

import problem_1
import pytest

def test_is_number_success():
    assert problem_1.is_number("32") == True
    assert problem_1.is_number("0") == True
    assert problem_1.is_number("-1.00") == True
def test_is_number_failures():
    assert problem_1.is_number("something") == False
    assert problem_1.is_number("") == False
def test_input_to_number():
    assert problem_1.input_to_number("32") == 32
    assert problem_1.input_to_number("-0.00") == 0
def temp_conversion():
    assert problem_1.temp_c_to_temp_f("32") == 0
    assert problem_1.temp_c_to_temp_f("1") == -17.22
    
pytest.main()