# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:41:30 2019

@author: adiministrator
"""
#三国演义出场人物分析1.py
import jieba

f=open("三国演义.txt", "r", encoding='utf-8')
txt = f.read()
f.close()

words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:  #排除单个字符的分词结果，主要是标点
        continue
    else:
        counts[word] = counts.get(word,0) + 1   #指有word时返回其值，默认是0，+1能够累计次数；没有word时则返回0

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(15):
    word, count = items[i]
    print ("{0:<5}{1}".format(word, count))
s = input('english :')
a = s.split(" ")
for i in range(len(a)):    
    if a[i] == "i":        
        a[i] = "I"
print (" ".join(a))
 