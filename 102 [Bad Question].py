# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 22:40:01 2022

@author: Kartik
"""

#You are given a string S. Write a function count_letters
#which will return a dictionary containing letters
#(including special character) in string S as keys and their
# count in string S as values.
def count_letters(S):
    d={}
    for i in S:
        d[i]=0
    for i in S:
        d[i]+=1
    return d
S = input()
d = count_letters(S)

d1 = {}
for i in S:
    try:
        d1[i]+=1
    except KeyError:
        d1[i]=1
if d1 == d:
    print('yes')
else:
    print('no')