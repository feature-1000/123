# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:16:01 2020

@author: adiministrator
"""
'''
宝塔上的琉璃灯
有一座八层宝塔，每一层都有一些琉璃灯，每一层的灯数都是上一层的二倍，
已知共有765盏琉璃灯，求解每层各有多少。

简单分析：
可以假设最高层琉璃灯的数量为1、2、3、4...，然后分别计算各层灯数，
如果各层灯数之和为765，则给出答案并停止假设。

代码中使用到了标准库itertools中的函数count(start, step)，
返回包含从start开始且以step为步长的无限长整数数列（start, start+step, start+2*step, start+3*step,...）的count对象。
代码中使用列表推导式计算假设顶层灯数为first时各层的灯数。



'''
from itertools import count
for first in count(1, 1):
    floors = [first*(2**i) for i in range(8)]
    if sum(floors) == 765:
        for index,values in enumerate(floors,start=1):
            print(f'第{index}层有{values}盏琉璃灯')
        break
    
    
'''
假设顶层灯数为x，那么顶层灯数计算方法如下：
2^0x+2^1x+2^2x+2^3x+2^4x+2^5x+2^6x+2^7x=765
x=3
'''
'''
total = 765
factor = [2**i for i in range(8)]
first = int(total/sum(factor))
for index,values in enumerate(factor,start=1):
    print(f'第{index}层有{values*first}盏琉璃灯')


'''

