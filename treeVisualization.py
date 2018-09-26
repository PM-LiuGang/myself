# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 22:24:24 2018
描述: 可视化决策树
作者: 刘刚
"""
import pydotplus

from sklearn import tree

model_tree = tree.DecisionTreeClassifier(random_state=0)
model_tree.fit(,)
pre_y = model_tree.predict()

name_list = []
'''保存决策树规则图为PDF文件'''
# feature_names number = n_features number
dot_data = tree.export_graphviz(model_tree, 
                                out_file=None, # 控制不生成dot文件
                                max_depth=5, # 分类规则的最大深度
                                feature_names=names_list, # 决策树规则每个变量的名称
                                filled=True,  # 控制填充
                                rounded=True)  # 控制字体样式
graph = pydotplus.graph_from_dot_data(dot_data)  # 通过pydotplus将决策树规则解析为图形
graph.write_pdf("Tree.pdf")  # 将决策树规则保存为PDF文件
