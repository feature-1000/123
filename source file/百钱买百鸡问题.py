# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:29:46 2020

@author: adiministrator
"""

'''
编写程序，计算百钱买百鸡问题。假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100元钱，
想买100只鸡，问有多少种买法？
解析：本例重点在于内置函数range()和循环嵌套的用法。
'''

#循环法
for x in range(21):
    for y in range(34):
        z=100-x-y
        if (z%3==0 and 5*x+3*y+z//3==100):
            print(x,y,z)
            
#列表推导式
#[(x,y,100-x-y) for x in range(21) for y in range(34) if ((100-x-y)%3==0 and 5*x+3*y+(100-x-y)//3==100) ]




