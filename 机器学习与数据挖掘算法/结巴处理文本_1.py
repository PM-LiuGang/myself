# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 00:25:35 2018
Modified on Wed Aug  19 21:25:35 2018wa
@author: 刘刚
结巴分词- 
cut_call=False 全匹配 | True 精确匹配 | cut_for_search 搜索引擎模式
HMM表示是否使用HMM模型识别未登录的词，默认False
l+cut 生成列表模式，cut生成迭代器模式
"""
import re
import collections
import numpy as np
import jieba
import os
os.chdir(r'd:\python\python_数据分析与数据化运营')
fn = open(r'd:\python\python_数据分析与数据化运营\chapter4\article1.txt')
string_data = fn.read()
fn.close()
pattern = re.compile('\t|\n|\.|-|——|:|;|\)|\)\(|\?|"')
string_data = re.sub(pattern, '', string_data)
seg_list_excat = jieba.cut(string_data, cut_all=False)
object_list = []
remove_words = [u'的', u'，', u'和', u'是', u'随着', u'对于', ' ', u'对', u'等', u'能', u'都', u'。',
                u'、', u'中', u'与', u'在', u'其', u'了', u'可以', u'进行', u'有', u'更', u'需要', u'提供',
                u'多', u'能力', u'通过', u'会', u'不同', u'一个', u'这个', u'我们', u'将', u'并',
                u'同时', u'看', u'如果', u'但', u'到', u'非常', u'—', u'如何', u'包括', u'这']

for word in seg_list_excat:
    if word not in remove_words:
        object_list.append(word)

word_counts = collections.Counter(object_list)
word_counts_top5 = word_counts.most_common(5)

for w, c in word_counts_top5:
    print(w, c)

name = []
value = []

for i, h in word_counts.items():
    name.append(i)
    value.append(h)

from pyecharts import WordCloud  # 取消了用matplotlib作图
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("词云图", name, value, word_size_range=[20, 100])
wordcloud.render('词云图.html')

'''
词性标注
'''
import jieba.posseg as pseg
import pandas as pd

fn = open(r'd:\python\python_数据分析与数据化运营\chapter4\article1.txt')
string_data = fn.read()
fn.close()
words = pseg.cut(string_data)
words_list = []

for word in words:
    words_list.append((word.word, word.flag))  # (())

words_pd = pd.DataFrame(words_list, columns=['word', 'type'])
words_gb = words_pd.groupby(['type', 'word'])['word'].count()
words_gb2 = words_pd.groupby('type').count()
words_gb2 = words_gb2.sort_values(by='word', ascending=False)
words_pd_index = words_pd['type'].isin(['n', 'eng'])
words_pd_select = words_pd[words_pd_index]

print(words_pd.head(4))
print(words_gb.head(4))
print(words_gb2.head(4))
print(words_pd_select.head(4))

'''
关键字提取
'''
import jieba.analyse
import pandas as pd

fn = open(r'd:\python\python_数据分析与数据化运营\chapter4\article1.txt')
string_data = fn.read()
fn.close()

tags_pairs = jieba.analyse.extract_tags(string_data, topK=5, withWeight=True, allowPOS=[
                                        'ns', 'n', 'vn', 'v', 'nr'], withFlag=True)
tags_list = []
for i in tags_pairs:
    tags_list.append((i[0].word, i[0].flag, i[1]))
tags_pd = pd.DataFrame(tags_list, columns=['word', 'flag', 'weight'])
print(tags_pd)

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
