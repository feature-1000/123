# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:25:21 2020

@author: adiministrator
"""

#今有雉兔同笼，上有三十五头，下有九十四足，问雉兔各几何？
#编写程序求解鸡兔同笼问题，输入鸡和兔子的总数及腿的数量，输出鸡和兔子分别有多少只。
#首先从键盘上接收两个数，但python接收时当成一个字符串，
#将字符串用split方法从空格处切割开来，(即输入两个数时中间至少一个空格，逗号也不行)
#切割开来仍然是两个字符串，调用map将其int化，即强行取整，
#第一个数赋值给heads(总头数), 第二个数赋值给legs(总腿数)
#此时，输入，接收均完成了
heads, legs = map(int, input('请输入鸡兔总数和腿总数：').split())
#下面是数学意义上的除法，计算结果可以有小数
#如果rabbit带有小数，即说明输入数据有误，本题无解
rabbit = (legs - heads*2) / 2 
#如果rabbit带有小数，chicken也带有小数，否则，两者都是整数(小数点后为0)
chicken = heads - rabbit
#合法性检查，如果数量都大于0，并且rabbit是整数(小数点后为0)，隐含chicken是整数(小数点后为0)
if rabbit>=0 and chicken>=0 and int(rabbit)==rabbit:
    #输出鸡的数量和兔的数量
    print('鸡的数量：{0},兔的数量：{1}'.format(int(chicken), int(rabbit)))
#合法性检查没通过
else:
    print('数据不正确')