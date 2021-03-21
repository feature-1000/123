# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:58:47 2020

@author: adiministrator
"""

###7.2.8  处理超市交易数据中的重复值
from copy import deepcopy
import pandas as pd
import numpy as np

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')

print('数据总行数'.ljust(20,'='))
print(len(df))

print('重复行'.ljust(20,'='))
print(df[df.duplicated()])

print('一人同时负责两个柜台的排班'.ljust(20,'='))
dff = df[['工号','姓名','日期','时段']]
dff = dff[dff.duplicated()]
for row in dff.values:
    print(df[(df.工号==row[0])&(df.日期==row[2])&(df.时段==row[3])])

# 直接丢弃重复行
df = df.drop_duplicates()
print('有效数据总行数'.ljust(20,'='))
print(len(df))

# 可以查看是否有录入错误的工号和姓名
print('所有工号与姓名的对应关系'.ljust(20,'='))
dff = df[['工号','姓名']]
print(dff.drop_duplicates())