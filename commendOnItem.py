# -*- coding: utf-8 -*-
"""
创建时间 Thu Oct 11 11:19:00 2018
描述:python 基于物品的协同过滤
作者:PM.liugang
"""

import numpy as np

def Jaccard(a, b):
    '''
    param a numpy or list
    param b numpy or list
    return numpy
    ------
    自定义杰卡德相似系数函数，仅对0-1矩阵有效
    '''
    return 1.0 * (a*b).sum()/(a+b-a*b).sum()

class Recommender():

    sim = None

    def similarity(self, x, distance):
        y = np.ones((len(x), len(x)))
        for i in range(len(x)):
            for j in range(len(x)):
                y[i, j] = distance(x[i], x[j])
        return y

    def fit(self, x, distance=Jaccard):
        self.sim = self.similarity(x, distance)

    def recommend(self, a):
        return np.dot(self.sim, a) * (1-a)
