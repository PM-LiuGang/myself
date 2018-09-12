# -*- coding: utf-8 -*-
"""
创建时间 Wed Sep 12 14:28:36 2018
描述:来源机器学习实战，非导包方式实现SVM
作者:PM.liugang
"""
import random

def loadDataSet(fileName):
    '''
    param 文件名称
    return 训练集和标签集
    '''
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat


def selectJrand(i, m):
    '''
    param i 第一个a的下表
    param m 所有a的数目
    '''
    j = i # 进入循环
    while j == i:
        # random.uniform return values between 0 and m
        j = int(random.uniform(0, m)) # 一轮游
    return j


def clipAlpha(aj, H, L):
    '''
    调整大于H或小于L的alpha的值
    param H >H =H
    param L <L =L
    '''
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj

def smoSimple(dataMatin,classLabels,C,toler,maxIter):
    pass