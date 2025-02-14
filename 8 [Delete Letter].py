# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 22:19:13 2022

@author: Kartik
"""

s=input("write:")
a = 'aeiouAEIOU'
for i in s:
    if i not in a:
        print('_', end='')
        
    else:
        print(i, end='')