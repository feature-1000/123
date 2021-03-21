# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:08:26 2020

@author: adiministrator
"""

import pandas as pd

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')

print('交易额列占用内存情况'.ljust(20,'='))
print(df['交易额'].memory_usage())

print('内存占用情况'.ljust(20,'='))
print(df.memory_usage())

print('内存占用总额'.ljust(20,'='))
print(df.memory_usage().sum())

print('使用df.info()查看内存占用'.ljust(20,'='))
df.info()
