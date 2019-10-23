# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 20:27:34 2018
@author: 刘刚
review:190123
"""

import re,os
import collections
import numpy as np
import jieba
import wordcloud
import matplotlib.pyplot as plt

from PIL import Image

file = 'article1.txt'
remove_words = ['的', '，', '和', '是', '随着', '对于', ' ', '对', '等',
                '能', '都', '。','、', '中', '与', '在', '其', '了', 
                '可以', '进行', '有', '更', '需要', '提供','多', '能力', 
                '通过', '会', '不同', '一个', '这个', '我们', '将', '并',
                '同时', '看', '如果', '但', '到', '非常', '—', '如何', 
                '包括', '这']


def jieba_fenci(file):
    fn = open(file)
    string_data = fn.read()
    fn.close()
    pattern = re.compile('\t|\n|\.|-|一|:|;|\)|\(|\?|"') #排除标点符号
    string_data = re.sub(pattern,'',string_data)
    seg_list_exact = jieba.cut(string_data,cut_all=False)
    object_list = []
    for word in seg_list_exact:
        if word not in remove_words:
            object_list.append(word)
    word_counts = collections.Counter(object_list)
    word_counts_top5 = word_counts.most_common(5)
    
    for w,c in word_counts_top5:
        print(w,c)
        
    mask = np.array(Image.open('wordcloud.jpg'))#将文件对象实例转换成数组
    wc = wordcloud.WordCloud(
            font_path = r'C:\Windows\Fonts\simhei.ttf',
            mask = mask,
            max_words = 200,
            max_font_size =100)#词云对象
    wc.generate_from_frequencies(word_counts)#从词频统计结果中获取词频数据
    image_colors = wordcloud.ImageColorGenerator(mask)#自定义展示颜色方案
    wc.recolor(color_func=image_colors)#改变词云的颜色方案
    plt.imshow(wc)#展示词云
    plt.axis('off')#关闭坐标轴
    plt.show()
   
jieba_fenci(file)

import jieba.posseg as pseg
import pandas as pd

fn = open(file)
string_data = fn.read()
fn.close()
#分词+词性标注
words = pseg.cut(string_data)#做带有词性标注的分词
words_list = []
for word in words:
    words_list.append((word.word,word.flag))#分词和词性
words_pd = pd.DataFrame(words_list,columns=['word','type'])
print(words_pd.head(4))

#词性分类汇总-两列分类
words_gb = words_pd.groupby(['type','word'])['word'].count()
print(words_gb.head(4))

#词性分类汇总，单列分类
words_gb2 = words_pd.groupby('type').count()
words_gb2 = words_gb2.sort_values(by='word',ascending=False)
print(words_gb2.head(4))

#选择特性类型词语做展示
words_pd_index = words_pd['type'].isin(['n','eng'])
words_pd_select = words_pd[words_pd_index]
print(words_pd_select.head(4))

import jieba.posseg as pseg
import pandas as pd

fn = open(file)
string_data = fn.read()
fn.close()
#分词+词性标注
words = pseg.cut(string_data)#做带有词性标注的分词
words_list = []
for word in words:
    words_list.append((word.word,word.flag))#分词和词性
words_pd = pd.DataFrame(words_list,columns=['word','type'])
print(words_pd.head(4))

#词性分类汇总，单列分类
words_gb2 = words_pd.groupby('type').count()
words_gb2 = words_gb2.sort_values(by='word',ascending=False)
print(words_gb2.head(4))

#选择特性类型词语做展示
words_pd_index = words_pd['type'].isin(['n','eng'])
words_pd_select = words_pd[words_pd_index]
print(words_pd_select.head(4))

def jieba_fenci(file):
    fn = open(file)
    string_data = fn.read()
    fn.close()
    pattern = re.compile(u'\t|\n|\.|-|一|:|;|\)|\(|\?|"') #排除标点符号
    string_data = re.sub(pattern,'',string_data)
    seg_list_exact = jieba.cut(string_data,cut_all=False)
    object_list = []
    for word in seg_list_exact:
        if word not in remove_words:
            object_list.append(word)
    word_counts = collections.Counter(object_list)
    word_counts_top5 = word_counts.most_common(5)
    
    for w,c in word_counts_top5:
        print(w,c)
        
    mask = np.array(Image.open('wordcloud.jpg'))#将文件对象实例转换成数组
    wc = wordcloud.WordCloud(
            font_path = r'C:\Windows\Fonts\simhei.ttf',
            mask = mask,
            max_words = 200,
            max_font_size =100)#词云对象
    wc.generate_from_frequencies(word_counts)#从词频统计结果中获取词频数据
    image_colors = wordcloud.ImageColorGenerator(mask)#自定义展示颜色方案
    wc.recolor(color_func=image_colors)#改变词云的颜色方案
    plt.imshow(wc)#展示词云
    plt.axis('off')#关闭坐标轴
    plt.show()
   
jieba_fenci(file)    

# 读取文本文件
fn = open(file)  # 以只读方式打开文件
string_data = fn.read()  # 使用read方法读取整段文本
fn.close()  # 关闭文件对象

#topk提取的关键字数量，withweight 设置为True指定输出次对应的IF-IDF权重，allowpos只允许提取符合特定词语类型的标签，withflag 指定输出的关键字标签带有词语类别信息
tags_pairs = jieba.analyse.extract_tags(string_data, topK=5, withWeight=True, allowPOS=['ns', 'n', 'vn', 'v', 'nr'],withFlag=True)
tags_list = []
for i in tags_pairs:
    tags_list.append((i[0].word,i[0].flag,i[1]))#标签，分组，TF-IDF权重
tags_pd = pd.DataFrame(tags_list,columns=['word','flag','weight'])
print(tags_pd)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import jieba.posseg as pseg

def jieba_cut(comment):
    word_list = []
    seg_list = pseg.cut(comment)
    for word in seg_list:
        if word.flag in ['a','ag','an']:
            word_list.append(word.word)
    return word_list

fn = open('comment_utf_8.txt',encoding='utf-8') # file
comment_list = fn.readlines()
fn.close()

stop_words = stop_words = [u'…', u'。', u'，', u'？', u'！', u'+', u' ', 
                           u'、', u'：', u'；', u'（', u'）', u'.', u'-']
#stop_words自定义去除的词表，不指定会默认使用英文的停用词列表
#tokenizer定义分词器
#指定tf-idf方法做词频转向量
vectorizer = TfidfVectorizer(stop_words=stop_words,tokenizer=jieba_cut,use_idf=True)#创建词向量模型
x = vectorizer.fit_transform(comment_list)#将评论关键字转换为词向量空间模型

model_kmeans = KMeans(n_clusters=3)
model_kmeans.fit(x)

cluster_labels = model_kmeans.labels_
word_vectors = vectorizer.get_feature_names()#词向量
word_values = x.toarray()#向量值
comment_matrix = np.hstack((word_values,cluster_labels.reshape(word_values.shape[0],1)))
word_vectors.append('cluster_labels')
comment_pd = pd.DataFrame(comment_matrix,columns=word_vectors)
print(comment_pd.head(1))

comment_cluster1 = comment_pd[comment_pd['cluster_labels']==2].drop('cluster_labels',axis=1)
word_importance = np.sum(comment_cluster1,axis=0)
print(word_importance.sort_values(ascending=False)[:5])
