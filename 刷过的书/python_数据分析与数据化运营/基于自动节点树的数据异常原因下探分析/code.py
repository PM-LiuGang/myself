# -*- coding: utf-8 -*-
"""
创建时间 Sat Dec 22 20:11:35 2018
作者: PM.LiuGang
描述：基于自动节点树的数据异常原因下探分析
未解决：HTML中的表格
"""
# import sys
import datetime
import pandas as pd
import numpy as np

from graphviz import Digraph

# reload(sys)
# sys.setdefaultencoding('utf-8')

rawData = pd.read_csv('advertising_data.csv')

print('{:*^60}'.format('数据总览:'))
print(rawData.head(2))
print('{:*^60}'.format('数据类型:'))
print(rawData.dtypes)

# 数据预处理
rawData['visit'] = rawData['visit'].replace('-', 0).astype(np.int64)
rawData['date'] = pd.to_datetime(rawData['date'], format='%Y/%m/%d')

print('数据预处理')
print('{:*^60}'.format('数据总览:'))
print(rawData.head(2))
print('{:*^60}'.format('数据类型:'))
print(rawData.dtypes)

daySummary = rawData.iloc[:, -1].groupby(rawData.iloc[:, 0]).sum()
dayChangeValue = daySummary.diff(1).rename('change')
dayChangeRate = (dayChangeValue.shift(-1) / daySummary).round(3).\
    rename('change_rate').shift(1)
daySummaryTotal = pd.concat((daySummary, dayChangeValue, dayChangeRate),
                            axis=1)
print('{:*^60}'.format('变换后的数据类型:'))
print(daySummaryTotal)

# 指定日期自动下探分解
theDay = pd.datetime(2017, 6, 7)
previousDay = theDay - datetime.timedelta(1)  # day=1 error
theDataTmp = rawData[rawData['date'] == theDay].\
    rename(columns={'visit': theDay})
previousDataTmp = rawData[rawData['date'] == previousDay].\
    rename(columns={'visit': previousDay})

dimensionList = ['source', 'site', 'channel', 'media']  # 原数据中的字段
splitNodeList = ['全站']
changeList = list()
increaseNodeList = []
decreaseNodeList = []
## 计算指定维度下的数据
for dimension in dimensionList:
    theDataMerge = theDataTmp[[dimension, theDay]]
    previousDataMerge = previousDataTmp[[dimension, previousDay]]
    theDayGroupby = pd.DataFrame(theDataMerge.iloc[:, -1].
                                 groupby(theDataMerge.iloc[:, 0]).sum())
    previousDayGroupby = pd.DataFrame(previousDataMerge.iloc[:, -1].
                                      groupby(previousDataMerge.iloc[:, 0]).sum())
    ## 将两天的数据合并计算其变化量和变化率
    mergeData = pd.merge(theDayGroupby, previousDayGroupby,
                         how='outer',
                         left_index=True,
                         right_index=True)
    mergeData = mergeData.fillna(0)
    ## 环比变化量和环比变化率
    mergeData['change'] = mergeData[theDay] - mergeData[previousDay]
    mergeData['change_rate'] = mergeData['change'] / mergeData[previousDay]
    # mergeData[mergeData['change'] == np.inf] = 0 # 自增
    # mergeData[mergeData['change_rate'] == np.inf] = 0 # 自增
    totalChange = mergeData['change'].sum()
    changeList.append(totalChange)
    ## 计算当前维度下变化量最大值对应的各项想信息
    mergeData = mergeData.sort_values(by='change')
    maxIncreaseNode = mergeData.iloc[-1, :].name
    maxValue, maxRate = mergeData.iloc[-1, :][2:4]
    increaseNodeList.append([maxIncreaseNode, int(maxValue), maxRate])
    ## 计算当前维度下变化量最小值对应的各项想信息
    minIncreaseNode = mergeData.iloc[0, :].name
    minValue, minRate = mergeData.iloc[0, :][2:4]
    decreaseNodeList.append([minIncreaseNode, int(minValue), minRate])
    ## 针对增长趋势的数据做逐层数据过滤
    if totalChange >= 0:
        splitNodeList.append(maxIncreaseNode)
        rulesLen = len(splitNodeList)
        if rulesLen == 2:
            theDataTmp = theDataTmp[theDataTmp['source'] == maxIncreaseNode]
            previousDataTmp = previousDataTmp[previousDataTmp['source'] ==
                                              maxIncreaseNode]
        elif rulesLen == 3:
            theDataTmp = theDataTmp[theDataTmp['site'] == maxIncreaseNode]
            previousDataTmp = previousDataTmp[previousDataTmp['site'] ==
                                              maxIncreaseNode]
        elif rulesLen == 4:
            theDataTmp = theDataTmp[theDataTmp['channel'] == maxIncreaseNode]
            previousDataTmp = previousDataTmp[previousDataTmp['channel'] ==
                                              maxIncreaseNode]
        elif rulesLen == 5:
            theDataTmp = theDataTmp[theDataTmp['media'] == maxIncreaseNode]
            previousDataTmp = previousDataTmp[previousDataTmp['media'] ==
                                              maxIncreaseNode]
    ## 针对下降趋势的数据做逐层数据过滤
    else:
        splitNodeList.append(minIncreaseNode)
        rulesLen = len(splitNodeList)
        if rulesLen == 2:
            theDataTmp = theDataTmp[theDataTmp['source'] == minIncreaseNode]
            previousDataTmp = previousDataTmp[previousDataTmp['source'] ==
                                              minIncreaseNode]
        elif rulesLen == 3:
            theDataTmp = theDataTmp[theDataTmp['site'] == minIncreaseNode]
            previousDataTmp = previousDataTmp[previousDataTmp['site'] ==
                                              minIncreaseNode]
        elif rulesLen == 4:
            theDataTmp = theDataTmp[theDataTmp['channel'] == minIncreaseNode]
            previousDataTmp = previousDataTmp[previousDataTmp['channel'] ==
                                              minIncreaseNode]
        elif rulesLen == 5:
            theDataTmp = theDataTmp[theDataTmp['media'] == minIncreaseNode]
            previousDataTmp = previousDataTmp[previousDataTmp['media'] ==
                                              minIncreaseNode]
