# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:07:52 2020

@author: adiministrator
"""

###7.1.1  一维数组与常用操作
import pandas as pd
import matplotlib.pyplot as plt

# 设置输出结果列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 自动创建从0开始的非负整数索引
s1 = pd.Series(range(1, 20, 5))
# 使用字典创建Series，使用字典的“键”作为索引
s2 = pd.Series({'语文':90, '数学': 92, 'Python': 98, '物理':87, '化学': 92})
# 修改指定索引对应的值
s1[3] = -17
s2['语文'] = 94

print('s1原始数据'.ljust(20, '='))
print(s1)

print('对s1所有数据求绝对值'.ljust(20, '='))
print(abs(s1))

print('s1所有的值加5'.ljust(20, '='))
print(s1+5)

print('s1的每行索引前面加上数字2'.ljust(20, '='))
print(s1.add_prefix('2_'))

print('s2原始数据'.ljust(20, '='))
print(s2)

print('s2数据的直方图'.ljust(20,'='))
s2.hist()
plt.show()

print('s2的每行索引后面加上_张三'.ljust(20, '='))
print(s2.add_suffix('_张三'))

print('s2最大值的索引'.ljust(20, '='))
#print(s2.argmax())
print(s2.values.argmax())

print('测试s2的值是否在指定区间内'.ljust(20, '='))
print(s2.between(90, 94, inclusive=True))

print('查看s2中90分以上的数据'.ljust(20,'='))
print(s2[s2>90])

print('查看s2中大于中值的数据'.ljust(20,'='))
print(s2[s2>s2.median()])

print('s2与数字之间的运算'.ljust(20, '='))
print(round((s2**0.5)*10, 1))

print('s2的中值'.ljust(20, '='))
print(s2.median())

print('s2中最小的2个值'.ljust(20, '='))
print(s2.nsmallest(2))

# 两个等长Series对象之间可以进行四则运算和幂运算
# 只对两个Series对象中都有的索引对应的值进行计算
# 非共同索引对应的值为控制NaN
print('两个Series对象相加'.ljust(20,'='))
print(pd.Series(range(5))+pd.Series(range(5,10)))

# pipe()方法可以实现函数链式调用的功能
print('每个值的平方对5的余数'.ljust(20,'='))
print(pd.Series(range(5)).pipe(lambda x,y,z:(x**y)%z, 2, 5))

print('每个值加3之后再乘以3'.ljust(20,'='))
print(pd.Series(range(5)).pipe(lambda x:x+3).pipe(lambda x:x*3))

# apply()方法用来对Series对象的值进行函数运算
print('每个值加3'.ljust(20,'='))
print(pd.Series(range(5)).apply(lambda x: x+3))

print('标准差、无偏方差、无偏标准差'.ljust(20,'='))
print(pd.Series(range(5)).std())
print(pd.Series(range(5)).var())
print(pd.Series(range(5)).sem())

print('查看是否存在等价于True的值'.ljust(20,'='))
print(any(pd.Series([3,0,True])))

print('查看是否所有值都等价于True'.ljust(20,'='))
print(all(pd.Series([3,0,True])))