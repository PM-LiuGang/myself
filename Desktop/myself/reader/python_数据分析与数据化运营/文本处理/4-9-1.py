'''
词频统计
'''
import re
import collections
import numpy as np
import jieba
import jieba.posseg as pseg
import pandas as pd
import jieba.analyse
import wordcloud

from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from PIL import Image

'''读取数据'''
fn = open('article1.txt')
string_data = fn.read()
fn.close()

'''清洗数据'''
pattern = re.compile('''
                     \t|
                     \n|
                     \.|
                     - |
                     ——|
                     : |
                     ; |
                     \)|
                     \(|
                     \?|
                     "
                     ''')
string_data_sub = re.sub(pattern, '', string_data)

'''切割词汇'''
seg_list_excat = jieba.cut(string_data, cut_all=False)
object_list = []
remove_words = ['的', '，', '和', '是', '随着', '对于', ' ', '对', '等', 
                '能', '都', '。','、', '中', '与', '在', '其', '了', 
                '可以', '进行', '有', '更', '需要', '提供','多', '能力', 
                '通过', '会', '不同', '一个', '这个', '我们', '将', '并',
                '同时', '看', '如果', '但', '到', '非常', '—', '如何', 
                '包括', '这']

for word in seg_list_excat:
    if word not in remove_words:
        object_list.append(word)

word_counts = collections.Counter(object_list)
word_counts_top5 = word_counts.most_common(5) # 

for w, c in word_counts_top5:
    print(w, c)

'''词性标注'''
words = pseg.cut(string_data)
words_list = []

for word in words:
    words_list.append((word.word, word.flag))  # 文本 内容 

words_pd = pd.DataFrame(words_list, columns=['word', 'type']) # ？
words_gb = words_pd.groupby(['type', 'word'])['word'].count()
words_gb2 = words_pd.groupby('type').count()
words_gb2 = words_gb2.sort_values(by='word', ascending=False)
words_pd_index = words_pd['type'].isin(['n', 'eng']) # n eng对应不同词性
words_pd_select = words_pd[words_pd_index]

'''关键字提取'''
tags_pairs = jieba.analyse.extract_tags(string_data, 
                                        topK=5, 
                                        withWeight=True, 
                                        allowPOS=['ns', 'n', 'vn', 'v', 'nr'],
                                        withFlag=True)
tags_list = []
for i in tags_pairs:
    tags_list.append((i[0].word, i[0].flag, i[1]))
tags_pd = pd.DataFrame(tags_list, columns=['word', 'flag', 'weight'])


'''文本聚类'''

def jieba_cut(comment):
    '''
    将符合词性的评论文本加入列表中
    '''
    word_list = []
    seg_list = pseg.cut(comment)
    for word in seg_list:
        if word.flag in ['a', 'ag', 'an']:
            word_list.append(word.word)
    return word_list

fnComment = open('comment_utf_8.txt',encoding='utf-8')
comment_list = fnComment.readlines()
fn.close()

stop_words = ['…', '。', '，', '？', '！', '+', ' ','、', '：', '；', '（', '）', 
              '.', '-']  # 定义停用词
'''模型评估'''
vectorizer = TfidfVectorizer(stop_words=stop_words, 
                             tokenizer=jieba_cut, # 自定义函数 
                             use_idf=True)
x = vectorizer.fit_transform(comment_list)

model_kmeans = KMeans(n_clusters=3)
model_kmeans.fit(x)

cluster_labels = model_kmeans.labels_
word_vectors = vectorizer.get_feature_names()
word_values = x.toarray()
comment_matrix = np.hstack((word_values, 
                            cluster_labels.reshape(word_values.shape[0], 1)))
word_vectors.append('Cluster_Labels')
comment_pd = pd.DataFrame(comment_matrix, columns=word_vectors)
comment_cluster1 = comment_pd[comment_pd['cluster_labels'] == 2].drop('cluster_labels', axis=1)
word_importance = np.sum(comment_cluster1, axis=0)

print(word_importance.sort_values(ascending=False)[:5])
