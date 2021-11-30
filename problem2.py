#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:34:28 2021

@author: kolliabhishek
"""

"""new program to find GCD"""
def greatest_common_divisor(a,b):
    """" takes two integers as input and returns the greatest common divisor"""
    if b==0:
        return a
    else:
        remainder = a%b
        return greatest_common_divisor(b, remainder)

def is_number(userinput):
    """ takes input and checks whether it is a positivve integer or not and returns True or false"""
    try:
        if int(userinput) > 0:
            return True
    except:
        return False

def input_to_number(userinput):
    number = None
    if is_number(userinput):
        number = int(userinput)
    return number

if __name__ == "__main__":
    a= input("enter the large number first: ")
    b= input("enter the second number: ")
    if is_number(a) and is_number(b):
        gcd = greatest_common_divisor(input_to_number(a), input_to_number(b))
        statement = "The gcd of the numbers is {}".format(gcd)
    else:
        statement = "Please enter valid input"
    
    print(statement)