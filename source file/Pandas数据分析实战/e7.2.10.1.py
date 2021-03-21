# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:59:44 2020

@author: adiministrator
"""

###7.2.10  使用透视表与交叉表查看业绩汇总数据
#（1）透视表
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')

print('查看每人每天交易总额'.ljust(20,'='))
dff = df.groupby(by=['姓名','日期'], as_index=False).sum()
# 数据量太大，为减少篇幅占用，只输出前5天的数据
dff = dff.pivot(index='姓名', columns='日期', values='交易额')
print(dff.iloc[:,:5])

print('交易总额低于5万元的员工前5天业绩'.ljust(20,'='))
print(dff[dff.sum(axis=1)<50000].iloc[:,:5])

print('交易总额低于5万元的员工姓名'.ljust(20,'='))
print(dff[dff.sum(axis=1)<50000].index.values)

print('使用pivot_table()方法实现'.ljust(20,'='))
# 如果把只显示前5列的限制去掉，会发现最后还有一个名字为ALL的列
print(df.pivot_table(values='交易额', index='姓名', columns='日期', aggfunc='sum',margins=True).iloc[:,:5])

print('查看每人在各柜台的交易总额'.ljust(20,'='))
dff = df.groupby(by=['姓名','柜台'], as_index=False).sum()
print(dff.pivot(index='姓名', columns='柜台', values='交易额'))

print('查看每人每天的上班次数'.ljust(20,'='))
print(df.pivot_table(values='交易额', index='姓名', columns='日期', aggfunc='count',margins=True).iloc[:,:5])

print('查看每人在各柜台的上班次数'.ljust(20,'='))
print(df.pivot_table(values='交易额', index='姓名', columns='柜台', aggfunc='count',margins=True))