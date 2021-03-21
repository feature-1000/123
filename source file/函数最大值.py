# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:52:00 2020

@author: adiministrator
"""
'''
编写程序，求解指定函数在给定区间的最大值。
解析：本例主要是演示内置函数map()和max()的用法。
'''

#两个多项式函数， 匿名函数

func1 = lambda x: 5*x**3 + 6*x**2 + 2*x + 8
func2 = lambda x: x**2 - 6*x + 9

'''
def func1(x):
    y=5*x**3 + 6*x**2 + 2*x + 8
    return(y)
'''   
    
    
#自变量定义域
xs = [] #空列表
for i in range(0, 201):
    xs.append(i/1)  #追加横坐标，步长0.02，
    
#输出两个函数在给定区间的最大值
print(max(map(func1, xs)))
print(max(map(func2, xs)))
