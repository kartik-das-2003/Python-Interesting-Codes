# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 20:20:36 2022

@author: Kartik
"""

import random
import matplotlib.pyplot as plt

account = 0
x=[]
y=[]
for i in range(30):
    x.append(i+1)
    n = random.randint(0,10)
    #print(n)
    a = random.randint(0,10)
    #print(a)
    if(a==n):
        account = account+1100-100
        #print("account balance",account)
    else:
        account = account-100
        #print("account balance",account)
    y.append(account)
        
print("Final Valule Of Amount",account)
plt.plot(x,y)
plt.show()