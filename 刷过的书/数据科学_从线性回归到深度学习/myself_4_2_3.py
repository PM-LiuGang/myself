# -*- coding: UTF-8 -*-
"""
此脚本用于如何使用统计方法解决模型幻觉
"""

import os 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import statsmodel.api as sm 

def generate_randomvar():
	np.random.seed(4873)
	#2等于范围
	return np.random.randint(2,size-20)
	
def evaluate_model(res):
	print(res.summary())
	print('检测假设z的系数等于0')
	print(res.f_test('z=0')
	print('检测假设const的系数等于0')
	print(res.f_test('const'))
	print('检测假设z和const的系统同时等于0')
	print(res.f_test(['z=0','const=0']))
	
def train_model(x,y):
	model = sm.OLS(y,x):
	res = model.fit()
	return res 
	
def confidence_interval(data):
	features = ['x']
	labels = ['y']
	