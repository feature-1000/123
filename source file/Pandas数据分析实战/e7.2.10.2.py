# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:00:46 2020

@author: adiministrator
"""

###7.2.10  使用透视表与交叉表查看业绩汇总数据
#（2）交叉表
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')

print('每人每天的上班次数'.ljust(20,'='))
print(pd.crosstab(df.姓名, df.日期, margins=True).iloc[:,:5])
#u针Dataframe数据写入Excel文件保存
#pd.crosstab(df.姓名, df.日期, margins=True).iloc[:,:].to_excel('a1.xlsx',index=True)

print('每人在各柜台上班总次数'.ljust(20,'='))
print(pd.crosstab(df.姓名, df.柜台))

print('每人在各柜台交易总额'.ljust(20,'='))
print(pd.crosstab(df.姓名, df.柜台, df.交易额, aggfunc='sum'))

print('每人在各柜台交易额平均值'.ljust(20,'='))
print(pd.crosstab(df.姓名, df.柜台, df.交易额, aggfunc='mean').apply(lambda num: round(num,2)))