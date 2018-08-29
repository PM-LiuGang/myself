# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:03:07 2018
Description:K-近邻算法
机器学习实战中K-近邻算法
Author: pm.liugang

"""
import numpy as np
import operator
from sklearn.preprocessing import MinMaxScaler


def create_dataset():
    group = np.array([[1.0, 1.1],
                      [1.0, 1.0],
                      [0, 0],
                      [0, 0.1]])
    labels = list('AABB')
    return group, labels


def classify0(inx, dataset, labels, k):
    '''
    description 
    流程：
    1.对未知类别属性的数据集中的每个点依次执行以下操作
    2.计算已知类别数据集中的点与当前点之间的距离
    3.按照距离递增次序排序
    4.选取与当前点距离最小的K个点
    5.确定前K个点所在类别的出现频率
    6.返回前K个点出现频率最高的类别作为当前点的预测分类

    param inx 用于分类的输入 向量 ,也就是一个行数，一个点
    param dataset 输入的训练样本集
    param labels 标签向量
    param k 最近邻的数目
    return labels中的标签
    '''
    datasetsize = dataset.shape[0]  # 获取数据集的维数
    # np.tile Construct an array by repeating A the number of times given by reps
    # 分类器基于欧氏距离 d = ((xA0 - xB0) ** 2 + (xA1 - xB1) ** 2) ** 0.5
    diffmat = np.tile(inx, (datasetsize, 1)) - dataset
    sqdiffmat = diffmat ** 2
    sqdistance = sqdiffmat.sum(axis=1)
    distance = sqdistance ** 0.5
    # 上面步骤 求d
    # y=np.array([1,4,3,-1,6,9]).argsort() y=array([3,0,2,1,4,5])。
    sorteddistindicies = distance.argsort()  # 流程3
    classcount = {}
    for i in range(k):  # k邻近的数目
        voteilabel = labels[sorteddistindicies[1]]
        # D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
        classcount[voteilabel] = classcount.get(voteilabel, 0) + 1
        # 按字典的值进行排序
    sortedclasscount = sorted(
        classcount.items(), key=operator.itemgetter(1), reverse=True)
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
    return_mat = np.zeros((number_of_lines, 3))
    class_label_vector = []
    index = 0
    for line in array_lines:
        line = line.strip()
        list_from_line = line.split('\t')
        return_mat[index, :] = list_from_line[0:3]
        class_label_vector.append(int(list_from_line[-1]))
        index += 1  # 逐行遍历
    return return_mat, class_label_vector


d1, l1 = file2matrix('datingTestSet2_1.txt')
'''
#matplot作图 书中
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
#利用变量l1存储的类标签属性，在散点图上绘制了色彩不等，尺寸不同的点
ax.scatter(d1[:,1],d1[:,2],s=15*np.array(l1),c=15*np.array(l1),marker='^')
plt.savefig('scatter.png')#这里保存图片怎么生效？

#plotly作图 扩展
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot
#也同样可以color = np.array定义不同标签的颜色
trace0 = go.Scatter(x=d1[:,0],y=d1[:,1],mode='markers',name='scatters',marker = dict(color=np.array(l1)))
pyplt([trace0],filename = 'scatters.html')
'''


def auto_norm(data_set):
    '''
    归一化数值 
    param data_set 数据集 类型numpy
    return 归一化后的矩阵(1000,3) 最大最小值的差(3,) 最小值(3,)
    '''
    # new value = (old value - min )/(max - min)采用公式
    min_vals = data_set.min(0)  # 按列求最小值
    max_vals = data_set.max(0)
    ranges = max_vals - min_vals  # max-min
    norm_data_set = np.zeros(np.shape(data_set))
    m = data_set.shape[0]
    norm_data_set = data_set - np.tile(min_vals, (m, 1))  # old-min
    norm_data_set = norm_data_set/np.tile(ranges, (m, 1))  # /
    return norm_data_set, ranges, min_vals


# 另一种归一化数值 MinMax标准化 [0,1]
minmax = MinMaxScaler()
data_minmax = minmax.fit_transform(d1)


def dating_class_test():
    '''
    计算错误率
    '''
    horatio = 0.10
    dating_data_mat, dating_labels = file2matrix(
        'datingTestSet2_1.txt')  # 读取数据
    norm_mat, ranges, min_vals = auto_norm(dating_data_mat)  # 归一化数据
    m = norm_mat.shape[0]  # 获取数据集行数
    num_test_vecs = int(m * horatio)  # 取10%的数据作为测试集
    errorcount = 0.0
    for i in range(num_test_vecs):
        # 训练数据 100:1000
        classifier_result = classify0(norm_mat[i, :], norm_mat[num_test_vecs:m, :],
                                      dating_labels[num_test_vecs:m], 3)
        print('the classifier came back with: %d, the real answer is: %d'
              % (classifier_result, dating_labels[i]))
        if classifier_result != dating_labels[i]:
            errorcount += 1.0
    # float(num_test_vecs=100)
    print('the total error rate is %f' % (errorcount/float(num_test_vecs)))


def classify_person():
    result_list = ['not at all', 'is small doses', 'in large doses']
    precenttacts = float(
        input('Percentage of time spend playing video games?'))
    ffmlies = float(input('Frequent flier miles earned per year?'))
    icecream = float(input('liters of ice cream consumed per year?'))
    # 读数据
    dating_data_mat, dating_labels = file2matrix('datingTestSet2_1.txt')
    # 数据归一化
    norm_mat, ranges, minvale = auto_norm(dating_data_mat)
    in_arr = np.array([ffmlies, precenttacts, icecream])
    # 分类
    classifier_result = classify0(
        in_arr-minvale/ranges, norm_mat, dating_labels, 3)

    print('You wii probably like this person: ',
          result_list[classifier_result - 1])