#画图展示自动下探结果
## 定义节点树形图形图用到属性和样式
'''
{0} 表示第一个对应变量的数据
{1:d} 表示第二个对应变量的数据，填充的数据类型为整数型
{2:.0%} 表示第二个对应变量的数据，填充的数据类型为百分比类型，保留0位小数
'''
nodeStyle = {'fontname': 'Simsun', 'shape': 'box'}
edgeStyle = {'fontname': 'SimHei', 'fontsiez': '11'}
## 具体释义 链接 p426
### 定义顶部node节点标签样式
top_node_style = '<<table><tr><td bgcolor="black"><font color="white">{0}</font></td></tr><tr><td>环比变化量:{1:d}</td></tr><tr><td>环比变化率:{2:.0%}</td></tr></table>>'
### 定义左侧node节点标签样式
left_node_style = '<<table><tr><td bgcolor="chartreuse"><font color="black">{0}</font></td></tr><tr><td>环比变化量:{1}</td></tr><tr><td>环比变化率:{2:.0%}</td></tr></table>>'
### 定义右侧node节点标签样式
right_node_style = '<<table><tr><td bgcolor="lightblue"><font color="black">{0}</font></td></tr><tr><td>环比变化量:{1}</td></tr><tr><td>环比变化率:{2:.0%}</td></tr></table>>'
dot = Digraph(format='png', node_attr=nodeStyle, edge_attr=edgeStyle)
## 获取每一层分裂节点的信息
for i in range(4):
    nodeName = splitNodeList[i]
    nodeLeft, maxValue, maxRate = increaseNodeList[i]
    nodeRight, minValue, minRate = decreaseNodeList[i]
    nodeChange = changeList[i]
    nodeLabelLeft = left_node_style.format(nodeLeft, maxValue, maxRate)
    nodeLabelRight = right_node_style.format(nodeRight, minValue, minRate)
    ### 定义顶级节点信息
    if i == 0:
        dayData = daySummaryTotal[daySummaryTotal.index == theDay]
        formerData = dayData.iloc[0, 1]
        nodeLabel = top_node_style.format(
            nodeName, int(formerData), dayData.iloc[0, 2])
        dot.node(nodeName, label=nodeLabel)

    ### 分别定义左侧和右侧边显示的贡献率信息
    contributionRate_1 = float(maxValue) / formerData
    contributionRate_2 = float(minValue) / formerData

    if nodeChange >= 0:
        edgeLabelLeft = '正向贡献率:{0:.0%}'.format(contributionRate_1)
        edgeLabelRight = '反向贡献率:{0:.0%}'.format(contributionRate_2)
        formerData = maxValue
    else:
        edgeLabelLeft = '反向贡献率:{0:.0%}'.format(contributionRate_1)
        edgeLabelRight = '正向贡献率:{0:.0%}'.format(contributionRate_2)
        formerData = minValue

    ### 建立节点，边并输入图形
    dot.node(nodeLeft, label=nodeLabelLeft)
    dot.node(nodeRight, label=nodeLabelRight)
    dot.edge(nodeName, nodeLeft, label=edgeLabelLeft, color='chartreuse')
    dot.edge(nodeName, nodeRight, label=edgeLabelRight, color='lightblue')
# 展示图形结果
dot.view('change summary', cleanup=True)
