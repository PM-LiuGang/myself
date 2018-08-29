# -*- coding: utf-8 -*-
"""
创建时间 Wed Aug 29 10:45:49 2018
来源 机器学习实战
非导包方式实现决策树
作者:PM.liugang
"""
from math import log

def calc_shan_non_ent(dataset):
    '''
    计算香农熵
    param 数据集，类型[] 或 numpy
    retrun 香农熵 类型值
    '''
    num_entries = len(dataset) # 4
    label_counts = {}
    for featvec in dataset:#遍历数据集
        current_label = featvec[-1]#取数据集最后一个列 = yes or no
        if current_label not in label_counts.keys():
            label_counts[current_label] = 0#如果当前标签不在，则计数为0
        label_counts[current_label] += 1#如果标签存在，则计数加1，yes:1 no:3
    shan_non_ent = 0.0 # 香农熵？
    for key in label_counts: #遍历标签计数 字典中的键
        prob = float(label_counts[key])/num_entries
        #prob= yes 25% | no 75%
        #I(Xi) = -log2(p(Xi))
        #H = -∑(i-1，n)p(Xi)log2(p(Xi))
        #∑通过 -= 实现
        shan_non_ent -= prob * log(prob,2)#以2为底
    return shan_non_ent
        
def create_data_set():
    '''
    创建测试数据集
    '''
    dataset = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataset,labels

def split_dataset(dataset,axis,value):
    '''
    按照给定特征划分数据集
    param dataset 数据集
    param axis 划分数据集的特征 索引位置
    param 需要返回特征的值
    return 列表嵌套列表
    dataset = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    return [[1, 'yes'], [1, 'yes'], [0, 'no']]
    '''
    ret_dataset = []
    for featvec in dataset:
        if featvec[axis] == value:
            reduce_featvec = featvec[:axis]
            #[].extend([]) 命令执行后，不返回结果.[]
            #[].append([]) 命令执行后，返回(,,,[])
            reduce_featvec.extend(featvec[axis+1:])
            ret_dataset.append(reduce_featvec)
    return ret_dataset # ![,,value,,,,]

def choose_best_feature_tosplit(dataset):
    '''
    选择最好的数据集划分方式
    '''
    num_features = len(dataset[0]) - 1 # 特征数量
    base_entropy = calc_shan_non_ent(dataset)
    best_info_gain = 0.0
    best_feature = -1
    for i in range(num_features):
        feat_list = [example[i] for example in dataset]
        unique_vals = set(feat_list)
        new_entropy = 0.0
        for value in unique_vals:
            sub_dataset = split_dataset(dataset,i,value)
            prob = len(sub_dataset)/float(len(dataset))
            new_entropy += prob * calc_shan_non_ent(sub_dataset)
        infogain = base_entropy - new_entropy
        if infogain > best_info_gain:
            best_info_gain = infogain
            best_feature = i
    return best_feature

    