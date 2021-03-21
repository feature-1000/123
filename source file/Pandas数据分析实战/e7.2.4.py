# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:49:05 2020

@author: adiministrator
"""

###7.2.4  按不同标准对数据排序
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')

print('按交易额和工号降序排序'.ljust(20, '='))
print(df.sort_values(by=['交易额','工号'], ascending=False)[:12])

print('按交易额降序、工号升序排序'.ljust(20, '='))
print(df.sort_values(by=['交易额','工号'], ascending=[False,True])[:12])

print('按工号升序排序'.ljust(20, '='))
print(df.sort_values(by='工号', na_position='last')[:10])

print('按列名升序排序'.ljust(20, '='))
# 注意，这里是按汉字的Unicode编码排序
print(df.sort_index(axis=1, ascending=True)[:10])