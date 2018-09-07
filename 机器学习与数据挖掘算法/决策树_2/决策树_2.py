# -*- coding: utf-8 -*-
"""
创建时间 Fri Sep  7 15:05:26 2018
描述:决策树 python机器学习
作者:PM.liugang
"""

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

import numpy as np

'''以下的都是假设二叉树'''


def gini(p):  # 基尼指数 ∑(i=1,c) p(i|t)(-p(i|t)) = 1 - ∑(i=1,c) p(i|t)**2
    return (p) * (1-(p)) + (1-p)*(1-(1-p))


def entropy(p):  # 熵 I(G) = -∑(i=1,c)p(i|t)log2 p(i|t)
    return -p * np.log2(p) - (1-p) * np.log2((1-p))


def error(p):  # 误差类率 1 - max{p(i|t)}
    return 1 - np.max([p, 1-p])  # max([])


'''熵和误分类率对基尼系数的影响'''

x = np.arange(0.0, 1.0, 0.01)
ent = [entropy(p) if p != 0 else None for p in x]  # 对x求熵
sc_ent = [e*0.5 if e else None for e in ent]  # 对e进行开方方式进行缩放
err = [error(i) for i in x]  # 对x求误差率
fig = plt.figure()
ax = plt.subplot(111)

for i, lab, ls, c, in zip([ent, sc_ent, gini(x), err],
                          ['熵', '熵(标准化)', '基尼不纯度','误差分类率'], \
                          list(['-', '--', '-.', ':']),\ # list('*…^') TypeError
                          ['black', 'lightgray', 'red', 'green', 'cyan']): # 至少需要大于循环的颜色
    line = ax.plot(x, i, label=lab, linestyle=ls, lw=2, color=c) # 其实i是x的函数

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=4, fancybox=True,
          shadow=False) # bbox_to_anchor(左右距离，上下距离) 0.5 中心对中心  1是正好贴上
ax.axhline(y=0.5, linewidth=1, color='k', linestyle='--')
ax.axhline(y=1.0, linewidth=1, color='k', linestyle='--')
plt.ylim([0, 1.1])  # ylim([])
plt.xlabel('p(i=1)')
plt.ylabel('Impurity Index')
plt.show()
