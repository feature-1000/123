# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:25:29 2020

@author: adiministrator
"""

#编写程序，判断一个年份是否为闰年。
#python默认接收到的为字符串
year = input('请输入一个4位数字的年份:')
if len(year) != 4:         
    print('输入错误')
else:
    year=int(year)
    if (year%4==0 and year%100!=0) or year%400==0:
        print('{0}年是闰年!'.format (year))
    else:
        print('{0}年不是闰年!'.format (year))
