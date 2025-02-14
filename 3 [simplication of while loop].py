# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 22:13:14 2022

@author: Kartik
"""

#pin code case/Bank Case
import random
k=random.randint(0, 5)
print(k)
n=int()
x=int(k)
while(x==k):
    for i in range(1):
        n=int(n+1)
        print("You Are Lucky Mann",n)
        x=input("Next,Input Your Pin:")
        x=int(x)
else:
    print("You Are Cheater")
        
