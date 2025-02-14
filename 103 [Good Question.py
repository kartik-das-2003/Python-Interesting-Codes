# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 22:45:17 2022

@author: Kartik
"""

def uniqueE(L):
  ans=[]
  for a in L:
    if L.count(a)==1:
      ans.append(a)
  return(sorted(ans))
L = [int(i) for i in input().split()]
print(uniqueE(L))