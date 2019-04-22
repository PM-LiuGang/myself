# -*- coding: utf-8 -*-
"""
创建时间：Sun Apr 21 10:28:48 2019
描述：
作者: PM.LiuGang
Review:
遗留：
"""
import numpy as np

def ols(a, p):
    """
    Parameters
    ----------
    a : ndarray 
    p : 矩阵的维数，只支持方阵
    """
    eigValues, eigVectors = np.linalg.eig(a)
    eigVectors = np.round(eigVectors,2)
    fe = eigVectors[0]
    se = eigVectors[1]
    te = eigVectors[2]
    # 判断是否正交，如果正交，直接单位化
    if sum(fe*se) == 0 and sum(fe*te)==0 and sum(se,te)==0:
        fe = fe / np.sqrt(sum(fe*fe))
        se = te / np.sqrt(sum(te*te))
        te = se / np.sqrt(sum(se*se))
    else: # 如果不正交，采用格拉姆-施密特方法求求正交基
        fe = fe
        se = se - (sum(se,fe)/sum(fe,fe)) * fe
        te = te - (sum(te,fe)/sum(fe,fe)) * fe - (sum(te,se)/sum(se,se)) * se
        # 单位化
        fe = np.round(fe / np.sqrt(sum(fe*fe)),2)
        se = np.round(se / np.sqrt(sum(se*se)),2)
        te = np.round(te / np.sqrt(sum(te*te)),2)
        
    print(np.c_[fe, se, te])
    print(eigValues)
    print(np.linalg.inv(np.c_[fe, se, te]))