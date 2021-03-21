# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:06:04 2020

@author: adiministrator
"""

###7.2.17  数据拆分与合并
#（2）merge()方法与join()方法
import numpy as np
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取Sheet1中全部数据，使用默认索引
df1 = pd.read_excel(r'超市营业额2.xlsx')
# 读取Sheet3中全部数据，使用默认索引
df2 = pd.read_excel(r'超市营业额2.xlsx', sheet_name='Sheet3')

# 按同名的列合并，随机查看10行数据
rows = np.random.randint(0, len(df1), 10)
print(pd.merge(df1, df2).iloc[rows,:], end='\n\n')

# 按工号合并，指定其他同名列的后缀
print(pd.merge(df1, df2, on='工号', suffixes=['_x','_y']).iloc[rows,:], end='\n\n')

# 两个表都设置工号列为索引
print(df1.set_index('工号').join(df2.set_index('工号'), lsuffix='_x', rsuffix='_y').iloc[rows,:])