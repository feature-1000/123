# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:43:53 2020

@author: adiministrator
"""

"""
输出所有的“水仙花数”，所谓的“水仙花数”是指一个三位数其各位数字的立方和等于该数本身，
例如153是“水仙花数”，因为：153 = 1^3 + 5^3 + 3^3
"""
for i in range(100, 1000):
    #这里是序列解包的用法
    bai, shi, ge = map(int, str(i))
    if bai**3 + shi**3 +  ge**3  == i:
        print(i)