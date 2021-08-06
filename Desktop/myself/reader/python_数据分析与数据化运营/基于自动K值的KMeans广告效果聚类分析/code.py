# -*- coding: utf-8 -*-
"""
描述：
创建时间：Wed Jan  2 20:51:38 2019
作者: PM.LiuGang
Review:20200328
遗留：
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn import metrics

rawData = pd.read_csv('ad_performance.txt', delimiter='\t')

print('{:*^60}'.format('Data overview:'))
print(rawData.head())

print('{:*^60}'.format('Data dtypes:'))
print((rawData.dtypes).T)

print('{:*^60}'.format('NA counts:'))
print(pd.DataFrame(rawData.isnull()).sum().T)

print('{:*^60}'.format('Data Describe'))
print(rawData.describe().round(2).T)  # 波动非常大 有缺失值 最小值和分位数值不对

print('{:*^60}'.format('Correlation Analysis:'))
print(rawData.corr().round(2).T)

dataFillna = rawData.fillna(rawData['平均停留时间'].mean())  # 有缺失值

converCols = ['素材类型', '广告类型', '合作方式', '广告尺寸', '广告卖点']
converMatrix = dataFillna[converCols]
lines = dataFillna.shape[0]
dictList = []
uniqueList = []

for colName in converCols:
    '''
    uniqueList=[['jpg', 'swf', 'gif', 'sp'],
     ['banner', 'tips', '不确定', '横幅', '通栏', '暂停'],
     ['roi', 'cpc', 'cpm', 'cpd'],
     ['140*40','308*388','450*300','600*90','480*360','960*126','900*120',
     '390*270'],
     ['打折', '满减', '满赠', '秒杀', '直降', '满返']]
    '''
    colsUniqueValue = dataFillna[colName].unique().tolist()
    uniqueList.append(colsUniqueValue)

for lineIndex in range(lines):
    '''
     dictList = [
     {'素材类型': 1, '广告类型': 4, '合作方式': 1, '广告尺寸': 6, '广告卖点': 0},
     {'素材类型': 1, '广告类型': 4, '合作方式': 1, '广告尺寸': 6, '广告卖点': 0},
     {'素材类型': 1, '广告类型': 4, '合作方式': 3, '广告尺寸': 6, '广告卖点': 0},
     {'素材类型': 2, '广告类型': 5, '合作方式': 1, '广告尺寸': 7, '广告卖点': 4}
     ]
     listValue = ['打折', '满减', '满赠', '秒杀', '直降', '满返'] | list.index
     eachRecord = 
     素材类型    2
     广告类型    5
     合作方式    1
     广告尺寸    7
     广告卖点    4 | Series
     eachDict = {'素材类型': 2, '广告类型': 5, '合作方式': 1, '广告尺寸': 7, '广告卖点': 4}
    '''
    eachRecord = converMatrix.iloc[lineIndex]  # 获得每行数据 | Series
    for eachIndex, eachData in enumerate(eachRecord):
        listValue = uniqueList[eachIndex]
        eachRecord[eachIndex] = listValue.index(eachData)
    eachDict = dict(zip(converCols, eachRecord))  # 将每个值和对应的索引组合字典
    dictList.append(eachDict)  # 将字典追加到总列表中 len() = 889
# 将[{x:1,y:2,z:3},{x:1,y:2,z:3},{x:1,y:2,z:3}...] 转换成
# array[[1,2,3],[1,2,3],[1,2,3]....]
modelDvtransform = DictVectorizer(sparse=False, dtype=np.int64)
dataDictvec = modelDvtransform.fit_transform(dictList)
# 零均值标准化
sacleMatrix = dataFillna.iloc[:, 1:8]
mms = MinMaxScaler()
dataScaled = mms.fit_transform(sacleMatrix)

X = np.hstack((dataScaled, dataDictvec))  # 水平

scoreList = list()
silhouetteInt = -1  # 平均轮廓系数得分 | [-1,1]
for n_clusters in range(2, 10):
    modelKmeans = KMeans(n_clusters=n_clusters, random_state=0)
    cluster_labels_tmp = modelKmeans.fit_predict(X)  # shape=(889,)
    silhouetteIntTmp = metrics.silhouette_score(X, cluster_labels_tmp)
    if silhouetteIntTmp > silhouetteInt:
        best_k = n_clusters
        silhouetteInt = silhouetteIntTmp
        bestKmeans = modelKmeans
        cluster_labels_k = cluster_labels_tmp  # 最好的聚类标签 | [0,3]
    scoreList.append([n_clusters, silhouetteIntTmp])
print('{:*^60}'.format('K value and silhouette summary:'))
print(np.array(scoreList))
print('Best K is : {0} with average silhouette of {1}'.
      format(best_k, silhouetteInt.round(4)))

cluster_labels = pd.DataFrame(
    cluster_labels_k, columns=['clusters'])  # (889,1)

mergeData = pd.concat((dataFillna, cluster_labels), axis=1)
clustering_count = pd.DataFrame(mergeData['渠道代号'].
                                groupby(mergeData['clusters']).count()).T.\
    rename({'渠道代号': 'counts'})  # 计算每个聚类的样本量
clustering_ratio = (clustering_count / len(mergeData)).round(2).\
    rename({'counts': 'percentage'})  # 计算每个聚类类别的样本量占比

cluster_features = []
for line in range(best_k):
    label_data = mergeData[mergeData['clusters'] == line]
    part1_data = label_data.iloc[:, 1:8]
    part1_desc = part1_data.describe().round(3)
    merge_data1 = part1_desc.iloc[2, :] # 取标准差？

    part2_data = label_data.iloc[:, 8:-1]
    part2_desc = part2_data.describe(include='all')  # count unique top freq
    merge_data2 = part2_desc.iloc[2, :]  # top
    merge_line = pd.concat((merge_data1, merge_data2), axis=0) # (12,)|Series
    cluster_features.append(merge_line) # [Series,Series,Series,...] | list | len()=4

cluster_pd = pd.DataFrame(cluster_features).T
print('{:*^60}'.format('所有簇的特征(标准差、Top值、技术、占比)'))
all_cluster_set = pd.concat((clustering_count, clustering_ratio, cluster_pd),axis=0)
print(all_cluster_set)

num_sets = cluster_pd.iloc[:6, :].T.astype(np.float64)
num_sets_max_min = mms.fit_transform(num_sets) # shape (4,6)
# 画极坐标图
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)  # polar=True 创建极坐标图
labels = np.array(merge_data1.index[:-1])
cor_list = list('rgby')
## angles->间隔长度,False表示最后一个值不是末尾的点
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
angles = np.concatenate((angles, [angles[0]])) # shape(7,) | 首尾一致

print('{:*^60}'.format('各聚类类别显著特征对比(雷达图)'))

for i in range(len(num_sets)):
    '''
    先画雷达图，再画线图
    set_thetagrids 设置极坐标系
    angles*180 / np.pi 代表角度
    labels 极坐标轴的标签
    fontproperties 黑体
    '''
    data_tmp = num_sets_max_min[i, :]
    data = np.concatenate((data_tmp, [data_tmp[0]])) # 首尾值一致 | shape(7,)
    ax.plot(angles, data, 'o-', c=cor_list[i], label=i) # label是坐标轴的标签
    ax.set_thetagrids(angles * 180 / np.pi, labels, fontproperties='SimHei')
    ax.set_title('各聚类类别显著特征对比', fontproperties='SimHei')
    ax.set_rlim(-0.2, 1.2) # 半径的范围
    plt.legend(loc='best')
plt.show()
