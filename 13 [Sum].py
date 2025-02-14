# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 09:13:30 2022

@author: Kartik
"""

def whole(n):
    if n==0:
        return 0
    else:
        return n+whole(n-1)
N = int(input())
print(whole(N))