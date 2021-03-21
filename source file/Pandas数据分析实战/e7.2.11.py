# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:01:33 2020

@author: adiministrator
"""

###7.2.11  使用重采样技术按时间段查看员工业绩
import numpy as np
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')
df.日期 = pd.to_datetime(df.日期)

print('每7天营业总额'.ljust(20,'='))
print(df.resample('7D', on='日期').sum()['交易额'])

print('每7天营业总额'.ljust(20,'='))
print(df.resample('7D', on='日期',
                    label='right').sum()['交易额'])

print('每7天营业额平均值'.ljust(20,'='))
func = lambda num:round(num,2)
print(df.resample('7D', on='日期',
                    label='right').mean().apply(func)['交易额'])

print('每7天营业额平均值'.ljust(20,'='))
# 注意，这里要用np.sum()，不能用内置函数sum()
# 因为内置函数sum()不能忽略缺失值
func = lambda item:round(np.sum(item)/len(item),2)
print(df.resample('7D', on='日期',
                    label='right').apply(func)['交易额'])