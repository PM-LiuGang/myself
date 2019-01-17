# -*- coding: utf-8 -*-
"""
创建时间 Tue Jan 15 10:52:51 2019
作者:PM.liugang
描述:随机森林算法大概分为四个步骤：
通过自助法构建大小为n的一个训练集，即重复抽样选择n个训练样例
对于刚才新得到的训练集，构建一颗决策树，在每个节点执行以下操作：
1.通过不重复抽样选择d个特征
2.利用上面的d个特征，选择某种度量分割节点
重复步骤1和2，k次
对于每一个测试样例，对K颗决策树的预测结果进行投票，票数最多的结果就是随机森林的
预测结果
遗留：
"""
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append('C:\\Users\\Administrator\\Desktop\\myself')

from plotClassifierRegions import plot_decision_regions
#from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.cross_validation import train_test_split
#from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

## 准备数据
iris = datasets.load_iris()
X = iris.data[:,[2,3]]
y = iris.target
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,
                                                  random_state=0)
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
X_combined = np.vstack((X_train,X_test))
#X_combined_std = np.vstack((X_train_std,X_test_std))
y_combined = np.hstack((y_train,y_test))
forest = RandomForestClassifier(criterion='entropy',
                                n_estimators=10,
                                random_state=1,
                                n_jobs=2)
forest.fit(X_train,y_train)
plot_decision_regions(X_combined,
                      y_combined,
                      classifier=forest,
                      test_idx=range(105,150))
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend(loc='best')
plt.show()
