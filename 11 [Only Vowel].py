# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 22:31:03 2022

@author: Kartik
"""

s = input()
a='aeiouAEIOU'

for ch in s:
    if ch not in a:
        print('_',end='')
    else:
        print(ch,end='')