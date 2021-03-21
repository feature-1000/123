# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:05:25 2020

@author: adiministrator
"""

###7.2.17  数据拆分与合并
#（1）concat()函数与append()方法
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取Sheet1中全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')
# 读取Sheet2中全部数据，使用默认索引
df5 = pd.read_excel(r'超市营业额2.xlsx',
                      sheet_name='Sheet2')

# 按行进行拆分
df1 = df[:3]
df2 = df[50:53]
# 按行进行合并，要求多个DataFrame结构相同
df3 = pd.concat([df1,df2,df5])
# 使用append()方法按行合并，忽略原来的索引
df4 = df1.append([df2,df5], ignore_index=True)
# 按列进行拆分
df6 = df.loc[:, ['姓名','柜台','交易额']]

print(df1, df2, df3, df4, df6[:5], sep='\n\n')