# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:34:56 2020

@author: adiministrator
"""

###7.2.1  读取Excel文件中的数据
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取工号、姓名、时段、交易额这四列数据，使用默认索引
df = pd.read_excel('超市营业额2.xlsx',
                   usecols=['工号','姓名','时段','交易额'])

df.to_excel('a3.xlsx',index=False)

# 输出前10行数据
print(df[:10], end='\n\n')

# 读取第一个worksheet中所有列
# 跳过第1、3、5行，指定下标为1的列中数据为DataFrame的行索引标签
df = pd.read_excel('超市营业额2.xlsx',
                   skiprows=[1,3,5], index_col=1)
print(df[:10])



