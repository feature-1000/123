# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:17:38 2020

@author: adiministrator
"""

#例，编写函数，接收整数或实数参数作为圆的半径，输出圆的面积。
#从内置库(模块)math中导入指定对象pi,并给它取了个别名：PI，就是引入圆周率的数值
from math import pi as PI

#定义了一个求圆面积的函数，输入参数为半径r
def circleArea(r):
    #下面的语句是测试r必须为整型或者为浮点型，并且要求r大于0
    if isinstance(r, (int,float)) and r>0:       # 确保接收的参数为正的整数或实数值
        return PI*r*r  #返回圆面积的值
    else:
        #如果上面的if语句不满足，给出下列提示信息，帮助检查错误
        return 'You must give me an integer or float as radius.'
#上面定义的函数结束

#先调用circleArea函数将半径为3的圆面积求出，调用print函数将其值输出
i=input('r =') 
r=int(i)  
print('圆面积=' ,circleArea(r))
