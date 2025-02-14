# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:09:56 2022

@author: Kartik
"""

#You are given a list L. Write a function all_even that accepts the list L and print all the even numbers is the list L.(Order of the numbers should be same as the order present in the list)
def all_even(L):
    for i in L:
        if (i%2==0):
            print(i)
L = [int(i) for i in input().split()]
all_even(L)