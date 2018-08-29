# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 20:27:34 2018

@author: 刘刚
"""

import re,os
import collections
import numpy as np
import jieba
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt

os.chdir('C:\python\python_数据分析与数据化运营\chapter4')
file = 'article1.txt'

def jieba_fenci(file):
    fn = open(file)
    string_data = fn.read()
    fn.close()
#    pattern = re.compile(u'\t|\n|\.|-|-|')
    pattern = re.compile(u'\t|\n|\.|-|一|:|;|\)|\(|\?|"') #排除标点符号
    string_data = re.sub(pattern,'',string_data)
    seg_list_exact = jieba.cut(string_data,cut_all=False)
    object_list = []
    remove_words = [u'的', u'，', u'和', u'是', u'随着', u'对于', ' ', u'对', u'等', u'能', u'都', u'。',
                u'、', u'中', u'与', u'在', u'其', u'了', u'可以', u'进行', u'有', u'更', u'需要', u'提供',
                u'多', u'能力', u'通过', u'会', u'不同', u'一个', u'这个', u'我们', u'将', u'并',
                u'同时', u'看', u'如果', u'但', u'到', u'非常', u'—', u'如何', u'包括', u'这']
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

# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 23:48:30 2018

@author: 刘刚
"""

import jieba.posseg as pseg
import pandas as pd
import os

os.chdir('C:\python\python_数据分析与数据化运营\chapter4')

fn = open('article1.txt')
string_data = fn.read()
fn.close()
#分词+词性标注
words = pseg.cut(string_data)#做带有词性标注的分词
words_list = []
for word in words:
    words_list.append((word.word,word.flag))#分词和词性
words_pd = pd.DataFrame(words_list,columns=['word','type'])
print(words_pd.head(4))
'''
        word type
0      Adobe  eng
1               x
2  Analytics  eng
3          和    c
e + ng
'''
#词性分类汇总-两列分类
words_gb = words_pd.groupby(['type','word'])['word'].count()
print(words_gb.head(4))
'''
type  word
a     不同      14
      不足       2
      不通       1
      严谨       2
'''
#词性分类汇总，单列分类
words_gb2 = words_pd.groupby('type').count()
words_gb2 = words_gb2.sort_values(by='word',ascending=False)
print(words_gb2.head(4))
'''
      word
type      
x      994
n      981
v      834
eng    295
'''

#选择特性类型词语做展示
words_pd_index = words_pd['type'].isin(['n','eng'])
words_pd_select = words_pd[words_pd_index]
print(words_pd_select.head(4))
'''
        word type
0      Adobe  eng
2  Analytics  eng
4   Webtrekk  eng
9         领域    n
'''

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 00:25:35 2018

@author: 刘刚
"""
import jieba.posseg as pseg
import pandas as pd
import os

os.chdir('C:\python\python_数据分析与数据化运营\chapter4')

fn = open('article1.txt')
string_data = fn.read()
fn.close()
#分词+词性标注
words = pseg.cut(string_data)#做带有词性标注的分词
words_list = []
for word in words:
    words_list.append((word.word,word.flag))#分词和词性
words_pd = pd.DataFrame(words_list,columns=['word','type'])
print(words_pd.head(4))
'''
        word type
0      Adobe  eng
1               x
2  Analytics  eng
3          和    c
e + ng
'''
#词性分类汇总-两列分类
words_gb = words_pd.groupby(['type','word'])['word'].count()
print(words_gb.head(4))
'''
type  word
a     不同      14
      不足       2
      不通       1
      严谨       2
'''
#词性分类汇总，单列分类
words_gb2 = words_pd.groupby('type').count()
words_gb2 = words_gb2.sort_values(by='word',ascending=False)
print(words_gb2.head(4))
'''
      word
type      
x      994
n      981
v      834
eng    295
'''

#选择特性类型词语做展示
words_pd_index = words_pd['type'].isin(['n','eng'])
words_pd_select = words_pd[words_pd_index]
print(words_pd_select.head(4))
'''
        word type
0      Adobe  eng
2  Analytics  eng
4   Webtrekk  eng
9         领域    n
'''


import re,os
import collections
import numpy as np
import jieba
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt

os.chdir('C:\python\python_数据分析与数据化运营\chapter4')
file = 'article1.txt'

def jieba_fenci(file):
    fn = open(file)
    string_data = fn.read()
    fn.close()
#    pattern = re.compile(u'\t|\n|\.|-|-|')
    pattern = re.compile(u'\t|\n|\.|-|一|:|;|\)|\(|\?|"') #排除标点符号
    string_data = re.sub(pattern,'',string_data)
    seg_list_exact = jieba.cut(string_data,cut_all=False)
    object_list = []
    remove_words = [u'的', u'，', u'和', u'是', u'随着', u'对于', ' ', u'对', u'等', u'能', u'都', u'。',
                u'、', u'中', u'与', u'在', u'其', u'了', u'可以', u'进行', u'有', u'更', u'需要', u'提供',
                u'多', u'能力', u'通过', u'会', u'不同', u'一个', u'这个', u'我们', u'将', u'并',
                u'同时', u'看', u'如果', u'但', u'到', u'非常', u'—', u'如何', u'包括', u'这']
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

import jieba.analyse
import pandas as pd
import os
os.chdir('C:\python\python_数据分析与数据化运营\chapter4')
# 读取文本文件
fn = open('article1.txt')  # 以只读方式打开文件
string_data = fn.read()  # 使用read方法读取整段文本
fn.close()  # 关闭文件对象

#topk提取的关键字数量，withweight 设置为True指定输出次对应的IF-IDF权重，allowpos只允许提取符合特定词语类型的标签，withflag 指定输出的关键字标签带有词语类别信息
tags_pairs = jieba.analyse.extract_tags(string_data, topK=5, withWeight=True, allowPOS=['ns', 'n', 'vn', 'v', 'nr'],withFlag=True)
tags_list = []
for i in tags_pairs:
    tags_list.append((i[0].word,i[0].flag,i[1]))#标签，分组，TF-IDF权重
tags_pd = pd.DataFrame(tags_list,columns=['word','flag','weight'])
print(tags_pd)

import numpy as np
import pandas as pd
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

fn = open('comment_utf_8.txt',encoding='utf-8')
comment_list = fn.readlines()
fn.close()

stop_words = stop_words = [u'…', u'。', u'，', u'？', u'！', u'+', u' ', u'、', u'：', u'；', u'（', u'）', u'.', u'-']
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
