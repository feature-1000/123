# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 21:05:20 2019

@author: adiministrator
"""

#三国演义出场人物分析2

import jieba

excludes={"将军","却说","荆州","二人","不可","不能","如此"}
f=open("三国演义.txt", "r", encoding='utf-8')
txt = f.read()
f.close()


words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(5):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
