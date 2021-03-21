# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:02:33 2020

@author: adiministrator
"""

###7.2.13  使用标准差与协方差分析员工业绩
###演示数据
import pandas as pd

df = pd.DataFrame({'A':[3,3,3,3,3], 'B':[1,2,3,4,5],'C':[-5,-4,15,4,5], 'D':[-50,-40,15,40,50]})
print('原始数据'.ljust(20,'='))
print(df)

print('平均值'.ljust(20,'='))
print(df.mean())

print('标准差'.ljust(20,'='))
print(df.std())

print('标准差的平方'.ljust(20,'='))
print(df.std()**2)

print('协方差'.ljust(20,'='))
print(df.cov())


###使用标准差和协方差分析不同柜台的业绩
# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx',
                     usecols=['姓名','日期','时段','柜台','交易额'])

# 丢弃缺失值和重复值
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# 处理异常值
df.loc[df.交易额<200, '交易额'] = 200
df.loc[df.交易额>3000, '交易额'] = 3000

# 使用交叉表得到不同员工在不同柜台的交易额平均值
dff = pd.crosstab(df.姓名, df.柜台, df.交易额, aggfunc='mean')

print('标准差'.ljust(20,'='))
print(dff.std())

print('协方差'.ljust(20,'='))
print(dff.cov())