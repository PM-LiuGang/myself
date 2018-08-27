# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:03:07 2018
Description:K-近邻算法
机器学习实战中K-近邻算法
Author: pm.liugang
判断逻辑
对未知类别属性的数据集中的每个点依次执行以下操作
计算已知类别数据集中的点与当前点之间的距离
按照距离递增次序排序
选取与当前点距离最小的K个点
确定前K个点所在类别的出现频率
返回前K个点出现频率最高的类别作为当前点的预测分类
"""
import numpy as np
import operator

def createdataset():
    group = np.array([[1.0,1.1],
                     [1.0,1.0],
                     [0,0],
                     [0,0.1]])
    labels = list('AABB')
    return group,labels

def classify0(inx,dataset,labels,k):
    '''
    param inx 用于分类的输入向量 
    param dataset 输入的训练样本集
    param labels 标签向量
    param k 最近邻居的数目
    '''
    datasetsize = dataset.shape[0]
    #np.tile Construct an array by repeating A the number of times given by reps
    diffmat = np.tile(inx,(datasetsize,1)) - dataset
    sqdiffmat = diffmat ** 2
    sqdistance = sqdiffmat.sum(axis=1)
    distance = sqdistance ** 0.5
    sorteddistindicies = distance.argsort()
    classcount = {}
    for i in range(k):
        voteilabel = labels[sorteddistindicies[1]]
        #D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
        classcount[voteilabel] = classcount.get(voteilabel,0) + 1
    sortedclasscount = sorted(classcount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedclasscount[0][0]

def file2matrix(filename):
    '''
    param filename 文件名称的字符串
    总共1000行，3种特征 每年获得的飞行常客里程数 玩视频游戏所耗时间百分比 每周消费的冰淇淋公升数
    return 训练样本矩阵和类标签向量 array和int类型
    '''      
    fr = open(filename)
    array_lines = fr.readlines()
    number_of_lines = len(array_lines)
    return_mat = np.zeros((number_of_lines,3))
    class_label_vector = []
    index = 0
    for line in array_lines:
        line = line.strip()
        list_from_line = line.split('\t')
        return_mat[index,:] = list_from_line[0:3]
        class_label_vector.append(int(list_from_line[-1]))
        index += 1 # 逐行遍历
    return return_mat,class_label_vector

d1,l1 = file2matrix('datingTestSet2_1.txt')

#matplot作图
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
#利用变量l1存储的类标签属性，在散点图上绘制了色彩不等，尺寸不同的点
ax.scatter(d1[:,1],d1[:,2],s=15*np.array(l1),c=15*np.array(l1),marker='^')
plt.show()

#plotpl作图
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot
#也同样可以color = np.array定义不同标签的颜色
trace0 = go.Scatter(x=d1[:,0],y=d1[:,1],mode='markers',name='scatters',marker = dict(color=np.array(l1)))
pyplt([trace0],filename = 'scatters.html')
