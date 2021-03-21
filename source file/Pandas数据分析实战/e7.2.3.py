# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:02:28 2020

@author: adiministrator
"""
###7.2.3  查看数据特征和统计信息
import pandas as pd

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')

print('查看交易额统计信息'.ljust(20, '='))
print(df['交易额'].describe())

print('交易额四分位数'.ljust(20, '='))
print(df['交易额'].quantile([0, 0.25, 0.5, 0.75, 1.0]))

print('交易额中值'.ljust(20, '='))
print(df['交易额'].median())

print('交易额最小的三条记录'.ljust(20, '='))
print(df.nsmallest(3, '交易额'))

print('交易额最大的5条记录'.ljust(20, '='))
print(df.nlargest(5, '交易额'))

print('最后一个日期'.ljust(20, '='))
print(df['日期'].max())

print('最小的工号'.ljust(20, '='))
print(df['工号'].min())

print('第一个最小交易额的行下标'.ljust(20,'='))
index = df['交易额'].idxmin()
print(index)
print('第一个最小交易额'.ljust(20,'='))
print(df.loc[index,'交易额'])

print('第一个最大交易额的行下标'.ljust(20,'='))
index = df['交易额'].idxmax()
print(index)
print('第一个最大交易额'.ljust(20,'='))
print(df.loc[index,'交易额'])
