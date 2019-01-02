# -*- coding: utf-8 -*-
"""
描述：
创建时间：Wed Jan  2 20:51:38 2019
作者: PM.LiuGang
Review:
遗留：
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn import metrics

rawData = pd.read_csv('ad_performance.txt',delimiter='\t')

print('{:*^60}'.format('Data overview:'))
print(rawData.head(2))

print('{:*^60}'.format('Data dtypes:'))
print((rawData.dtypes).T)

print('{:*^60}'.format('NA counts:'))
print(pd.DataFrame(rawData.isnull()).sum().T)

print('{:*^60}'.format('Data Describe'))
print(rawData.describe().round(2).T) # 波动非常大 有缺失值 最小值和分位数值不对

print('{:*^60}'.format('Correlation Analysis:'))
print(rawData.corr().round(2).T)

dataFillna = rawData.fillna(rawData['平均停留时间'].mean()) # 有缺失值

converCols = ['素材类型','广告类型','合作方式','广告尺寸','广告卖点']
converMatrix = dataFillna[converCols]
lines = dataFillna.shape[0]
dictList = []
uniqueList = []

for colName in converCols:
    colsUniqueValue = dataFillna[colName].unique().tolist()
    uniqueList.append(colsUniqueValue)
    
for lineIndex in range(lines):
    eachRecord = converMatrix.iloc[lineIndex] # 获得每行数据 | Series
    for eachIndex, eachData in enumerate(eachRecord):
        # 读取该行索引对应的总唯一值列表索引下的数据
        # 其实就是相当于原来的列做了转置成了行，目的是查找唯一值值仔列表中的位置
        listValue = uniqueList[eachIndex] 
        # 获取每个值对应到总唯一值列表中的索引
        eachRecord[eachIndex] = listValue.index(eachData)
    eachDict = dict(zip(converCols, eachRecord)) # 将每个值和对应的索引组合字典
    dictList.append(eachDict) # 将字典追加到总列表中 len() = 889
    
modelDvtransform = DictVectorizer(sparse=False, dtype=np.int64)
dataDictvec = modelDvtransform.fit_transform(dictList)

sacleMatrix = dataFillna.iloc[:,1:8]
mms = MinMaxScaler()
dataScaled = mms.fit_transform(sacleMatrix)

X = np.hstack((dataScaled,dataDictvec))

scoreList = list()
silhouetteInt = -1 # 可以设置为-1，或比-1更小的值
for n_clusters in range(2,10):
    modelKmeans = KMeans(n_clusters=n_clusters,random_state=0)
    cluster_labels_tmp = modelKmeans.fit_predict(X)
    # 平均轮廓系数得分检验 得到每个K下的平均轮廓系数 [-1,1]
    silhouetteIntTmp = metrics.silhouette_score(X,cluster_labels_tmp)
    if silhouetteIntTmp > silhouetteInt: #  如果平均系数更高
        best_k = n_clusters
        silhouetteInt = silhouetteIntTmp
        bestKmeans = modelKmeans
        cluster_labels_k = cluster_labels_tmp # 最好的聚类标签
    scoreList.append([n_clusters,silhouetteIntTmp])
print('{:*^60}'.format('K value and silhouette summary:'))
print(np.array(scoreList))
print('Best K is : {0} with average silhouette of {1}'.\
      format(best_k,silhouetteInt.round(4)))

cluster_labels = pd.DataFrame(cluster_labels_k,columns=['clusters']) # (889,1)
mergeData = pd.concat((dataFillna,cluster_labels),axis=1)

clustering_count = pd.DataFrame(mergeData['渠道代号'].\
                                groupby(mergeData['clusters']).count()).T.\
                                rename({'渠道代号':'counts'}) # 计算每个聚类的样本量
clustering_ratio = (clustering_count / len(mergeData)).round(2).\
                    rename({'counts':'percentage'}) # 计算每个聚类类别的样本量占比
                  
cluster_features = [] 
for line in range(best_k):
    label_data = mergeData[mergeData['clusters'] == line]
    part1_data = label_data.iloc[:,1:8]
    part1_desc = part1_data.describe().round(3)
    merge_data1 = part1_desc.iloc[2,:]
  
    part2_data = label_data.iloc[:,8:-1]
    part2_desc = part2_data.describe(include='all') # 获取字符串数据特征的描述性统计信息
    merge_data2 = part2_desc.iloc[2,:] # 获取字符串型数据特征的最频繁值
    merge_line = pd.concat((merge_data1,merge_data2),axis=0)
    cluster_features.append(merge_line)
    
cluster_pd = pd.DataFrame(cluster_features).T
print('{:*^60}'.format('Detail feature aboat all clusters'))
all_cluster_set = pd.concat((clustering_count,clustering_ratio,cluster_pd),axis=0)
print(all_cluster_set)

num_sets = cluster_pd.iloc[:6,:].T.astype(np.float64)
num_sets_max_min = mms.fit_transform(num_sets)

fig = plt.figure()
ax = fig.add_subplot(111,polar=True) # polar 用来设置该自网格对象显示极坐标系
labels = np.array(merge_data1.index[:-1])
cor_list = list('rgby')
# 间隔长度 False表示最后一个值不是间隔区间的末尾
angles = np.linspace(0,2*np.pi,len(labels),endpoint=False)
# 建立想提供首尾子弹以便于闭合 
angles = np.concatenate((angles,[angles[0]]))

for i in range(len(num_sets)):
    '''
    set_thetagrids 设置极坐标系
    angles*180 / np.pi 代表角度
    labels 极坐标轴的标签
    fontproperties 黑体
    '''
    data_tmp = num_sets_max_min[i,:]
    data = np.concatenate((data_tmp,[data_tmp[0]]))
    ax.plot(angles,data,'o-',c=cor_list[i],label=i)
    ax.set_thetagrids(angles * 180 / np.pi,labels,fontproperties='SimHei')
    ax.set_title('各聚类类别显著特征对比',fontproperties='SimHei')
    ax.set_rlim(-0.2,1.2)
    plt.legend(loc=0)
    plt.show()