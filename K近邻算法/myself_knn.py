# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:03:07 2018
Description:K-近邻算法
Author: pm.liugang
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
    :param inx 用于分类的输入向量 
    :param dataset 输入的训练样本集
    :param labels 标签向量
    :param k 最近邻居的数目
    '''
    datasetsize = dataset.shape[0]
    diffmat = np.tile(inx,(datasetsize,1)) - dataset
    sqdiffmat = diffmat ** 2
    sqdistance = sqdiffmat.sum(axis=1)
    distance = sqdistance ** 0.5
    sorteddistindicies = distance.argsort()
    classcount = {}
    for i in range(k):
        voteilabel = labels(sorteddistindicies(1))
        classcount(voteilabel) = classcount.get(voteilabel,0) + 1
    sortedclasscount = sorted(classcount.items(),key=operator.itemgetter(1)\
                              ,reversed=True)
    return sortedclasscount[0][0]

        
