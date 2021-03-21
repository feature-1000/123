# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:44:09 2020

@author: adiministrator
"""
#python-docx这个库。它只能解析docx文件，解析不了doc文件。安装方式直接pip install python-docx。
#安装的模块名与使用的模块名不一样，在python中常见，为了保持向下兼容
from docx import Document
from docx.shared import RGBColor

boldText = []
redText = []
doc = Document('test.docx')
#在word中的一个自然段，就是一个paragraph，用一个for循环就可以获得全部的段落。这是一个可迭代的类型
for p in doc.paragraphs:
    #格式，是加粗，颜色，居中等等这些排版设计的东西,在paragraph中，叫做run,一个段落是由许多run组成的
    #这同样是个可迭代的类型，可以循环获得每一个run相关的内容，比如alignment（对齐方式），bold（加粗），italic（斜体），text（具体文本内容）等等。
    for r in p.runs:
        # 加粗字体
        if r.bold:
            boldText.append(r.text) #列表追加元素
        # 红色字体
        if r.font.color.rgb == RGBColor(255,0,0):
            redText.append(r.text)   #列表追加元素

result = {'red text': redText,
          'bold text': boldText,
          'both': set(redText) & set(boldText)}  #列表转成集合，集合取“与”
#  输出结果
for title in result.keys():
    print(title.center(30, '='))
    for text in result[title]:
        print(text)

