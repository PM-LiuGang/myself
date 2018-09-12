# -*- coding: utf-8 -*-
"""
创建时间 Mon Sep  3 11:09:47 2018
描述:
作者:PM.liugang
"""

import numpy as np
# np.mat 将序列转换成二维矩阵 matrix类型


class Tree_node():
    def __init__(self, feat, val, right, left):
        '''
        param feat 待切分的特征,字段名称
        param val 待切分的特征值，字段值
        param right 右子树 当不在需要切分的时候，也可是是单个值
        param left 同右子树
        return 树的数据结构
        '''
        feature_to_spliton = feat  # 语法对么？
        value_of_split = val
        right_branch = right
        left_branch = left
        '''
        feature_to_spliton = self.feat # or 
        value_of_split = self.val
        right_branch = self.right
        left_branch = self.left
        '''


def regleaf(dataset):
    # 负责生成叶节点
    # 当choose best split函数确定不再对数据进行切分时，调用regleaf函数生成叶节点的模型
    # 回归树中，该模型其实就是目标变量的均值
    return np.mean(dataset[:, -1])


def regerr(dataset):
    '''
    该函数在给定数据上计算目标变量的平均误差
    np.var 均方差函数 * 行数 = 总方差
    '''
    return np.var(dataset[:, -1]) * np.shape(dataset)[0]


def choose_best_split(dataset, leaftype=regleaf, errtype=regerr, ops=(1, 4)):
    '''
    会统计不同剩余特征值的数目
    如果该数目为1，那么就不需要再切分而直接返回
    然后函数计算了当前数据集的大小和误差
    该误差S将用于与新切分误差进行对比，来检查新切分能否降低误差
    -------------------------------------------------
    param dataset 数据集 
    param leaftype 特征函数 均值
    param errtype 误差类型 总均方差
    param ops 
    return 特征编号和切分的特征值
    '''
    total_s = ops[0]  # 容许的误差下降值
    total_n = ops[1]  # 切分的最少样本数 控制函数的停止时机
    if len(set(dataset[:, -1].T.tolist()[0])) == 1:
        # if len(set(dataset[:, -1].T.A.tolist()[0])) == 1:
        # 如果所有值相等则退出
        # 生成叶节点 退出
        return None, leaftype(dataset)
    m, n = np.shape(dataset)
    s = errtype(dataset)
    best_s = np.inf
    best_index = 0
    best_value = 0
    for feat_index in range(n-1):    
        temp=dataset[:,feat_index].tolist()
        #改了这里上下两行
        for split_val in set([a[0]for a in temp]):
        #for split_val in set(dataset[:, feat_index]): #原文
        #for split_val in set((dataset[:, feat_index].T.tolist())[0]):
            mat0, mat1 = bin_split_dataset(dataset, feat_index, split_val)
            if (np.shape(mat0)[0] < total_n) or (np.shape(mat1)[0] < total_n):
                continue  # 满足上面条件，跳出，进入下一个循环
            new_s = errtype(mat0) + errtype(mat1)
            if new_s < best_s:  # 误差S与新误差对比
                best_index = feat_index
                best_value = split_val
                best_s = new_s
    if (s - best_s) < total_s:  # 总均方差-新误差 < 1
        return None, leaftype(dataset)  # 均值
    # 按照最好的值和最好的索引去分割
    mat0, mat1 = bin_split_dataset(dataset, best_index, best_value)
    if (np.shape(mat0)[0] < total_n) or (np.shape(mat1)[0] < total_n):
        return None, leaftype(dataset)  # 是否满足条件
    return best_index, best_value


def load_data_set(filename):
    '''
    读取一个文件内容到数据集里
    param filename读取文件的名称
    return 数据集[[],[]...]
    '''
    data_mat = []
    fr = open(filename)
    for line in fr.readlines():
        curline = line.strip().split('\t')
        # fltline = map(float,curline) 原文中的行 报错
        fltline = list(map(float, curline))
        data_mat.append(fltline)
    return data_mat


