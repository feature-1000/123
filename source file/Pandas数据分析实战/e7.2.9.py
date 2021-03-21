# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:59:21 2020

@author: adiministrator
"""

###7.2.9  使用数据差分查看员工业绩波动情况
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')

print('每天交易总额变化情况'.ljust(20,'='))
dff = df.groupby(by='日期').sum()['交易额'].diff()
# 格式化，整数前面带加号
print(dff.map(lambda num:'%+.2f'%num)[:5])

print('张三的每天交易总额变化情况'.ljust(20,'='))
print(df[df.姓名=='张三'].groupby(by='日期').sum()['交易额'].diff()[:5])