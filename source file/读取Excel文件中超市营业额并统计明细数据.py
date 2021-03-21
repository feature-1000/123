# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:36:06 2020

@author: adiministrator

已知文件“超市营业额.xlsx”中记录了某超市2019年3月1日至5日各员工在不同时段、不同柜台的销售额。
部分数据如图所示：

要求编写程序，读取该文件中的数据，并统计每个员工的销售总额、每个时段的销售总额、
每个柜台的销售总额。

"""

from openpyxl import load_workbook

#3个字典分别存储按员工、按时段、按柜台的销售总额persons= dict（
persons = dict()
periods = dict()
goods = dict()

ws = load_workbook('超市营业额.xlsx').worksheets[0]
for index, row in enumerate(ws.rows):
    #跳过第一行的表头
    if index==0:
        continue
    #获取每行的相关信息
    _,name,_,time,num,good = map(lambda cell:cell.value,row)
    #根据每行的值更新三个字典
    persons[name] = persons.get(name,0)+num
    periods[time] = periods.get(time,0)+num
    goods[good] = goods.get(good,0)+num

print(persons)
print(periods)
print(goods)

