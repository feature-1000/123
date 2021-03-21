# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:02:03 2020

@author: adiministrator
"""

###7.2.12  多索引相关技术与操作
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')
# 删除工号一列的数据
df.drop('工号', axis=1, inplace=True)
df = df.groupby(by=['姓名', '柜台']).sum()
print('按姓名和柜台进行分组汇总'.ljust(20,'='))
print(df[:10])

print('查看周七的汇总数据'.ljust(20,'='))
print(df.loc['周七',:])

print('查看周七在化妆品柜台的交易数据'.ljust(20,'='))
print(df.loc[('周七', '化妆品')])

# 重新读取数据，指定多个索引
df = pd.read_excel(r'超市营业额2.xlsx', index_col=[1, 5])

# 丢弃“工号”列
df.drop('工号', axis=1, inplace=True)

# 按索引“柜台”排序，查看前12行
dff = df.sort_index(level='柜台', axis=0)
print('按柜台排序，查看前12行'.ljust(20,'='))
print(dff[:12])

# 按索引“姓名”排序，查看前12行
dff = df.sort_index(level='姓名', axis=0)
print('按姓名排序，查看前12行'.ljust(20,'='))
print(dff[:12])

# 按索引“柜台”分组求和
print('按柜台分组求和'.ljust(20,'='))
dfff = dff.groupby(level='柜台').sum()
dfff.columns = ['交易额总和']
print(dfff)

# 按索引“姓名”分组求中值
print('按姓名分组求中值'.ljust(20,'='))
dfff = dff.groupby(level='姓名').median()
dfff.columns = ['交易额中值']
print(dfff)