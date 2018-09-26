# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 22:21:18 2018
描述：4-4-6 python关联分析
@author: 刘刚
"""
import sys
import pandas as pd
import apriori # 自定义
from graphviz import Digraph

fileName = 'association.txt'

minS = 0.1  # 定义最小支持度阀值
minC = 0.38  # 定义最小置信度阀值
dataSet = apriori.createData(fileName)  # 获取格式化的数据集
L, suppData = apriori.apriori(dataSet, minSupport=minS)  # 计算得到满足最小支持度的规则
rules = apriori.generateRules(fileName, 
                              L, 
                              suppData, 
                              minConf=minC)  # 计算满足最小置信度的规则
# 关联结果报表评估
model_summary = 'data record: {1} \nassociation rules count: {0}'  # 展示数据集记录数和满足阀值定义的规则数量
print (model_summary.format(len(rules), len(dataSet)))  # 使用str.format做格式化输出
df = pd.DataFrame(rules, 
                  columns=['item1', 
                           'itme2', 
                           'instance', 
                           'support', 
                           'confidence', 
                           'lift'])  # 创建频繁规则数据框
df_lift = df[df['lift'] > 1.0]  # 只选择提升度>1的规则
print (df_lift.sort('instance', ascending=False))  # 打印排序后的数据框

# 关联结果图形展示
dot = Digraph()  # 创建有向图
graph_data = df_lift[['item1', 'itme2', 'instance']]  # 切分画图用的前项、后项和实例数数据
for each_data in graph_data.values:  # 循环读出每条规则
    node1, node2, weight = each_data  # 分割每条数据画图用的前项、后项和实例数
    node1 = str(node1)  # 转化为字符串
    node2 = str(node2)  # 转化为字符串
    label = '%s' % weight  # 创建一个标签用于展示实例数
    dot.node(node1, node1, shape='record')  # 增加节点（规则中的前项）
    dot.edge(node1, node2, label=label, constraint='true')  # 增加有向边
dot.render('apriori', view=True)  # 保存规则为pdf文件
