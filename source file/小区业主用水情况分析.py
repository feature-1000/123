# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 09:51:01 2020

@author: adiministrator

问题描述：
已知某小区所有楼号所有业主2015年到2019年每个月用水情况，该小区供66栋楼，每个楼33层，每层4户，
这些数据保存在文件“小区业主用水情况.xlsx”中，约52万条数据，格式如下，其中房号前两位表示楼号
（01-66）、中间两位表示楼层（01-33），最后两位表示房号（01-04）。
现在要求统计出该小区每年每个楼的用水大户，也就年度用水量最大的业主房号。

技术要点：
缺失值填充，数据分组，筛选，字符串接口，透视表。

"""
import pandas as pd
#读取数据，指定每列的数据类型
#避免自动转换类型，还可以提高读取速度
df=pd.read_excel('小区业主用水情况.xlsx',dtype={'日期':str,'房号':str,'用水量（立方）':float})
#日期保留年份
df.日期=df.日期.str.slice(0,4)  #切片，对日期的前四位保留，即年份,slice()方法提取一个字符串的一部分,并返回一新的字符串
df.columns=['年份']+list(df.columns.values[1:])  #将列标签'日期'改为’年份‘

#缺失值替换为该小区整体月用水平均值
df.iloc[:,2].fillna(round(df.iloc[:,2].mean()),inplace=True)  #用fillna()填充缺失值，round(x) 返回浮点数x的四舍五入的值
#按年份，房号分组，每个月的用水量求和,且年份，房号列的数据不作为DF的index
df=df.groupby(by=['年份','房号'],as_index=False).sum()
#查找每年每幢楼的用水总量最大的房号
data=[]
for year in sorted(set(df.年份.values)):       #从2015，2016，2017，2018，2019遍历
    for building_number in sorted(set(df.房号.str.slice(0,2).values)):  #从01到66遍历
        #筛选指定年份的楼号的数据，构成一个子dataframe对象（筛选数据）
        df_temp=df[(df.年份==year)&(df.房号.str.startswith(building_number))]
        #将该年份、楼号中，用水总量最大的房号的所有数据（选排名第一的）追加到列表data
        data.extend(df_temp.nlargest(1,'用水量（立方）').values)
#获取了每一年每一幢楼的最大用水户的数据列表
#将其整理成dataframe格式，列标签与原始数据列标签一致
df_new=pd.DataFrame(data,columns=df.columns)
#在新数据框中增加一列“楼号”，即房号的前两位
df_new['楼号']=df_new.房号.str.slice(0,2)
print(df_new) 

print(df_new.pivot(index='楼号',columns='年份',values='房号')) #pivot()行转列,透视表