def bin_split_dataset(dataset, feature, value):
    '''
    param dataset 数据集合
    param feature 待切分的特征和该特征的某个值
    param value
    return 通过数组过滤方式将上述数据集合切分得到两个子集并返回  

    function->np.nonzero
    a = np.array([[0,0,3],[0,0,0],[0,0,9]])
    b = np.nonzero(a)
    print(b)
    (array([0, 2], dtype=int64), array([2, 2], dtype=int64))
    '''
#    mat0 = dataset[np.nonzero(dataset[:,feature] > value)[0],:][0]#原文
#    mat1 = dataset[np.nonzero(dataset[:,feature] <= value)[0],:][0]#原文
    mat0 = dataset[np.nonzero(dataset[:, feature] > value)[0], :]
    mat1 = dataset[np.nonzero(dataset[:, feature] <= value)[0], :]

    return mat0, mat1


def create_tree(dataset, leaftype=regleaf, errtype=regerr, ops=(1, 4)):
    '''
    param dataset 数据集
    param leaftype 给出简历树叶节点的函数
    param errtyoe 误差计算函数
    param ops 是一个包含树构建所需其他参数的元祖
    '''
    feat, val = choose_best_split(dataset, leaftype, errtype, ops)
    if feat == None:
        return val
    ret_tree = {}
    ret_tree['spInd'] = feat
    ret_tree['spVal'] = val
    lset, rset = bin_split_dataset(dataset, feat, val)
    ret_tree['left'] = create_tree(lset, leaftype, errtype, ops)
    ret_tree['right'] = create_tree(rset, leaftype, errtype, ops)
    return ret_tree


'''
mydat = regtrees.load_data_set('ex00.txt')
mymat = np.mat(mydat) # 将列表转换成二维数据
regtrees.create_tree(mymat)
Out[79]: 
{'spInd': 0,
 'spVal': 0.48813,
 'left': 1.0180967672413792,
 'right': -0.04465028571428572}
'''

'''
函数prune的伪代码如下：
基于已有的树切分测试数据：
    如果存在任一子集是一棵树，则在该自己递归剪枝过程
    计算将当前两个叶节点合并后的误差
    计算不合并的误差
    如果合并会降低误差的话，就将叶节点合并
'''


def istree(obj):
    '''
    用与测试输入变量是否是一棵树,用与判断当前处理的节点是否是叶节点
    param obj 对象
    return 返回布尔类型的结果
    '''
    return (type(obj).__name__ == 'dict')


def get_mean(tree):
    '''
    param tree 一棵树
    return 返回树的平均值
    递归函数，从上往下遍历树直到叶节点为止
    如果找到两个叶节点，则计算他们的平均值
    该函数对塌陷处理-返回树平均值
    '''
    if istree(tree['right']):  # istree 布尔型结果
        tree['right'] = get_mean(tree['right'])
    if istree(tree['left']):  # 一定是if，要左右同时计算
        tree['left'] = get_mean(tree['left'])
    return (tree['left']+tree['right'])/2.0


def prune(tree, test_data):
    '''
    param tree 待剪枝的树
    param test_data 剪枝所需要的测试数据
    return 
    np.power(x1,x2) 
    数组的元素分别求n次方 x2可以是数字，也可以是数组，但是x1和x2的列数要相同
    '''
    # 首先需要确认测试集是否为空，一旦是空，递归调用函数
    if np.shape(test_data) == 0:
        return get_mean(tree)
    if (istree(tree['right'])) or (istree(tree['left'])):
        lset, rset = bin_split_dataset(test_data, tree['spInd'], tree['spVal'])
    if istree(tree['left']):
        tree['left'] = prune(tree['left'], lset)
    if istree(tree['right']):
        tree['right'] = prune(tree['right'], rset)
    if not istree(tree['left']) and not istree(tree['right']):
        lset, rset = bin_split_dataset(test_data, tree['spInd'], tree['spVal'])
        error_no_merge = sum(np.power(lset[:, -1] - tree['left'], 2)) + \
            sum(np.power(rset[:, -1] - tree['right'], 2))
            
        tree_mean = (tree['left'] + tree['right'])/2.0
        
        error_merge = sum(np.power(test_data[:, -1] - tree_mean, 2))
        if error_merge < error_no_merge:
            print('Merging')
            return tree_mean
        else:
            return tree
    else:
        return tree
