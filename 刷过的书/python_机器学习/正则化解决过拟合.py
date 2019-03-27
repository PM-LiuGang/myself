# -*- coding: utf-8 -*-
"""
创建时间 Mon Jan  7 14:44:51 2019
作者:PM.liugang
描述:
review:190318
遗留：还是没明白C跟权重系数的关系
---------------------
L2正则:λ/2 * ‖w‖^2 = λ/2 * ∑(Wj^2) 
应用正则化：
J(w) = [损失函数] + λ/2 * ‖w‖^2
J(w) = C * [损失函数] + 1/2 * ‖w‖^2   (1/λ=C)
减小C的值，也就是增加正则系数λ的值，正则化项的威力也增强

"""
import matplotlib.pyplot as plt
import numpy as np 

from sklearn.linear_model import LogisticRegression
from sklearn import datasets
#from sklearn.cross_validation import train_test_split -> warning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

iris = datasets.load_iris()
X = iris.data[:,[2,3]] # (iris.data).shape = (150,4)
y = iris.target
print('标签共有%s类' % (len(np.unique(y))))

sc = StandardScaler()


def splitStandard(data, label, model, splitsize):
    """
    将数据分割成训练集和测试集，并对训练集和测试集标准化

    Parameters
    ----------
    data : np.ndarray
        特征数据
    label : np.ndarray
        数据分类标签
    model : model
        模型
    splitsize : float (0-1)
        按照比例分割数据集

    Returns
    -------
    xTrainStd : np.ndarray 
    xTestStd : np.ndarray
    yTrain : np.ndarray 
    yTest : np.ndarray
    """        
    xTrain, xTest, yTrain, yTest = train_test_split(data, label, 
                                                    test_size=splitsize,
                                                    random_state=0)
    model.fit(data)
    xTrainStd = model.transform(xTrain)
    xTestStd = model.transform(xTest)
    return xTrainStd, xTestStd, yTrain, yTest
        

def regularVisual(start, end, data, label):
    """
    正则化效果可视化
    
    Parameters
    ----------
    start : float
        
    end : float
        
    data : np.ndarray
        
    label : np.ndarray
        
    Returns
    -------
    图
    """
    weights = []
    params = []
    for coef in np.arange(start, end, dtype=float):
        lr = LogisticRegression(C=10**coef, random_state=0)
        lr.fit(data, label)
        weights.append(lr.coef_[1])
        params.append(10**coef)
    weights = np.array(weights)
    fig = plt.figure(figsize=(8,6), dpi=80)
    plt.plot(params, weights[:,0], label="花瓣长度")
    plt.plot(params, weights[:,1], linestyle="--", label="花瓣长度")
    plt.ylabel("权重系数")
    plt.xlabel(r"C=1/λ")
    plt.legend(loc='upper left')
    plt.xscale("log")
    fig.suptitle("随着C越来越小---->权重越来越小")
    plt.show()


if __name__ == "__main__":
    xTrainStd ,xTestStd ,yTrain, yTest = splitStandard(X, y, sc, 0.3)
    regularVisual(-5., 5., xTrainStd, yTrain)
