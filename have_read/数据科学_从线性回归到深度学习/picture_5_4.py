# -*- coding: utf-8 -*-
"""
创建时间：Fri Feb  1 10:05:03 2019
描述：
作者: PM.LiuGang
Review:
遗留：
"""

#import sys 
import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import norm, logistic

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

def visualization():
    fig = plt.figure(figsize=(9,6),dpi=100)
    ax = fig.add_subplot(111)
    x = np.linspace(-5,5,100)
    alpha = 1.702
    normal = norm.cdf(x)
    logit = logistic.cdf(alpha * x)
    ax.plot(x,
            normal,
            label=u'%s' % "标准正态分布：" +\
            r"$F(x) = \int_{-\infty}^{x}\frac{1}{\sqrt{2\pi}}{\rm e}^{-\frac{t^{2}}{2}}$"
            + r"${\rm d}t$")
    ax.plot(x,logit,'k-.',label=u'%s' %
            r"最佳近似的逻辑分布：$F(x) = \frac{1}{1 + {\rm e}^{-1.702x}}$")
    ax.set_xlabel('$x$')
    ax.set_ylabel('%s: $F(x)$' % '累计分布函数')
    plt.legend(shadow=True,fontsize=13)
    plt.show()
    
if __name__ == '__main__':
    visualization()