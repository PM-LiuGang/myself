# -*- coding: utf-8 -*-
"""
创建时间：Fri Jan  4 19:06:42 2019
描述：
作者: PM.LiuGang
Review:
遗留：程序大约需要运行10分钟才能出
"""

import tarfile
import os
import jieba.posseg as pseg

from gensim import corpora, models # gensim的词频统计和主题建模模块
from bs4 import BeautifulSoup # 用于XML格式化处理

def jieba_cut(text):
    '''
    将输入的文本句子根据词性标注做分词
    ————————————————————————————————
    text:文本句子 | str
    ————————————————————————————————
    return：符合规则的分词结果
    '''
    rule_words = ['z','vn','v','t','nz','nr','ns','n','l','i','j','an','a']
    words = pseg.cut(text)
    seg_list = []
    for word in words:
        if word.flag in rule_words:
            seg_list.append(word.word) # word.word?
    return seg_list

def text_pro(words_list,tfidf_object=None,training=True):
    '''
    gensim主题建模预处理过程，包含分词类别转字典、生成语料库和TF-IDF转换
    ————————————————————————————————————————————————————————————————
    words list 分词列表 | list
    tfidf object TF-IDF模型对象，在训练阶段生成 | tf-idf
    training 是否是训练阶段，用来针对训练和预测两个阶段做预处理 | bool
    —————————————————————————————————————————————————————————————————
    return 
    如果是训练阶段，返回词典 TF-IDF对象和TF-IDF向量空间数据 
    如果是预测阶段，返回TF-IDF向量空间数据
    '''
    # 分词列表转字典
    dic = corpora.Dictionary(words_list) # 将分词列表转为字典形式 
    h = 0
    print('{:*^60}'.format('token & word mapping review:'))
    for i, w in dic.items(): # 循环读出字典前5条的每个key和value，对应的是索引值和分词
        print('token:%s -- word:%s' % (i,w))
        h += 1
        if h > 4:
            break
    # 生成语料库
    corpus = [] # 建立一个用于储存语料库的列表
    for words in words_list:
        # 将每个分词列表转换为语料库词带 | bag of word
        corpus.append(dic.doc2bow(words))
    print('{:*^60}'.format('bag of words review:'))
    print(corpus[0])
    # TF-IDF语料库
    if training == True:
        tfidf= models.TfidfModel(corpus) # 建立TF-IDF模型对象
        corpus_tfidf = tfidf[corpus] # 得到TF-IDF向量的稀疏矩阵
        print('{:*^60}'.format('TF-IDF model review:'))
        for doc in corpus_tfidf: # 循环读出每个向量
            print(doc) # 打印第一条向量
            break 
        return dic,corpus_tfidf,tfidf
    else:
        return tfidf_object[corpus]
    
def str_convert(content):
    '''
    将内容中的全角字符，包括英文字母，数字键，符号等转换为半角字符
    ——————————————————————————————————————————————————————————
    content 要转换的字符串内容
    ——————————————————————————————————————————————————————————
    return 转换后的半角字符串
    '''
    new_str = ''
    for each_char in content:
        code_num = ord(each_char)
        if code_num == 12288: # 全角空格直接转换
            code_num == 32
        elif (code_num >= 65281 and code_num <= 65374): # 全角字符根据关系转化
            code_num -= 65248
        new_str += chr(code_num)
    return new_str

def data_parse(data):
    '''
    从原始文件中解析出文本内容数据
    param data:包含代码的原始内容
    return：文本中的所有内容 | list
    '''
    raw_code = BeautifulSoup(data,'lxml')
    content_code = raw_code.find_all('content') # 从包含文本的代码块中找到content标签
    content_list = []
    for each_content in content_code:
        if len(each_content) > 0:
            raw_content = each_content.text # 获取原始字符串
            convert_content = str_convert(raw_content) #全角2半角
            content_list.append(convert_content) # 将content文本内容加入列表
    return content_list

if not os.path.exists('./new_data'):
    print('从新的数据包解压数据..........')
    tar = tarfile.open('news_data.tar.gz') # 打开tar gz压缩包对象
    names = tar.getnames() # 获得压缩包内的每个文件对象的名称
    for name in names: 
        tar.extract(name,path='./') # 将文件解压到指定目录
    tar.close()
    
print('遍历文件，得到内容')
all_content = []
for root, dirs,files in os.walk('./news_data'):
    for file in files:
        file_name = os.path.join(root,file)
        with open(file_name,encoding='utf-8') as f:
            data = f.read()
        all_content.extend(data_parse(data))

print('得到词列表')
words_list = []
for each_content in all_content:
    words_list.append(list(jieba_cut(each_content)))
    
print('拟合主题模型')
dic,corpus_tfidf,tfidf = text_pro(words_list,tfidf_object=None,training=True)
num_topics = 3
lda = models.LdaModel(corpus_tfidf,id2word=dic,num_topics=num_topics)

print('{:*^60}'.format('主题模型审阅'))
for i in range(num_topics):
    print(lda.print_topic(i))
    
print('主题预测')
with open('article.txt',encoding='utf-8') as f:
    text_new = f.read()
text_content = data_parse(data)
words_list_new = jieba_cut(text_new)
corpus_tfidf_new = text_pro([words_list_new],tfidf_object=tfidf,training=False)
corpus_lda_new = lda[corpus_tfidf_new]
print('{:*^60}'.format('主题预测'))
print(list(corpus_lda_new))
        