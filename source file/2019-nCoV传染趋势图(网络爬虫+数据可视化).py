# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:42:14 2020

@author: adiministrator
"""
'''
2020年春节武汉新冠状病毒的疫情爆发。腾讯实时疫情最新动态页面:
（https://news.qq.com/zt2020/page/feiyan.htm?from=timeline&isappinstalled=0），
一个简单的网页爬虫就可以爬取到疫情数据,腾讯最新动态数据从1月13日开始更新，获得数据后，可以数据可视化，
用Matplotlib来实现疫情数据趋势图。

'''
import time
import json
import requests
from datetime import datetime
import pickle
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

#如果图形标识中含有中文字符，需打开下面命令
#plt.rcParams['font.sans-serif'] = ['FangSong']  # 用来正常显示中文标签
#plt.rcParams['axes.unicode_minus'] = False #解决保存图像时'-'显示为方块的问题

def catch_daily():
  
    #数据网址超链接
    url= 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=&_=%d'%int(time.time()*1000) #后面为时间戳
    #下面网址也可以运行
    #url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    reponse = requests.get(url=url).json() #requests中内置了一个JSON解码器，帮助你处理JSON数据
    #返回数据字典
    data = json.loads(reponse['data'])
    #data.keys()#查看字典的键，选取所需数据的键
    #获取指定数据
    data = data['chinaDayList'] 
    #上面三步可合成为下句
    #data = json.loads(requests.get(url=url).json()['data'])['chinaDayList']
    #按日期升序排序
    data.sort(key=lambda x:x['date'])
    #打印超链接
    print(url)
    #空列表，等待追加数据
    
    #将爬虫获取的数据保存成文件，防止网站下架该数据
    with open(r'2019nCOVdata.data', 'wb') as f:
        pickle.dump(data,f)#对象的系列化
    '''
    若网站下架该数据，可从上述数据文件读取数据 
    with open(r'2019nCOVdata.data', 'rb') as f:
        data=pickle.load(f)   #对象的反系列化
    '''
    
    date_list = list() #
    confirm_list = list() # 确诊
    suspect_list = list() # 疑似
    dead_list = list() # 死亡
    heal_list = list() # 治愈
    
    for item in data:
        #分割原数据的日期(1.23这样的数据)
        month, day = item['date'].split('.')
        #month, day = item['date'].split('/')
        #以通用日期格式改写上述日期字符串，
        #要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串
        date_list.append(datetime.strptime('2020-%s-%s'%(month, day), '%Y-%m-%d'))
        #获取四种类型的数据
        confirm_list.append(int(item['confirm']))
        suspect_list.append(int(item['suspect']))
        dead_list.append(int(item['dead']))
        heal_list.append(int(item['heal']))
    #返回五个列表值(日期，确诊数，疑似数，死亡数，治愈数)，供其他函数调用
    return date_list, confirm_list, suspect_list, dead_list, heal_list

def plot_daily():
    #调用上面函数，序列解包，获取所需数据
    date_list, confirm_list, suspect_list, dead_list, heal_list = catch_daily() 
    
    plt.figure('2019-nCoV-Epidemic-Trend', facecolor='#f4f4f4', figsize=(10, 8))
    plt.title('2019-nCoV Epidemic Trend ', fontsize=20)
    
    #plt.plot()函数的本质就是根据点连接线。根据x(数组或者列表) 和 y(数组或者列表)组成点，然后连接成线
    #以日期为横坐标，，分别以确诊数、疑似数、死亡数、治愈数为纵坐标画四条折线
    #标签供后面图例所用
    plt.plot(date_list, confirm_list, label='Confirmed Cases')
    plt.plot(date_list, suspect_list, label='Suspected Cases')
    plt.plot(date_list, heal_list, label='Healed Cases')
    plt.plot(date_list, dead_list, label='Dead Cases')
    
    # 配置横坐标为日期格式
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) 
    # 自动旋转日期标记
    plt.gcf().autofmt_xdate()
    #自定义x轴的刻度显示为其他样式，比如根据时间显示。 rotation设置标签旋转的角度
    plt.xticks(pd.date_range('2020-01-13','2020-02-21'),rotation=90) # 格式化时间轴标注
    #设置多格线为虚线
    plt.grid(linestyle=':') 
    #添加图例，其中’loc’参数有多种，’best’表示自动分配最佳位置
    plt.legend(loc='best') 
    #保存图片
    plt.savefig('2019-nCoV-Epidemic-Trend.png') 
    #plt.show()

if __name__ == '__main__': #只能作为主程序运行，不能作为模块导入
    plot_daily()

