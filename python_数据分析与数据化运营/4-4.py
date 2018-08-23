# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 23:49:19 2018

@author: 刘刚
"""

import os,sys

import pandas as pd
from graphviz import Digraph

import apriori

os.chdir('C:\\python\\python_数据分析与数据化运营\\chapter4')
sys.path.append('../chapter4')

filename = 'association.txt'

mins = 0.1
minc = 0.38

dataset = apriori.createData(filename)
l,suppdata = apriori.apriori(dataset,minSupport=mins)
rules = apriori.generateRules(filename,l,suppdata,minConf=minc)

model_summary = 'data record: {1} \nassociation rules count: {0}'
print(model_summary.format(len(rules),len(dataset)))
df = pd.DataFrame(rules,columns=['item1','item2','instance','support','confidence',\
                                 'lift'])
df_lift = df[df['lift'] > 1.0]
print(df_lift.sort_values('instance',ascending=False))

dot = Digraph()
graph_data = df_lift[['item1','item2','instance']]

for each_data in graph_data.values:
    node1,node2,weight = each_data
    node1 = str(node1)
    node2 = str(node2)
    label = '%s' % weight
    dot.node(node1,node1,shape='record')
    dot.egde(node1,node2,label=label,constraint='true')
dot.render('apriori',view=True)