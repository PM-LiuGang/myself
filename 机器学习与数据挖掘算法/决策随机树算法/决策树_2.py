# -*- coding: utf-8 -*-
"""
创建时间 Wed Aug 29 10:45:49 2018
来源 机器学习实战
非导包方式实现决策树
作者:PM.liugang
"""
import operator

from math import log


def calc_shan_non_ent(dataset):
    '''
    计算香农熵
    param 数据集，类型[] 或 numpy
    retrun 香农熵 类型值
    '''
    num_entries = len(dataset)  # 4
    label_counts = {}
    for featvec in dataset:  # 遍历数据集
        current_label = featvec[-1]  # 取数据集最后一个列 = yes or no
        if current_label not in label_counts.keys():
            label_counts[current_label] = 0  # 如果当前标签不在，则计数为0
        label_counts[current_label] += 1  # 如果标签存在，则计数加1，yes:1 no:3
    shan_non_ent = 0.0  # 香农熵？
    for key in label_counts:  # 遍历标签计数 字典中的键
        prob = float(label_counts[key])/num_entries
        # prob= yes 25% | no 75%
        # I(Xi) = -log2(p(Xi))
        # H = -∑(i-1，n)p(Xi)log2(p(Xi))
        # ∑通过 -= 实现
        shan_non_ent -= prob * log(prob, 2)  # 以2为底
    return shan_non_ent


def create_data_set():
    '''
    创建测试数据集
    '''
    dataset = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataset, labels


def split_dataset(dataset, axis, value):
    '''
    按照给定特征值划分数据集
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
            # [].extend([]) 命令执行后，不返回结果.[]
            # [].append([]) 命令执行后，返回(,,,[])
            reduce_featvec.extend(featvec[axis+1:])
            ret_dataset.append(reduce_featvec)
    return ret_dataset  # ![,,value,,,,]


def choose_best_feature_tosplit(dataset):
    '''
    选择最好的数据集划分方式
    '''
    num_features = len(dataset[0]) - 1  # 特征数量
    base_entropy = calc_shan_non_ent(dataset)  # 整个数据集的熵
    best_info_gain = 0.0
    best_feature = -1
    for i in range(num_features):  # 遍历数据集中的所有特征=2
        # 数据每次遍历生成一个内容，放到列表里
        # dataset = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
        # feat_list = [1,1,1,0,0]
        feat_list = [example[i] for example in dataset]
        unique_vals = set(feat_list)  # unique_vals = {0,1}
        new_entropy = 0.0
        for value in unique_vals:
            sub_dataset = split_dataset(dataset, i, value)  # 对每个唯一属性值划分一次数据集
            # i,value = 0,0 0,1 1,0,1,1
            # I(Xi) = -log2(p(Xi))
            # H = -∑(i-1，n)p(Xi)log2(p(Xi))
            # ∑通过 -= 实现
            prob = len(sub_dataset)/float(len(dataset))  # 每个特征向量被均匀的选择的概率
            #为什么不是prob * log(prob,2)
            new_entropy += prob * calc_shan_non_ent(sub_dataset)
        infogain = base_entropy - new_entropy
        if infogain > best_info_gain:
            best_info_gain = infogain
            best_feature = i
    return best_feature


'''
import 决策树_2 as trees

mydat,labels = trees.create_data_set()

trees.choose_best_feature_tosplit(mydat)
Out[68]: 0

mydat
Out[69]: [[1, 1, 'yes'], [1, 1, 'yes'], \
[1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
第一个特征为1进行划分很好的处理相关数据
'''


def majority_cnt(class_list):
    '''
    对分类进行排序
    param 分类列表
    return 返回出现次数最多的分类名称（已排序）
    '''
    class_count = {}
    for vote in class_list:
        if vote not in class_count.keys():  # 如果没有这个键，默认设置这个键为0
            class_count[vote] = 0
        class_count[vote] += 1  # 如果存在这个键，值加1
    sorted_class_count = sorted(class_count.items(),
                                key=operator.itemgetter(1), reverse=True)  # 按照 值 排序
    return sorted_class_count[0][0]


def create_tree(dataset, labels):
    '''
    创建树
    param dataset 数据集
    param labels 包含了数据集中所有特征的标签
    return 
    '''
    classlist = [example[-1] for example in dataset]  # 取所有数据集的类标签
    # 第一个停止条件：类别完全相同则停止继续划分，直接返回该类标签
    # classlist = ['yes','yes','yes']
    # classlist.count(classlist[0]) 3
    # len(classlist) 3
    if classlist.count(classlist[0]) == len(classlist):
        return classlist[0]
    # 遍历完所有特征时返回出现次数最多的
    # 第二个停止条件使用完了所有特征，仍然不能将数据集划分成仅包含仅包含唯一类别的分组
    # 由于第二个条件无法简单的返回唯一的类标签，使用函数挑选出现次数最多的类别作为返回值
    if len(dataset[0]) == 1:
        return majority_cnt(classlist)
    #创建树
    #当前数据集选取最好特征储存在变量beat feat中
    best_feat = choose_best_feature_tosplit(dataset)
    best_feat_label = labels[best_feat]
    mytree = {best_feat_label: {}}
    # 得到列表包含的所有属性值
    del(labels[best_feat])
    feat_values = [example[best_feat] for example in dataset]
    unique_vals = set(feat_values)
    for value in unique_vals:#遍历当前选择特征包含的所有属性值
        sub_labels = labels[:]#复制类标签 新变量代替原始列表
        mytree[best_feat_label][value] = create_tree(split_dataset
                                                     (dataset, best_feat, value), sub_labels)
    return mytree
'''
mydat,labels = trees.create_data_set()

mydat,labels
Out[94]: 
([[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']],
 ['no surfacing', 'flippers'])

mytree = trees.create_tree(mydat,labels)

mytree
Out[96]: {'no surfacing': 
         {0: 'no', 
          1: {'flippers': 
             {0: 'no', 
              1: 'yes'}}}}

no surfacing 第一个划分数据集的特征名称
3个叶子节点 2个判断节点
'''
# 使用Matplotlib注解绘制树形图的章节略去，用plt画的图太过难看
# from pyecharts import Tree 报错，不存在tree
# import json
# with open('json1.json','r',encoding='utf-8') as f：
#   data = json.load(f)
#   报错 except value

#如何利用决策树执行数据分类，用于实际数据分类

def classify(input_tree,feat_labels,test_vec):
    '''
    使用决策树的分类函数
    param input_tree 类型?
    param feat_labels
    param test_vec
    return 
    '''
    first_str = input_tree.keys()[0]#取出输入的第一个键
    second_dict = input_tree[first_str]#将标签字符串转换为索引
    feat_index = feat_labels.index(first_str)
    for key in second_dict.keys():
        if test_vec[feat_index] == key:
            if type(second_dict[key]).__name__ == 'dict':
                #这可以直接调用classify么？在定义classify函数里
                class_label = classify(second_dict[key],feat_labels,test_vec)
            else:
                class_label = second_dict[key]
    return class_label
