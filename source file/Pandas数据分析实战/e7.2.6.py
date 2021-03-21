# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:57:52 2020

@author: adiministrator
"""

###7.2.6  处理超市交易数据中的异常值
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')

print('查看交易额低于200的数据'.ljust(20,'='))
print(df[df.交易额<200])

df.loc[df.交易额<200, '交易额'] = df[df.交易额<200]['交易额'].map(lambda num: num*1.5)
print('上浮50%之后仍低于200的数据'.ljust(20,'='))
print(df[df.交易额<200])

print('查看交易额高于3000的数据'.ljust(20,'='))
print(df[df['交易额']>3000])

print('交易额低于200或高于3000的数据'.ljust(20,'='))
print(df[(df.交易额<200) | (df.交易额>3000)])

# 把低于200的交易额都替换为固定的200
df.loc[df.交易额<200, '交易额'] = 200
print('交易额低于200或高于3000的数据'.ljust(20,'='))
print(df[(df.交易额<200) | (df.交易额>3000)])

# 把高于3000的交易额都替换为固定的3000
df.loc[df.交易额>3000, '交易额'] = 3000
print('交易额低于200或高于3000的数量'.ljust(20,'='))
print(df[(df.交易额<200) | (df.交易额>3000)]['交易额'].count())