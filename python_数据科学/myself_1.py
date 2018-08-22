# IPython log file

import os
import pandas as pd
import numpy as np
def convert_number():
    try:
        return float(x) 
    except:
        return np.nan
from collections import defaultdict
converters = defaultdict(convert_number)
converts = defaultdict(convert_number)
lambda x : 1 if x.strip() == 'ad' else 0
#[Out]# <function <lambda> at 0x0000021F3D4D4048>
converters = lambda x : 1 if x.strip() == 'ad' else 0
get_ipython().run_line_magic('pinfo', 'pd.read_csv')
get_ipython().run_line_magic('pwd', '')
#[Out]# 'C:\\Users\\刘刚'
get_ipython().run_line_magic('cd', 'b')
get_ipython().run_line_magic('cd', '"Chapter 6"')
get_ipython().run_line_magic('ls', '')
def func(a,b):
    return a/b
def func(a,b):
    return a/b
def func2(x):
    a = x 
    b = x - 1
def func(a,b):
    return a/b
def func2(x):
    a = x 
    b = x - 1
    return func1(a,b)
func2(1)
func(1)
ipdb
get_ipython().run_line_magic('ipdb', '')
get_ipython().run_line_magic('debug', '')
def func(a,b):
    return a/b
def func2(x):
    a = x 
    b = x - 1

    return func1(a,b)
func(1)
func2(1)
def func(a,b):
    return a/b
def func2(x):
    a = x 
    b = x - 1

    return func(a,b)
func2(1)
get_ipython().run_line_magic('debug', '')
get_ipython().run_line_magic('debug', '')
get_ipython().run_line_magic('pwd', '')
#[Out]# 'C:\\python\\python_数据挖掘入门与实践\\Chapter 6'
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('logstate', '-o myself_1.py')
get_ipython().run_line_magic('logstart', '-o myself_1.py')
import json
import twitter
t = twitter.Twitter(auth = authorization)
consumer_key = "52Nu7ubm2szT1JyJEOB7V2lGM"
consumer_secret = "mqA94defqjioyWeMxdJsSduthxdMMGd2vfOUKvOFpm0n7JTqfY"
access_token = "16065520-USf3DBbQAh6ZA8CnSAi6NAUlkorXdppRXpC4cQCKk"
access_token_secret = "DowMQeXqh5ZsGvZGrmUmkI0iCmI34ShFzKF3iOdiilpX5"
authorization = twitter.OAuth(access_token, access_token_secret, consumer_key, consumer_secret)
t = twitter.Twitter(auth = authorization)
get_ipython().run_line_magic('ls', '')
ofile = 'replicable_dataset.json'
with open(ofile,'a') as ofile:
    search_results = t.search.tweets(q = 'python',count = 100)['statuses']
    for tweet in search_results:
        if 'text' in tweet:
            print(tweet['user']['screen_name'])
            print(tweet['text'])
            print()
            ofile.write(json.dumps(tweet))
            ofile.write('\n\n')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('logstop', '')
