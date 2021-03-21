# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:12:02 2020

@author: adiministrator
"""

# 统计小说中的单词频次
#小说《Walden》单词词频统计
'''
Walden中文译名《瓦尔登湖》，是美国作家梭罗独居瓦尔登湖畔的记录，描绘了他两年多时间里的所见、
所闻和所思。该书崇尚简朴生活，热爱大自然的风光，内容丰厚，意义深远，语言生动。请用Python统计excludes
小说Walden中各单词出现的频次，并按频次由高到低排序。
'''
from re import  *
f = open('Walden.txt', 'r')
txt = f.read()   # 读取进来的数据类型是字符串
f.close()
txt = txt.lower()
txt = sub('[,.?:"\'!-;].', '', txt)   # 去除小说中的标点符号
words = txt.split()   # 单词分割
word_freq = {}
for i in words:
    if i not in word_freq.keys():
        word_freq[i] = 1
    else:
        word_freq[i] += 1
res = sorted(word_freq.items(), key=lambda x:x[1],reverse=True)  # 排序
print(res)

