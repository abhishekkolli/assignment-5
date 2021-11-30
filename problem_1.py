#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 18:56:21 2021

@author: kollisrivenkataphaniabhishek
"""

def is_number(string):
    """evaluates if a entered input is number and it returns True or False"""
    try:
        number = float(string)
        return True
    except:
        return False

def input_to_number(userinput):
    """convert userinput to a number returns a float or None"""
    number = None
    if is_number(userinput):
        number = float(userinput)
    return number

def temp_f_to_temp_c(temperature):
    """convert a f to c returns: Float to 2 decimals"""
    temp_c = (temperature - 32)/1.8
    return round(temp_c,2)


if __name__ == "__main__":
    userinput = input("Enter the temperature in Fahrenheit: ")
    if is_number(userinput):
        temp_f = input_to_number(userinput)
        temp_c = temp_f_to_temp_c(temp_f)
        statement = "The temperature in celsius is {}" .format(temp_c)
    else:
        statement = "please enter valid input"
        
    print(statement)

