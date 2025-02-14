# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 08:41:53 2022

@author: Kartik
"""

N=int(input("No of planets:"))
L = [int(i) for i in input("List of distances of planet:").split()]
K=int(input("position of favourite planet in unsorted list:"))
position = L[K-1]#K-1,mean 0 is not included at first!=0,1,...,there is also 1,2,3,...
L.sort()
print(L)
for i in range(N):
    if L[i] == position:
        print(i+1)
        break
    