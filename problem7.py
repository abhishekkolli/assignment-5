#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 23:36:07 2021

@author: kollisrivenkataphaniabhishek
"""
import re

def validating_email(userinput):
    """
    

    Parameters
    ----------
    userinput : emailid
        checks whether it is valid like if the recepient name has alphabets
        numbers, special chars till it finds @ and then separates it using match1
        match 2 is similarly starts from @ to .
        match 3 is similarly starts from . in the end of match2 to the end

    Returns
    -------
    bool as all are statisfied
    

    """
    match1 = re.search(r'([A-Za-z0-9]+[.-_+])*[A-Za-z0-9]+\@', userinput)
    if match1:
        match2 = re.search(r'\@([A-Za-z0-9]+[-])*[A-Za-z0-9]+\.', userinput)
    #print(match2.group()[0:-1])
    #print(userinput[match2.span()[1]:])
        if match2:
            match3 = re.search(r'\.([a-z]+[.])*[a-z]+', userinput[match2.span()[1]-1:])
            #print(match3.group())
            if match3:
                return True
            else:
                return True
        else:
            return False
    else:
        return False
    
if __name__ == "__main__":
    userinput= "john.doe@domainsample.net"
    print(validating_email(userinput))
    


"""
johndoe@domainsample.com
john.doe@domainsample.net
john.doe43@domainsample.co.uk
john.doe+spamfilter@domainsample.co.uk
"""
"""
@domainsample.com
johndoedomainsample.com
john.doe@.net
john.doe43@domainsample
"""
