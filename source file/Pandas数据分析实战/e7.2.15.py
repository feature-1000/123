# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:03:29 2020

@author: adiministrator
"""

###7.2.15  绘制各员工在不同柜台业绩平均值的柱状图
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 读取全部数据，使用默认索引
df = pd.read_excel(r'超市营业额2.xlsx')

# 修改异常值
df.loc[df.交易额>3000, '交易额'] = 3000
df.loc[df.交易额<200, '交易额'] = 200

# 删除重复值
df.drop_duplicates(inplace=True)

# 填充缺失值
df['交易额'].fillna(df['交易额'].mean(), inplace=True)

# 使用交叉表得到每人在各柜台交易额平均值
print(''.ljust(20,'='))
df_group = pd.crosstab(df.姓名, df.柜台, df.交易额, aggfunc='mean').apply(round)

# 绘制柱状图，默认使用index作为横坐标
df_group.plot(kind='bar')

font = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf')
plt.xlabel('员工业绩分布', fontproperties='simhei', fontsize=15)
plt.ylabel('员工交易额均值', fontproperties='simhei', fontsize=15)
plt.title('员工业绩分布bar图', fontproperties='simhei', fontsize=20)
plt.xticks(fontproperties='simhei')
plt.legend(prop=font)

# 显示绘制结果
plt.show()