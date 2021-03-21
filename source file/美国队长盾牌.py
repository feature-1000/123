# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:12:51 2020

@author: adiministrator
"""
'''
请编写Python程序完成以下要求：使用小海龟，在屏幕上绘制一系列的同心圆，并为这些同心圆填充上不同的颜色。
内部再画一个五角星，像美国队长盾牌的造型。
'''
import turtle


turtle.penup()    
turtle.goto(0,-250)
turtle.pendown()
turtle.pensize(3) 
color = ['red','gainsboro','red','blue']
for i in range(4):
    turtle.color(color[i])
    turtle.begin_fill()
    turtle.circle(250-i*40)
    turtle.right(90)
    turtle.penup()
    turtle.fd(-40)
    turtle.seth(0)
    turtle.pendown()
    turtle.end_fill()
    
turtle.penup()    
turtle.goto(0,-250)
turtle.pendown()    
  
for i in range(4):
    turtle.color('black')
    turtle.circle(250-i*40)
    turtle.right(90)
    turtle.penup()
    turtle.fd(-40)
    turtle.seth(0)
    turtle.pendown()
    
turtle.penup()    
turtle.goto(-120,40)
turtle.pendown()
turtle.fillcolor("lightgray")
turtle.color('lightgray')
turtle.begin_fill()
for i in range(5):
    turtle.forward(240)
    turtle.right(144) 
turtle.end_fill()

turtle.hideturtle()  #隐藏箭头
turtle.done()
turtle.bye()#关闭窗体，可反复运行代码 
    

