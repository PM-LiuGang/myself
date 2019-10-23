# -*- coding: utf-8 -*-
"""
创建时间：Wed Feb 20 21:27:28 2019
描述：以线性回归模型为例子，此脚本用于展示如何保存和读取模型
作者: PM.LiuGang
Review:
遗留：
"""

import numpy as np
import pandas as pd
import pickle

from sklearn import linear_model
from sklearn2pmml import PMMLPipeline
from sklearn2pmml import sklearn2pmml


def readData(path):
    '''
    读取数据
    '''
    data = pd.read_csv(path)
    return data


def saveAsPMML(data, modelPath):
    '''
    利用sklearn2pmml将模型存储为PMML
    
    Parameters
    ----------
    data : pd.DataFrame
        train data
    modelPath : 
    
    Returns
    -------
    local-model linear.pmml
    
    See also
    --------
    PMML(steps)
    steps : list
    List of (name, transform) tuples (implementing fit/transform) that are
    chained, in the order in which they are chained, with the last object
    an estimator
    
    sklearn2pmml(
                PMMLPipeline/The pipeline,
                The path to where the PMML document should be stored,
                If true, insert the string representation of pipeline into the PMML document)
    '''
    model = PMMLPipeline([('regressor',linear_model.LinearRegression())])
    model.fit(data[['x']], data[['y']])
    sklearn2pmml(model, 'linear.pmml', with_repr=True)
    
    
def trainAndSaveModel(data, modelPath):
    '''
    使用pickle保存训练好的模型
    '''
    model = linear_model.LinearRegression()
    model.fit(data[['x']], data[['y']])
    pickle.dump(model, open(modelPath, 'wb'))
    return model


def loadModel(modelPath):
    '''
    使用pickle读取已有模型
    '''
    model = pickle.load(open(modelPath, 'rb'))
    return model


if __name__ == '__main__':
    dataPath = 'simple_example.csv'
    data = readData(dataPath)
    modelPath = 'linear_model'
    originalModel = trainAndSaveModel(data, modelPath)
    model = loadModel(modelPath)
    print('保存的模型对1的预测值' % originalModel.predict([[1]]))
    print('读取的模型对1的预测值' % model.predict([[1]]))
    saveAsPMML(data, 'linear.pmml')
    