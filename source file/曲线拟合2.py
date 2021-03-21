# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:05:25 2020

@author: adiministrator

根据给定样本点坐标绘制散点图，然后使用多项式对这些点进行拟合，
绘制拟合效果图。

"""
import numpy as np
import matplotlib.pyplot as plt

#产生横坐标
x = np.arange(1,17,1)
#纵坐标，使之转换成numpy数组类型
y = np.array([4.00,6.40,8.00,8.80,9.22,9.50,9.70,9.86,10.00,10.20,10.32,10.42,10.50,10.55,10.58,10.60])
#用3次多项式拟合  可以改为5次多项式。返回三次多项式系数
##最高次幂3，得到4个系数,从高次到低次排列
z1 = np.polyfit(x,y,3)
# 生成多项式对象
p1= np.poly1d(z1)
#在屏幕上打印拟合多项式
print(p1)
#计算多项式的函数值,返回在x处多项式的值
yvals = p1(x)   #也可以使用yvals=np.polyval(z1,x),，z1为多项式系数，元素按多项式降幂排序

'''

figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)

num:图像编号或名称，数字为编号 ，字符串为名称
figsize:指定figure的宽和高，单位为英寸；
dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80      1英寸等于2.5cm,A4纸是 21*30cm的纸张 
facecolor:背景颜色
edgecolor:边框颜色
frameon:是否显示边框
'''

plt.figure('曲线拟合图', facecolor='#f4f4f4', figsize=(10, 8))
#绘制原始散点
plot1 = plt.plot(x,y,'*',label='original  values')
#绘拟合曲线
plot2 = plt.plot(x,yvals,'r',label='polyfit values')


#绘横、纵坐标,设置坐标标签字体大小
plt.xlabel('xaxis',fontsize=20)
plt.ylabel('yaxis',fontsize=20)

#，绘出图例，legend的位置系统选择,设置坐标标签字体大小,可以自己help它的用法
plt.legend(loc='best',fontsize=15)
#绘制标题
plt.title('polyfitting',fontsize=20)
#显示图形
plt.show()
#保存成一个图形文件
plt.savefig('p1.png')