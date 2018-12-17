# -*- coding: utf-8 -*-
"""
创建时间 Wed Aug 29 10:03:15 2018
描述:
作者:PM.liugang
"""

'''
文本聚类
'''

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import jieba.posseg as pseg


def jieba_cut(comment):
    word_list = []
    seg_list = pseg.cut(comment)
    for word in seg_list:
        if word.flag in ['a', 'ag', 'an']:
            word_list.append(word.word)
    return word_list


fn = open(r'd:\python\python_数据分析与数据化运营\chapter4\comment_utf_8.txt',
          encoding='utf-8')
comment_list = fn.readlines()
fn.close()
stop_words = [u'…', u'。', u'，', u'？', u'！', u'+', u' ',
              u'、', u'：', u'；', u'（', u'）', u'.', u'-']  # 定义停用词
vectorizer = TfidfVectorizer(
    stop_words=stop_words, tokenizer=jieba_cut, use_idf=True)
x = vectorizer.fit_transform(comment_list)

model_kmeans = KMeans(n_clusters=3)
model_kmeans.fit(x)
cluster_labels = model_kmeans.labels_  # 0,1,2
word_vectors = vectorizer.get_feature_names()  # 形容词1，形容词2，形容词3，
word_values = x.toarray()
comment_matrix = np.hstack(
    (word_values, cluster_labels.reshape(word_values.shape[0], 1)))
word_vectors.append('cluster_labels')
comment_pd = pd.DataFrame(comment_matrix, columns=word_vectors)
print(comment_pd.head(1))

comment_cluster1 = comment_pd[comment_pd['cluster_labels'] == 2].drop(
    'cluster_labels', axis=1)
word_importance = np.sum(comment_cluster1, axis=0)  # 每个特征求和
print(word_importance.sort_values(ascending=False)[:5])

'''
高     4.201592
差     4.134921
快     2.872504
流畅    2.563055
大     1.502440
'''
