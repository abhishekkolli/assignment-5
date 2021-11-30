#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 00:13:24 2021

@author: kollisrivenkataphaniabhishek
"""

import problem7
import pytest
def test_valid_email():
    assert problem7.validating_email("johndoe@domainsample.com") == True
    assert problem7.validating_email("john.doe@domainsample.net") == True
    assert problem7.validating_email("john.doe43@domainsample.co.uk") == True
    assert problem7.validating_email("john.doe+spamfilter@domainsample.co.uk") == True
    
    assert problem7.validating_email("@domainsample.com") == False
    assert problem7.validating_email("johndoedomainsample.com") == False
    assert problem7.validating_email("john.doe@.net") == False
    assert problem7.validating_email("john.doe43@domainsample") == False

pytest.main()
if __name__ == "__main__":
    test_valid_email()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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