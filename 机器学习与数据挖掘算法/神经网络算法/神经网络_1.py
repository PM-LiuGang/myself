# -*- coding: utf-8 -*-
"""
创建时间 Wed Aug 29 10:14:40 2018
描述:
作者:PM.liugang
"""

# 神经网络预测代码
import pandas as pd
from keras.models import Sequential  # 导入神经网络初始化函数
from keras.layers.core import Dense, Activation  # 导入神经网络层函数、激活函数

net = Sequential()  # 建立神经网络
net.add(Dense(input_dim=7, units=14))  # 添加输入层（3节点）到隐藏层（10节点）的连接
net.add(Activation('relu'))  # 隐藏层使用relu激活函数
net.add(Dense(input_dim=14, units=1))  # 添加隐藏层（10节点）到输出层（1节点）的连接
net.add(Activation('sigmoid'))  # 输出层使用sigmoid激活函数
net.compile(loss='binary_crossentropy', optimizer='adam')  # 编译模型，使用adam方法求解
net.fit(train[:, :8], train[:, 8], nb_epoch=1000, batch_size=1)  # 训练模型，循环1000次

predict_result = net.predict_classes(train[:, :8])
predict_result = predict_result.reshape(len(train))  # 预测结果变形
# keras用predict给出预测概率
# predict_classes才是给出预测类别，而且两者的预测结果都是n x 1维数组，而不是通常的 1 x n
train_df = pd.DataFrame(train)
predict_result_series = pd.Series(predict_result)
