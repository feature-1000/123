# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:30:15 2020

@author: adiministrator
"""

###7.1.3  二维数组DataFrame
import numpy as np
import pandas as pd

# 设置输出结果列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 在[1,20]区间上生成5行3列15个随机数
# 使用index参数指定索引，columns参数指定每列标题
df = pd.DataFrame(np.random.randint(1, 20, (5,3)),
                  index=range(5),
                  columns=['A', 'B', 'C'])
print(df)

print('='*20)
# 模拟2019年7月15日某超市熟食、化妆品、日用品每小时的销量
# 使用时间序列作为索引
df = pd.DataFrame(np.random.randint(5, 15, (13, 3)),
                  index=pd.date_range(start='201907150900',
                                      end='201907152100',
                                      freq='H'),
                  columns=['熟食', '化妆品', '日用品'])
print(df)

print('='*20)
# 模拟考试成绩，使用人名字符串做索引
df = pd.DataFrame({'语文':[87,79,67,92],
                   '数学':[93,89,80,77],
                   '英语':[90,80,70,75]},
                  index=['张三', '李四', '王五', '赵六'])
print(df)

print('='*20)
# 自动对B列数据进行扩充，使其与A列数据一样多
df = pd.DataFrame({'A':range(5,10), 'B':3})
print(df)