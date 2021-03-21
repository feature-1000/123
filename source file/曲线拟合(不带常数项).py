# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:18:08 2020

@author: adiministrator
"""
import numpy as np
import matplotlib.pyplot as plt

#为了在输出图形中能显示中文，做如下设置。否则为“口口口口”字样
import matplotlib.font_manager as fm
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc') #中文为宋体


x=np.array([[1,1],[2,4],[3,9],[4,16],[5,25]])
y=np.array([1.8,2.7,3.4,3.8,3.9])
y=y.T  #矩阵转置

A=x.T@x   #x^T *X
b=x.T@y   #x^T *y
#求解A.beta=b的解 
beta=np.linalg.solve(A,b)
#或者也可以用逆阵的求法
#beta=np.linalg.inv(A)@b

print(beta)

b1,b2=beta #序列解包，作为多项式的系数




#横坐标
x = np.array([1,2,3,4,5])
#纵坐标，使之转换成numpy数组类型
y = np.array([1.8,2.7,3.4,3.8,3.9])
#需降序排列，作为多项式的系数，不含常数项，故第三个为0
z1 = (b2,b1,0)
#生成多项式对象
p1= np.poly1d(z1)
#在屏幕上打印拟合多项式
print(p1)
#计算多项式的函数值,返回在x处多项式的值
yvals = p1(x)   #也可以使用yvals=np.polyval(z1,x),，z1为多项式系数，元素按多项式降幂排序
print(yvals)
'''
figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)

num:图像编号或名称，数字为编号 ，字符串为名称
figsize:指定figure的宽和高，单位为英寸；
dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80      1英寸等于2.5cm,A4纸是 21*30cm的纸张 
facecolor:背景颜色
edgecolor:边框颜色
frameon:是否显示边框
'''

#为画光滑曲线，重新采样
x3=np.linspace(0,6,100)
#根据拟合函数求其纵坐标，由于采样细，画出来显得光滑
y3=list(map(lambda item:b2*item**2+b1*item,x3))
y3=np.array(y3)

plt.figure('曲线拟合图', facecolor='#5959AB', figsize=(10, 8))
#绘制原始散点
plot1 = plt.plot(x,y,'b*',label='原始值')     #蓝色散点
#绘拟合曲线
plot2 = plt.plot(x,yvals,'r*',label='拟合值') #红色散点
plot3 = plt.plot(x3,y3,'g',label='拟合曲线')

#添加文本标注
plt.text(2,2.5,'-0.1988* x^2 + 1.76* x')

#绘横、纵坐标,设置坐标标签字体大小
plt.xlabel('x-axis',fontsize=30)
plt.ylabel('y-axis',fontsize=30)

#绘出图例，legend的位置系统选择,设置坐标标签字体大小,可以自己help它的用法

plt.legend(prop=myfont,loc='best',fontsize=15)   
#绘制标题，为能显示中文，需要给出字体信息
plt.title('曲线拟合图',fontproperties='simsun',fontsize=20)
#显示图形
plt.show()
#保存成一个图形文件
plt.savefig('p1.png')