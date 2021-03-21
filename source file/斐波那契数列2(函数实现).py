# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:29:36 2019

@author: adiministrator
"""
#定义一个斐波那契数列函数，然后通过调用该函数来实现此功能
def fib(n):
    '''accept an integer n.
    return the numbers less than n in Fibonacci sequence.'''
    a, b = 1, 1
    while a < n:
        print(a  ,end=' ')
        a = b
        b=a+b
    print()#回车另起一行,主要是怕多次调用该函数，输出结果放一起互相干扰，影响对程序的理解

#下面是两次调用该函数，实现了代码复用，减少了工作量
fib(10)
fib(50000)
#执行后，如果在Anaconda的右下窗口，输入help(fib),给出提示，即定义时的'''   '''里面的内容，帮助信息
 