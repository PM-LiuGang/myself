# -*- coding: utf-8 -*-
"""
创建时间：Sun Jan  6 16:50:53 2019
描述：
建立文本向量模型常用的三种方法
sklearn->TfidfVectorrizer
gensim->TfidfModel
feature_extraction.text->HashingVectorizer
作者: PM.LiuGang
Review:
遗留：
"""

import re 
import tarfile
import os
import numpy as np
import warnings

from bs4 import BeautifulSoup # 解析xml和html数据
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

warnings.filterwarnings('ignore')

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
            code_num = 32 # 
        elif (code_num >= 65281 and code_num <= 65374): # 全角字符根据关系转化
            code_num -= 65248
        new_str += chr(code_num) # python3-chr python2-unichr
    return new_str

def data_parse(data):
    '''
    从原始文件中解析出文本内容和标签数据
    :param data：包含代码的原始内容
    return：content、域名 | []、[]
    '''
    raw_code = BeautifulSoup(data,'lxml')
    doc_code = raw_code.find_all('doc') # 从包含文本的代码块中找到的doc标签
    content_list = []
    label_list = []
    for each_doc in doc_code:
        if len(each_doc) > 0:
            content_code = each_doc.find('content') #从包含文本你的代码块中找到doc标签
            raw_content = content_code.text # 获取原始内容字符串
            convert_content = str_convert(raw_content)
            content_list.append(convert_content)
            
            label_code = each_doc.find('url') #
            label_content = label_code.text
            label = re.split('[/|.]',label_content)[2] # 将URL做分割并提取子域名
            label_list.append(label)
    return content_list, label_list

def cross_val(model_obj,data,label):
    '''
    通过交叉检验计算每次增量学习后的模型得分
    :param model_object: 每次增量学习后的模型对象
    :param data: 训练数据集
    :param label: 训练数据集对应的标签
    return: 交叉检验得分
    '''
    predict_label = model_obj.predict(data)
    score_tmp = round(accuracy_score(label,predict_label),4)
    return score_tmp

def word_to_vector(data):
    '''
    将训练集文本数据转换为稀疏矩阵
    param data：输入的文本列表
    return 稀疏矩阵
    '''
    model_vector = HashingVectorizer(non_negative=True) 
    vector_data = model_vector.fit_transform(data)
    return vector_data

def label_to_vector(label,unique_list):
    '''
    将文本标签转换为向量标签
    :param label：文本列表
    :param unique_list：唯一值列表 | list
    return 向量标签列表
    '''
    for each_index, each_data in enumerate(label):
        label[each_index] = unique_list.index(each_data) # 返回具体索引位置
    return label 
    
if not os.path.exists('./new_data'):
    print('从新的数据包解压数据..........')
    tar = tarfile.open('news_data.tar.gz') # 打开tar gz压缩包对象
    names = tar.getnames() # 获得压缩包内的每个文件对象的名称
    for name in names: 
        tar.extract(name,path='./') # 将文件解压到指定目录
    tar.close()
    
all_content = []
all_label = []
score_list = list()
pre_list = list()
unique_list = ['sports','house','news']
print('unique label:',unique_list)
model_nb = MultinomialNB()

with open('test_sets.txt',encoding='utf-8') as f:
    test_data = f.read()
test_content, test_label = data_parse(test_data)
test_data_vector = word_to_vector(test_content)
test_label_vector = label_to_vector(test_label,unique_list)

with open('article.txt',encoding='utf-8') as f:
    new_data = f.read()
new_content, new_label = data_parse(new_data)
new_data_vector = word_to_vector(new_content)

print('{:*^60}'.format('增量学习........'))

for root,dirs,files in os.walk('./news_data'):
    for file in files:
        file_name = os.path.join(root,file)
        print('training file: %s............' % file)
        with open(file_name,encoding='utf-8') as f:
            data = f.read()
        content,label = data_parse(data)
        data_vector = word_to_vector(content)
        label_vector = label_to_vector(label,unique_list)
        model_nb.partial_fit(data_vector,
                             label_vector,
                             classes=np.array([0,1,2]))
        score_list.append(cross_val(model_nb,
                                    test_data_vector,
                                    test_label_vector))
        predict_y = model_nb.predict(new_data_vector)
        pre_list.append(predict_y.tolist())
    
print('{:*^60}'.format('打印出每次交叉验证得分:'))
print(score_list)
print('{:*^60}'.format('预测的标签索引值:'))
print(pre_list)
print('{:*^60}'.format('打印出输出正确的标签值:'))
print(new_label)

