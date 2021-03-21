# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 07:47:14 2020

@author: adiministrator
"""
'''
利用KNN分类算法实现根据身高和体重对体型分类

窦验目的
（1）熟练安装 Python扩展库 sklearn。
（2）理解KNN分类算法的原理。
（3）了解KNN分类算法的适用问题类型。
（4）了解使用KNN分类算法解决问题的方法。

窦验内容
    KNN算法是k- Nearest Neighbor Classification的简称，也就是k近邻分类算法，属于有监督的学习算法。
基本思路是在特征空间中査找k个最相似或者距离最近的样本，然后根据k个最相似的样本对未知样本进行分类。
基本步骤如下。
（1）计算已知样本空间中所有点与未知样本的距离。
（2）对所有距离按升序排列。
（3）确定并选取与未知样本距离最小的k个样本或点。
（4）统计选取的k个点所属类别的出现频率。
（5）把出现频率最高的类别作为预测结果，即未知样本所属类别。

    假设已知样本数据，其中包含性别、身高、体重与肥胖程度的对应关系。
要求使用KNN分类算法对未知数据（性别，身高，体重）进行分类。

函数参数的意义：
sklearn.neighbors.KNeighborsClassifier()函数用于实现k近邻投票算法的分类器。

class sklearn.neighbors.KNeighborsClassifier(n_neighbors=5, weights=’uniform’, 
											algorithm=’auto’, leaf_size=30, 
											p=2, metric=’minkowski’, 
											metric_params=None, 
											n_jobs=None, **kwargs)


n_neighbors ： int，optional(default = 5)
默认情况下kneighbors查询使用的邻居数。就是k-NN的k的值，选取最近的k个点。

weights ： str或callable，可选(默认=‘uniform’)
默认是uniform，参数可以是uniform、distance，也可以是用户自己定义的函数。uniform是均等的权重，就说所有的邻近点的权重都是相等的。distance是不均等的权重，距离近的点比距离远的点的影响大。用户自定义的函数，接收距离的数组，返回一组维数相同的权重。

algorithm ： {‘auto’，‘ball_tree’，‘kd_tree’，‘brute’}，可选
快速k近邻搜索算法，默认参数为auto，可以理解为算法自己决定合适的搜索算法。除此之外，用户也可以自己指定搜索算法ball_tree、kd_tree、brute方法进行搜索，brute是蛮力搜索，也就是线性扫描，当训练集很大时，计算非常耗时。kd_tree，构造kd树存储数据以便对其进行快速检索的树形数据结构，kd树也就是数据结构中的二叉树。以中值切分构造的树，每个结点是一个超矩形，在维数小于20时效率高。ball tree是为了克服kd树高纬失效而发明的，其构造过程是以质心C和半径r分割样本空间，每个节点是一个超球体。

leaf_size ： int，optional(默认值= 30)
默认是30，这个是构造的kd树和ball树的大小。这个值的设置会影响树构建的速度和搜索速度，同样也影响着存储树所需的内存大小。需要根据问题的性质选择最优的大小。

p ： 整数，可选(默认= 2)
距离度量公式。在上小结，我们使用欧氏距离公式进行距离度量。除此之外，还有其他的度量方法，例如曼哈顿距离。这个参数默认为2，也就是默认使用欧式距离公式进行距离度量。也可以设置为1，使用曼哈顿距离公式进行距离度量。

metric ： 字符串或可调用，默认为’minkowski’
用于距离度量，默认度量是minkowski，也就是p=2的欧氏距离(欧几里德度量)。

metric_params ： dict，optional(默认=None)
距离公式的其他关键参数，这个可以不管，使用默认的None即可。

n_jobs ： int或None，可选(默认=None)
并行处理设置。默认为1，临近点搜索并行工作数。如果为-1，那么CPU的所有cores都用于并行工作。


'''
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

#已知样本数据
#每个样本数据分别为性别、身高、体重
knownData=((1,180,85),(1,180,86),(1,180,90),
           (1,180,100),(1,185,120),(1,175,80),
           (1,175,60),(1,170,70),(1,175,90),
           (1,175,100),(1,185,90),(1,185,80))

knownTarget=('稍胖','稍胖','稍胖',
             '过胖','太胖','正常',
             '偏瘦','正常','稍胖',
             '太胖','正常','偏瘦')

#创建并利用已知数据训练模型
clf=KNeighborsClassifier(n_neighbors=3, weights='distance')
clf.fit(knownData,knownTarget)

unKnownData=[(1,180,70),(1,160,90),(1,170,85)]

#对未知数据，利用训练好的模型进行分类
print('分类结果如下：')
for current in unKnownData:
    print(current,end=' : ')
    current = np.array(current).reshape(1,-1) #将输入数据转化为一行，列为-1为无效数字，即有几个数，转为几列
    print(clf.predict(current)[0]) #输出结果为列表，输出第0个元素