import array
l1 = list(range(10))
A = array.array('i',l1)
A
#[Out]# array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.array([1,23,245,345,0])
#[Out]# array([  1,  23, 245, 345,   0])
np.array([1,23,245.22,345,0])
#[Out]# array([  1.  ,  23.  , 245.22, 345.  ,   0.  ])
np.array([3.14,4,2,4])
#[Out]# array([3.14, 4.  , 2.  , 4.  ])
np.array([3.14,4,2,4],dtype='int')
#[Out]# array([3, 4, 2, 4])
np.array([3.14,4,2,4],dtype='float')
#[Out]# array([3.14, 4.  , 2.  , 4.  ])
np.array([range(i,i+3) for i in [2,4,6]])
#[Out]# array([[2, 3, 4],
#[Out]#        [4, 5, 6],
#[Out]#        [6, 7, 8]])
get_ipython().run_line_magic('pwd', '')
#[Out]# 'C:\\python\\python_数据挖掘入门与实践\\Chapter 6'
get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('cd', 'python_数据科学手册/')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('mkdir', 'chapter_1')
get_ipython().run_line_magic('cd', 'chapter_1/')
np.zeros(10,dtype=int)
#[Out]# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
np.ones((3,5),dtype=float)
#[Out]# array([[1., 1., 1., 1., 1.],
#[Out]#        [1., 1., 1., 1., 1.],
#[Out]#        [1., 1., 1., 1., 1.]])
np.full((3,5),3.14)
#[Out]# array([[3.14, 3.14, 3.14, 3.14, 3.14],
#[Out]#        [3.14, 3.14, 3.14, 3.14, 3.14],
#[Out]#        [3.14, 3.14, 3.14, 3.14, 3.14]])
np.arange(0,20,2)
#[Out]# array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
np.linspace(0,1,5)
#[Out]# array([0.  , 0.25, 0.5 , 0.75, 1.  ])
cat myself_1.py
get_ipython().run_line_magic('cat', 'myself_1.py')
h
get_ipython().show_usage()
get_ipython().run_line_magic('pinfo', 'cat')
get_ipython().run_line_magic('pinfo', 'dir')
dir myself_1.py
np.linspace(0,1,5)
#[Out]# array([0.  , 0.25, 0.5 , 0.75, 1.  ])
np.random.random((3,3))
#[Out]# array([[0.02939202, 0.79114997, 0.86373539],
#[Out]#        [0.09876293, 0.7225512 , 0.45608461],
#[Out]#        [0.24404289, 0.58554167, 0.56092962]])
np.random.random((3,3))#0-1均匀分布的随机数组成的数组
#[Out]# array([[0.7235592 , 0.26676196, 0.55234082],
#[Out]#        [0.89614186, 0.14933604, 0.24077278],
#[Out]#        [0.04110162, 0.37227658, 0.16540181]])
np.random.normal(0,1,(3,3))
#[Out]# array([[ 0.44793201, -0.18224379, -0.08980845],
#[Out]#        [-2.17076717,  1.98047412,  2.00530728],
#[Out]#        [-0.76663427,  0.20002923,  0.21722966]])
np.random.normal(0,1,(3,3))#0均值1方差
#[Out]# array([[ 0.01604365, -1.52411914, -1.87503644],
#[Out]#        [ 0.00329367, -0.42225592, -0.57989127],
#[Out]#        [-0.25292575,  0.90848618, -0.15961129]])
np.random.randint(0,10,(3,3))#0-10区间的随机整行数组
#[Out]# array([[5, 3, 3],
#[Out]#        [4, 4, 3],
#[Out]#        [3, 9, 2]])
np.eyes(3)#3*3的单位矩阵
np.eye(3)#3*3的单位矩阵
#[Out]# array([[1., 0., 0.],
#[Out]#        [0., 1., 0.],
#[Out]#        [0., 0., 1.]])
np.empty(3)
#[Out]# array([1., 1., 1.])
np.random.random((3,3),dtype='int64')
np.arange((4,4),dtype='int64')
np.arange((4,4))
np.arange(4,4)
#[Out]# array([], dtype=int32)
np.arange(4).dtype('int32')
np.arange(4,dtype('int32'))
np.arange(4))
np.arange(4)
#[Out]# array([0, 1, 2, 3])
np.array(range(55),dtype='int32')
#[Out]# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
#[Out]#        17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
#[Out]#        34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
#[Out]#        51, 52, 53, 54])
np.random.seed(0)
x1 = np.random.randint(10,size=6）
x1 = np.random.randint(10,size=6)
x2 = np.random.randint(10,size=(3,4))
x3 = np.random.randint(10,size=(3,4,5))
x3.ndim
#[Out]# 3
x3.shape
#[Out]# (3, 4, 5)
x3.size
#[Out]# 60
x3.dtype
#[Out]# dtype('int32')
x3.itemsize
#[Out]# 4
x3.nbytes
#[Out]# 240
x1
#[Out]# array([5, 0, 3, 3, 7, 9])
x1[0]
#[Out]# 5
x1[4]
#[Out]# 7
x1[-1]
#[Out]# 9
x1[-2]
#[Out]# 7
x2
#[Out]# array([[3, 5, 2, 4],
#[Out]#        [7, 6, 8, 8],
#[Out]#        [1, 6, 7, 7]])
x2[0,0]
#[Out]# 3
x2[2,0]
#[Out]# 1
x2[0,0] = 12
x2
#[Out]# array([[12,  5,  2,  4],
#[Out]#        [ 7,  6,  8,  8],
#[Out]#        [ 1,  6,  7,  7]])
x1
#[Out]# array([5, 0, 3, 3, 7, 9])
x1[0] = 3.14159
x1 
#[Out]# array([3, 0, 3, 3, 7, 9])
x1.dtype
#[Out]# dtype('int32')
x = np.arang
x = np.arange(10)
x
#[Out]# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x[:5]
#[Out]# array([0, 1, 2, 3, 4])
x[5:]
#[Out]# array([5, 6, 7, 8, 9])
x[4:7]
#[Out]# array([4, 5, 6])
x[::2]
#[Out]# array([0, 2, 4, 6, 8])
x[1::2]
#[Out]# array([1, 3, 5, 7, 9])
x[::-1]
#[Out]# array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
x[5::-2]
#[Out]# array([5, 3, 1])
x2
#[Out]# array([[12,  5,  2,  4],
#[Out]#        [ 7,  6,  8,  8],
#[Out]#        [ 1,  6,  7,  7]])
x2[:2,:3]
#[Out]# array([[12,  5,  2],
#[Out]#        [ 7,  6,  8]])
x2[:3,::2]
#[Out]# array([[12,  2],
#[Out]#        [ 7,  8],
#[Out]#        [ 1,  7]])
x2[::-1,::-1】
x2[::-1,::-1]
#[Out]# array([[ 7,  7,  6,  1],
#[Out]#        [ 8,  8,  6,  7],
#[Out]#        [ 4,  2,  5, 12]])
print(x2[:,0])
x2
#[Out]# array([[12,  5,  2,  4],
#[Out]#        [ 7,  6,  8,  8],
#[Out]#        [ 1,  6,  7,  7]])
print(x2[0,:])
print(x2[0])
x2
#[Out]# array([[12,  5,  2,  4],
#[Out]#        [ 7,  6,  8,  8],
#[Out]#        [ 1,  6,  7,  7]])
x2_sub = x2[:2,:2]
x2_sub
#[Out]# array([[12,  5],
#[Out]#        [ 7,  6]])
x2_sub[0,0] = 99
print(x2_sub)
print(x2)
grid = np.arange(1,10),reshape((3,3))
grid = np.arange(1,10).reshape((3,3))
print(grid)
x = np.array([1,2,3])
x.shape((1,3))
x.reshape((1,3))
#[Out]# array([[1, 2, 3]])
x[np.newaxis,:]
#[Out]# array([[1, 2, 3]])
x[np.newaxis,:]#获取行向量
#[Out]# array([[1, 2, 3]])
x.reshape((3,1))
#[Out]# array([[1],
#[Out]#        [2],
#[Out]#        [3]])
x[:,np.newaxis]
#[Out]# array([[1],
#[Out]#        [2],
#[Out]#        [3]])
x[:,np.newaxis]#获取列向量
#[Out]# array([[1],
#[Out]#        [2],
#[Out]#        [3]])
x = np.array([1,2,3])
y = np.array([3,2,1])
np.concatenate([x,y])
#[Out]# array([1, 2, 3, 3, 2, 1])
np.concatenate([x,y],axis=1)
np.concatenate([x,y],axis=0)
#[Out]# array([1, 2, 3, 3, 2, 1])
z = [44,44,44]
print(np.concatenate([x,y,z]))
grid = np.array([[1,2,3],[4,5,6]])
grid
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
np.concatenate([grid,grid])
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [1, 2, 3],
#[Out]#        [4, 5, 6]])
np.concatenate([grid,grid],axis=1)
#[Out]# array([[1, 2, 3, 1, 2, 3],
#[Out]#        [4, 5, 6, 4, 5, 6]])
x = np.array([1,2,3])
grid
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
np.vstack([x,grid])
#[Out]# array([[1, 2, 3],
#[Out]#        [1, 2, 3],
#[Out]#        [4, 5, 6]])
np.hstack([grid,y])
grid
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
y
#[Out]# array([3, 2, 1])
y = np.array([[99],[99]])
np.hstack([grid,y])
#[Out]# array([[ 1,  2,  3, 99],
#[Out]#        [ 4,  5,  6, 99]])
x = [1,2,3,99,99,3,2,1]
x1,x2,x3 = np.split(x,[3,5])
print(x1,x2,x3)
grid = np.arange(16).reshape((4,4))
grid
#[Out]# array([[ 0,  1,  2,  3],
#[Out]#        [ 4,  5,  6,  7],
#[Out]#        [ 8,  9, 10, 11],
#[Out]#        [12, 13, 14, 15]])
upper,lower = np.vsplit(grid,[2])
print(upper)
print(lower)
left,right = np.hsplit(grid,[2])
left,right
#[Out]# (array([[ 0,  1],
#[Out]#         [ 4,  5],
#[Out]#         [ 8,  9],
#[Out]#         [12, 13]]), array([[ 2,  3],
#[Out]#         [ 6,  7],
#[Out]#         [10, 11],
#[Out]#         [14, 15]]))
grid
#[Out]# array([[ 0,  1,  2,  3],
#[Out]#        [ 4,  5,  6,  7],
#[Out]#        [ 8,  9, 10, 11],
#[Out]#        [12, 13, 14, 15]])
get_ipython().run_line_magic('logstop', '')
