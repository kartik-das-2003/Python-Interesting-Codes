# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:32:09 2022

@author: Kartik
"""

n=int(input("Write:"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
