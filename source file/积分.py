# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:25:05 2020

@author: 10232
"""

 
import numpy as np
 
#区间
u=3
l=1
 
#导函数

def f(x):
    i=x**2
    return i

count=100
list=np.linspace(l,u,count+1)
sum=0

for i in range(count):
    x0=list[i]
    x1=list[i+1]
    v=(x1-x0)*f(0.5*(x1+x0))
    sum+=v
       
 
print("计算的定积分：")
print(sum)

 
