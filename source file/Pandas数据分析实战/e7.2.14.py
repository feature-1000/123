# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:02:59 2020

@author: adiministrator
"""

###7.2.14  使用pandas的属性接口实现高级功能
import copy
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx', usecols=['日期', '交易额'])

# 深复制，不影响原来的df
dff = copy.deepcopy(df)
# 把日期列替换为周几
dff['日期'] = pd.to_datetime(df['日期']).dt.weekday_name
# 按周几分组，查看交易额平均值，四舍五入
print('按周几分组查看交易额平均值'.ljust(20,'='))
dff = dff.groupby('日期').mean().apply(round)
dff.index.name = '周几'
print(dff)

dff = copy.deepcopy(df)
# 修改日期列，只保留年份和月份
dff['日期'] = dff['日期'].str.extract(r'(\d{4}-\d{2})')
print('只查看年份和月份'.ljust(20,'='))
print(dff[:5])

# 按字符串形式的日期最后一位数进行分组
# 该月1、11、21、31日汇总为一组，2、12、22日为一组，以此类推
print('按日期的日进行分组查看交易额平均值'.ljust(20,'='))
print(df.groupby(df['日期'].str.__getitem__(-1)).mean().apply(round))

# 查看日期尾数为6的数据前12行
print('查看日期尾数为6的数据'.ljust(20,'='))
print(df[df['日期'].str.endswith('6')][:12])

# 查看日期尾数为12的数据
# slice()接收3个参数，分别为起始位置、结束位置和步长
print('日期尾数为12的交易数据'.ljust(20,'='))
print(df[df.日期.str.slice(-2)=='12'])

# 日期中月份或天数包含2的交易数据第15到25行
print('日期中月份或天数包含2的交易数据'.ljust(20,'='))
print(df[df.日期.str.slice(-5).str.contains('2')][15:25])