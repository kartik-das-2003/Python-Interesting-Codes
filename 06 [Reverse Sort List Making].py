# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:48:25 2022

@author: Kartik
"""

#Reverse Sort List Making
L = [int(i) for i in input("Here Write Some Number Including Space:").split()]
L.sort()
print(L[0:3],"This Are Least 3 Numbers")
L.reverse()
print(L[0:2],"These Are Highest 2 Numbers")
