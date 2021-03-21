# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:58:21 2020

@author: adiministrator
"""

###7.2.7  处理超市交易数据中的缺失值
from copy import deepcopy
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')

print('数据总行数'.ljust(20,'='))
print(len(df))

print('丢弃缺失值之后的行数'.ljust(20,'='))
print(len(df.dropna()))

print('包含缺失值的行'.ljust(20,'='))
print(df[df['交易额'].isnull()])

print('使用固定值替换缺失值'.ljust(20,'='))
# 深复制，不影响原来的df
dff = deepcopy(df)
dff.loc[dff.交易额.isnull(),'交易额'] = 1000
print(dff.iloc[[110,124,168],:])

print('使用每人交易额均值替换缺失值'.ljust(20,'='))
dff = deepcopy(df)
for i in dff[dff.交易额.isnull()].index:
    dff.loc[i, '交易额'] = round(dff.loc[dff.姓名==dff.loc[i,'姓名'], '交易额'].mean())
print(dff.iloc[[110,124,168],:])

print('使用整体均值的80%填充缺失值'.ljust(20,'='))
df.fillna({'交易额': round(df['交易额'].mean()*0.8)}, inplace=True)
print(df.iloc[[110,124,168],:])