# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:15:16 2020

@author: adiministrator




已知文件“超市营业额.xlsx”中记录了某超市2019年3月1日至5日各员工在不同时段、不同柜台的销售额。
部分数据如图所示：(见文件)

打印所有数据

"""
'''
在openpyxl中，主要用到三个概念：Workbooks，Sheets，Cells。Workbook就是一个excel工作簿；
Sheet是工作簿中的一张工作表；Cell就是简单的一个格。openpyxl就是围绕着这三个概念进行的，
不管读写都是“三板斧”：打开Workbook，定位Sheet，操作Cell。
'''

from openpyxl import load_workbook
#读取工作簿文件“超市营业额.xlsx”中的第一张工作表，返回一个对象，命名为ws
ws = load_workbook('超市营业额.xlsx').worksheets[0]
#对ws.rows遍历，返回索引，索引值的迭代器对象，类似：0，第0行的内容(元组)；1，第1行的内容(元组)；......
for  row in ws.rows:
    for j in range(len(row)):
        print(row[j].value,end='    ')
    print()
    
    