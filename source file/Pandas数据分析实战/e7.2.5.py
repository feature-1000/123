# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:57:09 2020

@author: adiministrator
"""

###7.2.5  使用分组与聚合对员工业绩进行汇总
import pandas as pd
import numpy as np

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')

print('根据lambda表达式对index处理后的结果分组'.ljust(30,'='))
print(df.groupby(by=lambda num: num%5)['交易额'].sum())

# 根据指定字典的“键”对index进行分组，“值”作为index标签
print('指定by参数为字典'.ljust(30,'='))
print(df.groupby(by={7:'下标为7的行', 35:'下标为35的行'})['交易额'].sum())

print('不同时段的销售总额'.ljust(30,'='))
print(df.groupby(by='时段')['交易额'].sum())

print('各柜台的销售总额'.ljust(30,'='))
print(df.groupby(by='柜台')['交易额'].sum())

# 可以查看每个员工上班总时长是否均匀
print('每个员工上班的次数'.ljust(30,'='))
dff = df.groupby(by='姓名')['日期'].count()
dff.name = '上班次数'
print(dff)

print('每个员工交易额平均值'.ljust(30,'='))
print(df.groupby(by='姓名')[ '交易额'].mean().round(2).sort_values())

print('汇总交易额转换为整数'.ljust(30,'='))
print(df.groupby(by='姓名').sum()['交易额'].apply(int))

print('每个员工交易额的中值'.ljust(30,'='))
dff = df.groupby(by='姓名').median()
print(dff['交易额'])

dff['排名'] = dff['交易额'].rank(ascending=False)
print('每个员工交易额中值的排名'.ljust(30,'='))
print(dff[['交易额','排名']])

print('每个员工不同时段的交易额'.ljust(30,'='))
print(df.groupby(by=['姓名','时段'])['交易额'].sum())

# 对不同的列可以采用不同的函数
print('时段和交易额采用不同的聚合方式'.ljust(30,'='))
print(df.groupby(by=['姓名'])['时段', '交易额'].aggregate({'交易额':np.sum, '时段':lambda x:'各时段累计'}))

# 使用DataFrame结构的agg()方法对指定列进行聚合
print('使用agg()方法对交易额进行聚合'.ljust(30,'='))
print(df.agg({'交易额':['sum','mean','min','max','median'], '日期':['min','max']}))

print('对分组结果进行聚合'.ljust(30,'='))
print(df.groupby(by='姓名').agg(['max','min','mean','median']))

print('查看分组聚合后的部分结果'.ljust(30,'='))
print(df.groupby(by='姓名').agg(['max','min', 'mean','median'])['交易额'])