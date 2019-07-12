# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:00:46 2019

@author: Mahdi Kouretchian
"""

def func(c):
    array=[]
    if type(c) is str:
        array =c.lower().split()
    print(array)
    if "accounting" in array:
        return "accounting"
    else:
        return c
    
d=func('is good')