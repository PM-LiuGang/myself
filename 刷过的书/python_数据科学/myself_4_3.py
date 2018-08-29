# IPython log file

get_ipython().run_line_magic('pylab', '')
get_ipython().run_line_magic('cd', 'c')
get_ipython().run_line_magic('ls', '')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style,use('serborn-white')
plt.style.use('serborn-white')
plt.style,use('seaborn-white')
plt.style,use('seaborn-white')
plt.style.use('seaborn-white')
def f(x,y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
x = np.linspace(0,5,50)
y = np.linspace(0,5,50)
x,y = np.meshgrid(x,y)
z = f(x,y)
y = np.linspace(0,5,40)
plt.contour(x,y,z,colors='black')
x = np.linspace(0,5,50)
y = np.linspace(0,5,40)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
plt.contour(X,Y,Z,colors='black')
#[Out]# <matplotlib.contour.QuadContourSet at 0x2655ebeb6d8>
plt.contour(X,Y,Z,20,cmap='RdGy')
#[Out]# <matplotlib.contour.QuadContourSet at 0x2655e94fda0>
plt.cm.absolute_import
#[Out]# _Feature((2, 5, 0, 'alpha', 1), (3, 0, 0, 'alpha', 0), 16384)
plt.contourf(X,Y,Z,20,cmp='RdGy')
#[Out]# <matplotlib.contour.QuadContourSet at 0x26566a1e128>
plt.colorbar()
#[Out]# <matplotlib.colorbar.Colorbar at 0x2655e937e48>
plt.imshow(Z,extent=[0,5,0,5],origin='lower',cmap='RdGy')
#[Out]# <matplotlib.image.AxesImage at 0x2655f566048>
plt.colorbar()
#[Out]# <matplotlib.colorbar.Colorbar at 0x26566be1ac8>
plt.axis(aspect='image')
#[Out]# (0.0, 5.0, 0.0, 5.0)
contours = plt.contour(X,Y,Z,3,colors ='black')
plt.clabel(contours,inline=True,fontsize=8)
#[Out]# <a list of 14 text.Text objects>
plt.imshow(Z,exteng=[0,5,0,5],origin='lower',cmap='RdGy',alpha==0.5)
plt.colorbar()
#[Out]# <matplotlib.colorbar.Colorbar at 0x265663deda0>
data = np.random.randn(1000)
plt.hist(data)
#[Out]# (array([ 10.,  40.,  93., 190., 240., 223., 143.,  45.,  14.,   2.]),
#[Out]#  array([-2.95332555, -2.31250899, -1.67169243, -1.03087587, -0.39005931,
#[Out]#          0.25075725,  0.89157381,  1.53239037,  2.17320693,  2.81402349,
#[Out]#          3.45484005]),
#[Out]#  <a list of 10 Patch objects>)
plt.hist(data,bins=30,normed=True,alpha=0.5,histtype='stepfilled',color='steelblue')
#[Out]# (array([0.00936305, 0.01404458, 0.02340763, 0.02340763, 0.04681527,
#[Out]#         0.11703817, 0.07490443, 0.21066871, 0.14980886, 0.25280246,
#[Out]#         0.35111452, 0.28557314, 0.33706994, 0.3651591 , 0.42133743,
#[Out]#         0.36984063, 0.34175147, 0.33238841, 0.27152856, 0.25280246,
#[Out]#         0.14512734, 0.1217197 , 0.04681527, 0.04213374, 0.02808916,
#[Out]#         0.02340763, 0.01404458, 0.00468153, 0.        , 0.00468153]),
#[Out]#  array([-2.95332555, -2.73972003, -2.52611451, -2.31250899, -2.09890347,
#[Out]#         -1.88529795, -1.67169243, -1.45808691, -1.24448139, -1.03087587,
#[Out]#         -0.81727035, -0.60366483, -0.39005931, -0.17645379,  0.03715173,
#[Out]#          0.25075725,  0.46436277,  0.67796829,  0.89157381,  1.10517933,
#[Out]#          1.31878485,  1.53239037,  1.74599589,  1.95960141,  2.17320693,
#[Out]#          2.38681245,  2.60041797,  2.81402349,  3.02762901,  3.24123453,
#[Out]#          3.45484005]),
#[Out]#  <a list of 1 Patch objects>)
plt.hist(data,bins=30,normed=True,alpha=0.5,histtype='stepfilled',color='steelblue',edgecolor='none')
#[Out]# (array([0.00936305, 0.01404458, 0.02340763, 0.02340763, 0.04681527,
#[Out]#         0.11703817, 0.07490443, 0.21066871, 0.14980886, 0.25280246,
#[Out]#         0.35111452, 0.28557314, 0.33706994, 0.3651591 , 0.42133743,
#[Out]#         0.36984063, 0.34175147, 0.33238841, 0.27152856, 0.25280246,
#[Out]#         0.14512734, 0.1217197 , 0.04681527, 0.04213374, 0.02808916,
#[Out]#         0.02340763, 0.01404458, 0.00468153, 0.        , 0.00468153]),
#[Out]#  array([-2.95332555, -2.73972003, -2.52611451, -2.31250899, -2.09890347,
#[Out]#         -1.88529795, -1.67169243, -1.45808691, -1.24448139, -1.03087587,
#[Out]#         -0.81727035, -0.60366483, -0.39005931, -0.17645379,  0.03715173,
#[Out]#          0.25075725,  0.46436277,  0.67796829,  0.89157381,  1.10517933,
#[Out]#          1.31878485,  1.53239037,  1.74599589,  1.95960141,  2.17320693,
#[Out]#          2.38681245,  2.60041797,  2.81402349,  3.02762901,  3.24123453,
#[Out]#          3.45484005]),
#[Out]#  <a list of 1 Patch objects>)
plt.hist(data,bins=30,normed=True,alpha=0.5,histtype='stepfilled',color='steelblue',edgecolor='none')
#[Out]# (array([0.00936305, 0.01404458, 0.02340763, 0.02340763, 0.04681527,
#[Out]#         0.11703817, 0.07490443, 0.21066871, 0.14980886, 0.25280246,
#[Out]#         0.35111452, 0.28557314, 0.33706994, 0.3651591 , 0.42133743,
#[Out]#         0.36984063, 0.34175147, 0.33238841, 0.27152856, 0.25280246,
#[Out]#         0.14512734, 0.1217197 , 0.04681527, 0.04213374, 0.02808916,
#[Out]#         0.02340763, 0.01404458, 0.00468153, 0.        , 0.00468153]),
#[Out]#  array([-2.95332555, -2.73972003, -2.52611451, -2.31250899, -2.09890347,
#[Out]#         -1.88529795, -1.67169243, -1.45808691, -1.24448139, -1.03087587,
#[Out]#         -0.81727035, -0.60366483, -0.39005931, -0.17645379,  0.03715173,
#[Out]#          0.25075725,  0.46436277,  0.67796829,  0.89157381,  1.10517933,
#[Out]#          1.31878485,  1.53239037,  1.74599589,  1.95960141,  2.17320693,
#[Out]#          2.38681245,  2.60041797,  2.81402349,  3.02762901,  3.24123453,
#[Out]#          3.45484005]),
#[Out]#  <a list of 1 Patch objects>)
x1 = np.random.normal(0,0.8,1000)
x2 = np.random.normal(-2,1,1000)
x3 = np.random.normal(3,2,1000)
kwargs = dict(histtype='stepfilled',alpha=0.3,normed=True,bins=40)
plt.hist(x1,**kwargs)
#[Out]# (array([0.00596257, 0.        , 0.00596257, 0.        , 0.00596257,
#[Out]#         0.01192513, 0.0536631 , 0.0357754 , 0.10136364, 0.11328878,
#[Out]#         0.14906418, 0.18483958, 0.22657755, 0.32794119, 0.31005349,
#[Out]#         0.399492  , 0.53066848, 0.54855618, 0.399492  , 0.48893051,
#[Out]#         0.42930484, 0.36967916, 0.29812836, 0.31601606, 0.23254012,
#[Out]#         0.14906418, 0.06558824, 0.07155081, 0.08347594, 0.0357754 ,
#[Out]#         0.        , 0.00596257, 0.        , 0.        , 0.        ,
#[Out]#         0.        , 0.        , 0.        , 0.        , 0.00596257]),
#[Out]#  array([-3.00407799, -2.836365  , -2.668652  , -2.500939  , -2.33322601,
#[Out]#         -2.16551301, -1.99780002, -1.83008702, -1.66237403, -1.49466103,
#[Out]#         -1.32694804, -1.15923504, -0.99152205, -0.82380905, -0.65609606,
#[Out]#         -0.48838306, -0.32067007, -0.15295707,  0.01475592,  0.18246892,
#[Out]#          0.35018191,  0.51789491,  0.68560791,  0.8533209 ,  1.0210339 ,
#[Out]#          1.18874689,  1.35645989,  1.52417288,  1.69188588,  1.85959887,
#[Out]#          2.02731187,  2.19502486,  2.36273786,  2.53045085,  2.69816385,
#[Out]#          2.86587684,  3.03358984,  3.20130283,  3.36901583,  3.53672882,
#[Out]#          3.70444182]),
#[Out]#  <a list of 1 Patch objects>)
plt.hist(x1,**kwargs)
#[Out]# (array([0.00596257, 0.        , 0.00596257, 0.        , 0.00596257,
#[Out]#         0.01192513, 0.0536631 , 0.0357754 , 0.10136364, 0.11328878,
#[Out]#         0.14906418, 0.18483958, 0.22657755, 0.32794119, 0.31005349,
#[Out]#         0.399492  , 0.53066848, 0.54855618, 0.399492  , 0.48893051,
#[Out]#         0.42930484, 0.36967916, 0.29812836, 0.31601606, 0.23254012,
#[Out]#         0.14906418, 0.06558824, 0.07155081, 0.08347594, 0.0357754 ,
#[Out]#         0.        , 0.00596257, 0.        , 0.        , 0.        ,
#[Out]#         0.        , 0.        , 0.        , 0.        , 0.00596257]),
#[Out]#  array([-3.00407799, -2.836365  , -2.668652  , -2.500939  , -2.33322601,
#[Out]#         -2.16551301, -1.99780002, -1.83008702, -1.66237403, -1.49466103,
#[Out]#         -1.32694804, -1.15923504, -0.99152205, -0.82380905, -0.65609606,
#[Out]#         -0.48838306, -0.32067007, -0.15295707,  0.01475592,  0.18246892,
#[Out]#          0.35018191,  0.51789491,  0.68560791,  0.8533209 ,  1.0210339 ,
#[Out]#          1.18874689,  1.35645989,  1.52417288,  1.69188588,  1.85959887,
#[Out]#          2.02731187,  2.19502486,  2.36273786,  2.53045085,  2.69816385,
#[Out]#          2.86587684,  3.03358984,  3.20130283,  3.36901583,  3.53672882,
#[Out]#          3.70444182]),
#[Out]#  <a list of 1 Patch objects>)
plt.hist(x2,**kwargs)
#[Out]# (array([0.00703102, 0.01406204, 0.02812409, 0.02109307, 0.02812409,
#[Out]#         0.02812409, 0.04921715, 0.03515511, 0.04921715, 0.13358942,
#[Out]#         0.12655839, 0.18280657, 0.20389964, 0.1617135 , 0.29530292,
#[Out]#         0.34452007, 0.33045803, 0.41483029, 0.49217154, 0.36561314,
#[Out]#         0.36561314, 0.28124088, 0.39373723, 0.31639599, 0.2882719 ,
#[Out]#         0.31639599, 0.26014781, 0.28124088, 0.21796168, 0.2249927 ,
#[Out]#         0.18983759, 0.1617135 , 0.09843431, 0.0632792 , 0.0632792 ,
#[Out]#         0.07734124, 0.04218613, 0.04218613, 0.01406204, 0.02109307]),
#[Out]#  array([-4.9570653 , -4.81483846, -4.67261163, -4.53038479, -4.38815796,
#[Out]#         -4.24593112, -4.10370428, -3.96147745, -3.81925061, -3.67702378,
#[Out]#         -3.53479694, -3.39257011, -3.25034327, -3.10811643, -2.9658896 ,
#[Out]#         -2.82366276, -2.68143593, -2.53920909, -2.39698226, -2.25475542,
#[Out]#         -2.11252859, -1.97030175, -1.82807491, -1.68584808, -1.54362124,
#[Out]#         -1.40139441, -1.25916757, -1.11694074, -0.9747139 , -0.83248707,
#[Out]#         -0.69026023, -0.54803339, -0.40580656, -0.26357972, -0.12135289,
#[Out]#          0.02087395,  0.16310078,  0.30532762,  0.44755446,  0.58978129,
#[Out]#          0.73200813]),
#[Out]#  <a list of 1 Patch objects>)
plt.hist(x3,**kwargs)
#[Out]# (array([0.0200898 , 0.0100449 , 0.0100449 , 0.0167415 , 0.0200898 ,
#[Out]#         0.0368313 , 0.06361771, 0.04687621, 0.09040411, 0.07366261,
#[Out]#         0.11049391, 0.11719051, 0.14062862, 0.15402182, 0.18080822,
#[Out]#         0.20089803, 0.17745992, 0.21094293, 0.22098783, 0.18415652,
#[Out]#         0.21094293, 0.17411162, 0.16406672, 0.14397692, 0.09710071,
#[Out]#         0.10379731, 0.08035921, 0.09040411, 0.04017961, 0.0368313 ,
#[Out]#         0.05022451, 0.0234381 , 0.0100449 , 0.0100449 , 0.0133932 ,
#[Out]#         0.0033483 , 0.        , 0.        , 0.        , 0.0100449 ]),
#[Out]#  array([-2.36539318, -2.0667342 , -1.76807521, -1.46941623, -1.17075724,
#[Out]#         -0.87209826, -0.57343928, -0.27478029,  0.02387869,  0.32253767,
#[Out]#          0.62119666,  0.91985564,  1.21851463,  1.51717361,  1.81583259,
#[Out]#          2.11449158,  2.41315056,  2.71180954,  3.01046853,  3.30912751,
#[Out]#          3.6077865 ,  3.90644548,  4.20510446,  4.50376345,  4.80242243,
#[Out]#          5.10108142,  5.3997404 ,  5.69839938,  5.99705837,  6.29571735,
#[Out]#          6.59437633,  6.89303532,  7.1916943 ,  7.49035329,  7.78901227,
#[Out]#          8.08767125,  8.38633024,  8.68498922,  8.9836482 ,  9.28230719,
#[Out]#          9.58096617]),
#[Out]#  <a list of 1 Patch objects>)
counts,bin_edges = np.histogram(data,bins=5)
print(counts)
mean = [0,0]
cov = [[1,1],[1,2]]
x,y = np.random.multivariate_normal(mean,cov,10000).T
plt.hist2d(x,y,bins=30,cmap='Blues')
#[Out]# (array([[  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   1.,   0.,   1.,   1.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   1.,   1.,   0.,   1.,   0.,   0.,   0.,   1.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   1.,   1.,   0.,   1.,   2.,   0.,
#[Out]#            0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   1.,   5.,   1.,   3.,   4.,   3.,   4.,
#[Out]#            0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   2.,   1.,   2.,   6.,   4.,   9.,   1.,
#[Out]#            2.,   0.,   1.,   0.,   0.,   0.,   1.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   1.,   0.,   3.,   2.,   5.,  12.,  10.,  22.,  18.,   9.,
#[Out]#           17.,  10.,   3.,   1.,   1.,   1.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   9.,  10.,  11.,  18.,  24.,  33.,
#[Out]#           21.,  17.,  12.,   0.,   6.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  1.,   0.,   0.,   2.,   1.,   8.,  15.,  13.,  33.,  42.,  43.,
#[Out]#           44.,  37.,  22.,  18.,  15.,   2.,   1.,   2.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   1.,   0.,   6.,  15.,  27.,  25.,  42.,  45.,
#[Out]#           61.,  56.,  57.,  41.,  17.,  10.,   7.,   2.,   2.,   1.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   1.,   0.,   3.,   1.,  10.,  13.,  36.,  53.,  66.,
#[Out]#           88.,  94.,  81.,  50.,  39.,  29.,  13.,  13.,   2.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   1.,   2.,  13.,  11.,  23.,  53.,  68.,
#[Out]#          109., 101., 132.,  94.,  86.,  56.,  30.,  10.,   7.,   4.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   1.,   2.,   8.,  13.,  35.,  73.,
#[Out]#           98., 124., 128., 129., 123.,  75.,  39.,  31.,  16.,   6.,   2.,
#[Out]#            0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   2.,   6.,  16.,  28.,  37.,
#[Out]#           75., 123., 136., 157., 134., 101.,  82.,  50.,  25.,  11.,   7.,
#[Out]#            0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   7.,  16.,  37.,
#[Out]#           63., 103., 137., 156., 159., 172., 100.,  94.,  44.,  23.,  11.,
#[Out]#            1.,   3.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   5.,   8.,  20.,
#[Out]#           38.,  67.,  97., 146., 183., 165., 122., 113.,  76.,  45.,  18.,
#[Out]#            4.,   4.,   0.,   1.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   3.,   7.,
#[Out]#           19.,  46.,  72.,  90., 128., 119., 139., 117.,  93.,  56.,  25.,
#[Out]#           17.,   2.,   0.,   0.,   1.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   4.,
#[Out]#           10.,  21.,  39.,  75., 108., 125., 121., 127.,  81.,  55.,  31.,
#[Out]#           20.,  13.,   4.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   2.,
#[Out]#            5.,  10.,  22.,  34.,  41.,  80.,  91.,  81.,  77.,  56.,  39.,
#[Out]#           18.,  15.,   5.,   3.,   1.,   1.,   1.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            1.,   3.,   7.,  17.,  33.,  42.,  50.,  49.,  61.,  68.,  39.,
#[Out]#           27.,  12.,   5.,   5.,   0.,   1.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   4.,   7.,  12.,  20.,  38.,  47.,  43.,  34.,  39.,
#[Out]#           24.,  13.,  11.,   2.,   1.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   3.,   4.,   9.,  14.,  21.,  28.,  14.,  21.,
#[Out]#           15.,  16.,  11.,   6.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   1.,   1.,   2.,   2.,   5.,  14.,   5.,  15.,  14.,
#[Out]#           20.,   9.,   4.,   3.,   1.,   1.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   1.,   0.,   2.,   1.,   4.,   9.,   8.,
#[Out]#            6.,   8.,   6.,   2.,   1.,   0.,   0.,   1.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   2.,   5.,   5.,
#[Out]#            7.,   0.,   1.,   2.,   1.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   1.,   2.,   1.,
#[Out]#            1.,   2.,   1.,   1.,   1.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   3.,
#[Out]#            0.,   1.,   0.,   1.,   0.,   0.,   0.,   1.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   1.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#         [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#            0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.]]),
#[Out]#  array([-4.07062228, -3.7912677 , -3.51191312, -3.23255854, -2.95320395,
#[Out]#         -2.67384937, -2.39449479, -2.11514021, -1.83578562, -1.55643104,
#[Out]#         -1.27707646, -0.99772188, -0.71836729, -0.43901271, -0.15965813,
#[Out]#          0.11969645,  0.39905104,  0.67840562,  0.9577602 ,  1.23711478,
#[Out]#          1.51646937,  1.79582395,  2.07517853,  2.35453311,  2.6338877 ,
#[Out]#          2.91324228,  3.19259686,  3.47195144,  3.75130603,  4.03066061,
#[Out]#          4.31001519]),
#[Out]#  array([-5.77130296, -5.39231372, -5.01332448, -4.63433524, -4.25534601,
#[Out]#         -3.87635677, -3.49736753, -3.11837829, -2.73938905, -2.36039982,
#[Out]#         -1.98141058, -1.60242134, -1.2234321 , -0.84444287, -0.46545363,
#[Out]#         -0.08646439,  0.29252485,  0.67151409,  1.05050332,  1.42949256,
#[Out]#          1.8084818 ,  2.18747104,  2.56646027,  2.94544951,  3.32443875,
#[Out]#          3.70342799,  4.08241722,  4.46140646,  4.8403957 ,  5.21938494,
#[Out]#          5.59837418]),
#[Out]#  <matplotlib.image.AxesImage at 0x265671bafd0>)
cb = plt.colorbar()
cb.set_label('counts in bin')
counts,xedges,yedges = np.histogram2d(x,y,bins=30)
counts
#[Out]# array([[  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   1.,   0.,   1.,   1.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   1.,   1.,   0.,   1.,   0.,   0.,   0.,   1.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   1.,   1.,   0.,   1.,   2.,   0.,
#[Out]#           0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   1.,   5.,   1.,   3.,   4.,   3.,   4.,
#[Out]#           0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   2.,   1.,   2.,   6.,   4.,   9.,   1.,
#[Out]#           2.,   0.,   1.,   0.,   0.,   0.,   1.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   1.,   0.,   3.,   2.,   5.,  12.,  10.,  22.,  18.,   9.,
#[Out]#          17.,  10.,   3.,   1.,   1.,   1.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   9.,  10.,  11.,  18.,  24.,  33.,
#[Out]#          21.,  17.,  12.,   0.,   6.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  1.,   0.,   0.,   2.,   1.,   8.,  15.,  13.,  33.,  42.,  43.,
#[Out]#          44.,  37.,  22.,  18.,  15.,   2.,   1.,   2.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   1.,   0.,   6.,  15.,  27.,  25.,  42.,  45.,
#[Out]#          61.,  56.,  57.,  41.,  17.,  10.,   7.,   2.,   2.,   1.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   1.,   0.,   3.,   1.,  10.,  13.,  36.,  53.,  66.,
#[Out]#          88.,  94.,  81.,  50.,  39.,  29.,  13.,  13.,   2.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   1.,   2.,  13.,  11.,  23.,  53.,  68.,
#[Out]#         109., 101., 132.,  94.,  86.,  56.,  30.,  10.,   7.,   4.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   1.,   2.,   8.,  13.,  35.,  73.,
#[Out]#          98., 124., 128., 129., 123.,  75.,  39.,  31.,  16.,   6.,   2.,
#[Out]#           0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   2.,   6.,  16.,  28.,  37.,
#[Out]#          75., 123., 136., 157., 134., 101.,  82.,  50.,  25.,  11.,   7.,
#[Out]#           0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   7.,  16.,  37.,
#[Out]#          63., 103., 137., 156., 159., 172., 100.,  94.,  44.,  23.,  11.,
#[Out]#           1.,   3.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   5.,   8.,  20.,
#[Out]#          38.,  67.,  97., 146., 183., 165., 122., 113.,  76.,  45.,  18.,
#[Out]#           4.,   4.,   0.,   1.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   3.,   7.,
#[Out]#          19.,  46.,  72.,  90., 128., 119., 139., 117.,  93.,  56.,  25.,
#[Out]#          17.,   2.,   0.,   0.,   1.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   4.,
#[Out]#          10.,  21.,  39.,  75., 108., 125., 121., 127.,  81.,  55.,  31.,
#[Out]#          20.,  13.,   4.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   2.,
#[Out]#           5.,  10.,  22.,  34.,  41.,  80.,  91.,  81.,  77.,  56.,  39.,
#[Out]#          18.,  15.,   5.,   3.,   1.,   1.,   1.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           1.,   3.,   7.,  17.,  33.,  42.,  50.,  49.,  61.,  68.,  39.,
#[Out]#          27.,  12.,   5.,   5.,   0.,   1.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   4.,   7.,  12.,  20.,  38.,  47.,  43.,  34.,  39.,
#[Out]#          24.,  13.,  11.,   2.,   1.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   3.,   4.,   9.,  14.,  21.,  28.,  14.,  21.,
#[Out]#          15.,  16.,  11.,   6.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   1.,   1.,   2.,   2.,   5.,  14.,   5.,  15.,  14.,
#[Out]#          20.,   9.,   4.,   3.,   1.,   1.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   1.,   0.,   2.,   1.,   4.,   9.,   8.,
#[Out]#           6.,   8.,   6.,   2.,   1.,   0.,   0.,   1.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   2.,   5.,   5.,
#[Out]#           7.,   0.,   1.,   2.,   1.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   1.,   2.,   1.,
#[Out]#           1.,   2.,   1.,   1.,   1.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   3.,
#[Out]#           0.,   1.,   0.,   1.,   0.,   0.,   0.,   1.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   1.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
#[Out]#        [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
#[Out]#           0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.]])
import matplotlib.pyplot as plt
plt.style.use('classic')
x = np.linspace(0,10,1000)
fig,ax = plt.subplots()
ax.plot(x,np.sin(x),'-b',label='Sine')
#[Out]# [<matplotlib.lines.Line2D at 0x2655f5fd2e8>]
ax.plot(x,np.cos(x),'--r',label='Cosine')
#[Out]# [<matplotlib.lines.Line2D at 0x265680d4160>]
ax.axis('equal')
#[Out]# (0.0, 10.0, -1.0, 1.0)
leg = ax.legend()
ax.legend(loc='upper left',frameon=False)
#[Out]# <matplotlib.legend.Legend at 0x26568c6fd68>
fig
#[Out]# <matplotlib.figure.Figure at 0x2655f4d8e80>
ax.legend(loc='lower center',ncol=2,frameon=False)
#[Out]# <matplotlib.legend.Legend at 0x2656858d780>
ax.legend(fancbox=True,framealpha=1,shadow=True,borderpad=1)
ax.legend(fancybox=True,framealpha=1,shadow=True,borderpad=1)
#[Out]# <matplotlib.legend.Legend at 0x2655e0eb048>
y = np.sin(x[:,np,newaxis] + np.pi * np.arange(0,2,0.5))
y = np.sin(x[:,np.newaxis] + np.pi * np.arange(0,2,0.5))
lines = plt.plot(x,y)
plt.legend(lines[:2],['first','second'])
#[Out]# <matplotlib.legend.Legend at 0x265671a55f8>
y = np.sin(x[:,np.newaxis] + np.pi * np.arange(0,2,0.5))
lines = plt.plot(x,y)
plt.legend(lines[:2],['first','second'])
#[Out]# <matplotlib.legend.Legend at 0x26568aef4e0>
plt.draw()
plt.show()
plt.plot(x,y[:,0],label='fisrt')
#[Out]# [<matplotlib.lines.Line2D at 0x2655f654320>]
plt.plot(x,y[:,1],label='second')
#[Out]# [<matplotlib.lines.Line2D at 0x265671895f8>]
plt.plot(x,y[:,2:])
#[Out]# [<matplotlib.lines.Line2D at 0x2656718bcc0>,
#[Out]#  <matplotlib.lines.Line2D at 0x2655f606278>]
plt.legend(framealpha=1,frameon='True)
plt.legend(framealpha=1,frameon='True')
#[Out]# <matplotlib.legend.Legend at 0x265692c6208>
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', '数据集/')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'data/')
get_ipython().run_line_magic('ls', '')
cities = pd.read_csv('california_cities.csv')
get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('ls', '')
cities.columns
#[Out]# Index(['Unnamed: 0', 'city', 'latd', 'longd', 'elevation_m', 'elevation_ft',
#[Out]#        'population_total', 'area_total_sq_mi', 'area_land_sq_mi',
#[Out]#        'area_water_sq_mi', 'area_total_km2', 'area_land_km2', 'area_water_km2',
#[Out]#        'area_water_percent'],
#[Out]#       dtype='object')
lat,lon = cities['latd'],cities['longd']
population,area = cities['population_total'],cities['area_total_km2']
plt.scatter(lon.lat,label=None,c=np.log10(population),cmap='viridis',s=area,linewidth=0,alpha=0.5)
plt.scatter(lon,lat,label=None,c=np.log10(population),cmap='viridis',s=area,linewidth=0,alpha=0.5)
#[Out]# <matplotlib.collections.PathCollection at 0x2656d5bcbe0>
plt.axis(aspect='equal')
#[Out]# (-126.0, -114.0, 32.0, 44.0)
plt.xlabel('longitude')
#[Out]# Text(0.5,23.7,'longitude')
plt.ylabel('latitude')
#[Out]# Text(53,0.5,'latitude')
plt.colorbar(label='log$){10}$(population)')
#[Out]# <matplotlib.colorbar.Colorbar at 0x2655f4f7978>
plt.clim(3,7)
for area in [100.300.500]:
for area in [100.300.500]:
for area in [100,300,500]:
    plt.scatter([],[],c='k',alpha=0.3,s=area,label=str(area)+' km$^2$')
    
plt.legend(scatterpoints=1,frameon=False,labelspacing=1,title='City Area')
#[Out]# <matplotlib.legend.Legend at 0x2656cd44748>
plt.title('California Cities:Area and Population')
#[Out]# Text(0.5,1,'California Cities:Area and Population')
from sklearn.datasets import load_digits
digits = load_digits(n_class=6)
fig,ax = plt.subplots(8,8,figsize=(6,6))
fig,ax = plt.subplots(8,8,figsize=(6,6))
for i,axi in enumerate(ax.flat):
    axi,imshow(digitis.images[i],cmap='binary')
    axi.set(xticks=[],yticks=[])
    
for i,axi in enumerate(ax.flat):
    axi,imshow(digits.images[i],cmap='binary')
    axi.set(xticks=[],yticks=[])
    
import matplotlib.pyplot as plt
ax1= plt.axes()
ax2 = plt.axes([0.65,0.65,0.2,0.2])
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.5,0.8,0.4]),xticklabels=[],ylim=(-1.2,1.2))
ax1 = fig.add_axes([0.1,0.5,0.8,0.4]),xticklabels=[],ylim=(-1.2,1.2))
ax1 = fig.add_axes([0.1,0.5,0.8,0.4],xticklabels=[],ylim=(-1.2,1.2))
ax2 = fig.add_axes([0.1,0.1,0.8,0.4],ylim=(-1.2,1.2))
x = np.linspace(0,10)
ax1.plot(np.sin(x))
#[Out]# [<matplotlib.lines.Line2D at 0x26573e05b70>]
ax2.plot(np.cos(x))
#[Out]# [<matplotlib.lines.Line2D at 0x26573e1bc50>]
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.5,0.8,0.4],xticklabels=[],ylim=(-1.2,1.2))
ax2 = fig.add_axes([0.1,0.1,0.8,0.4],ylim=(-1.2,1.2))
ax3 = fig.add_axes([0.1,0.9,0.8,0.4],ylim=(-1.2,1.2))
ax3 = fig.add_axes([0.1,0.1,0.8,0.4],ylim=(-1.2,1.2))
for i in range(1,7):
    plt.subplot(2,3,i)
    plt.text(0.5,0.5,str((2,3,i)),fontsize=18,ha='center')
    
fig = plt.figure()
fig.subplots_adjust(hspace=0.4,wspace=0.4)
for i in range(1,7):
    ax.subplot(2,3,i)
    ax.text(0.5,0.5,str((2,3,i)),fontsize=18,ha='center')
    
    
for i in range(1,7):
    ax = fig.add_subplot(2,3,i)
    ax.text(0.5,0.5,str((2,3,i)),fontsize=18,ha='center')
    
    
fig,ax = plt.subplots(2,3,sharex='col',sharey='row')
for i in range(2):
    for j in range(3):
        ax[i,j].text(0.5,0.5,str((i,j)),fontsize=18,ha='center')
        
import matplotlib as mpl
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'data/')
get_ipython().run_line_magic('ls', '')
births = pd.read_csv('births.csv')
births.columns
#[Out]# Index(['year', 'month', 'day', 'gender', 'births'], dtype='object')
quartiles = np.percentile(births['births'],[25,50,75])
quartiles.head()
quartiles.head[:5]
len(quartiles)
#[Out]# 3
quartiles
#[Out]# array([4358. , 4814. , 5289.5])
births.shape
#[Out]# (15547, 5)
quartiles.sum()
#[Out]# 14461.5
births['births'].value_counts()
#[Out]# 2         95
#[Out]# 4         54
#[Out]# 1         42
#[Out]# 8         28
#[Out]# 6         28
#[Out]# 3         22
#[Out]# 5226      21
#[Out]# 4598      21
#[Out]# 5110      20
#[Out]# 14        19
#[Out]# 5180      19
#[Out]# 4768      19
#[Out]# 12        18
#[Out]# 4514      18
#[Out]# 4660      18
#[Out]# 5006      17
#[Out]# 4872      17
#[Out]# 4472      17
#[Out]# 5080      17
#[Out]# 5024      17
#[Out]# 4944      17
#[Out]# 4588      17
#[Out]# 4656      16
#[Out]# 4489      16
#[Out]# 5170      16
#[Out]# 4490      16
#[Out]# 4480      16
#[Out]# 5380      16
#[Out]# 5204      16
#[Out]# 4488      16
#[Out]#           ..
#[Out]# 182707     1
#[Out]# 5903       1
#[Out]# 5871       1
#[Out]# 3820       1
#[Out]# 179938     1
#[Out]# 180098     1
#[Out]# 151260     1
#[Out]# 3804       1
#[Out]# 166443     1
#[Out]# 174639     1
#[Out]# 171718     1
#[Out]# 169585     1
#[Out]# 3868       1
#[Out]# 165661     1
#[Out]# 156054     1
#[Out]# 165669     1
#[Out]# 160124     1
#[Out]# 5935       1
#[Out]# 152641     1
#[Out]# 164186     1
#[Out]# 5959       1
#[Out]# 6473       1
#[Out]# 5983       1
#[Out]# 155502     1
#[Out]# 6417       1
#[Out]# 5999       1
#[Out]# 266        1
#[Out]# 157561     1
#[Out]# 169225     1
#[Out]# 165889     1
#[Out]# Name: births, Length: 3137, dtype: int64
(births['births'],isnull).value_counts()
(births['births'].isnull).value_counts()
(births['births'].isnull()).value_counts()
#[Out]# False    15547
#[Out]# Name: births, dtype: int64
len(quartiles)
#[Out]# 3
births.shape
#[Out]# (15547, 5)
quartiles
#[Out]# array([4358. , 4814. , 5289.5])
quartiles_1 = quartiles.copy()
quartiles_1 = np.percentile(births['births'],[25,50,75,100])
quartiles_1
#[Out]# array([  4358. ,   4814. ,   5289.5, 199622. ])
quartiles_1 = np.percentile(births['births'],[0,25,50,75])
quartiles_1
#[Out]# array([1.0000e+00, 4.3580e+03, 4.8140e+03, 5.2895e+03])
mu,sig = quartiles[1],0.74 * (quartiles[2] - quartiles[0])
births = births.query('(births >@mu-5*@sig) & (birth < @mu +5 * @sig)')
births = births.query('(births >@mu-5*@sig) & (births < @mu +5 * @sig)')
births
#[Out]#        year  month   day gender  births
#[Out]# 0      1969      1   1.0      F    4046
#[Out]# 1      1969      1   1.0      M    4440
#[Out]# 2      1969      1   2.0      F    4454
#[Out]# 3      1969      1   2.0      M    4548
#[Out]# 4      1969      1   3.0      F    4548
#[Out]# 5      1969      1   3.0      M    4994
#[Out]# 6      1969      1   4.0      F    4440
#[Out]# 7      1969      1   4.0      M    4520
#[Out]# 8      1969      1   5.0      F    4192
#[Out]# 9      1969      1   5.0      M    4198
#[Out]# 10     1969      1   6.0      F    4710
#[Out]# 11     1969      1   6.0      M    4850
#[Out]# 12     1969      1   7.0      F    4646
#[Out]# 13     1969      1   7.0      M    5092
#[Out]# 14     1969      1   8.0      F    4800
#[Out]# 15     1969      1   8.0      M    4934
#[Out]# 16     1969      1   9.0      F    4592
#[Out]# 17     1969      1   9.0      M    4842
#[Out]# 18     1969      1  10.0      F    4852
#[Out]# 19     1969      1  10.0      M    5190
#[Out]# 20     1969      1  11.0      F    4580
#[Out]# 21     1969      1  11.0      M    4598
#[Out]# 22     1969      1  12.0      F    4126
#[Out]# 23     1969      1  12.0      M    4324
#[Out]# 24     1969      1  13.0      F    4758
#[Out]# 25     1969      1  13.0      M    5076
#[Out]# 26     1969      1  14.0      F    5070
#[Out]# 27     1969      1  14.0      M    5296
#[Out]# 28     1969      1  15.0      F    4798
#[Out]# 29     1969      1  15.0      M    5096
#[Out]# ...     ...    ...   ...    ...     ...
#[Out]# 15037  1988     12  17.0      F    4270
#[Out]# 15038  1988     12  17.0      M    4486
#[Out]# 15039  1988     12  18.0      F    4211
#[Out]# 15040  1988     12  18.0      M    4220
#[Out]# 15041  1988     12  19.0      F    5651
#[Out]# 15042  1988     12  19.0      M    6065
#[Out]# 15043  1988     12  20.0      F    6092
#[Out]# 15044  1988     12  20.0      M    6343
#[Out]# 15045  1988     12  21.0      F    5462
#[Out]# 15046  1988     12  21.0      M    5861
#[Out]# 15047  1988     12  22.0      F    5219
#[Out]# 15048  1988     12  22.0      M    5510
#[Out]# 15049  1988     12  23.0      F    4887
#[Out]# 15050  1988     12  23.0      M    5110
#[Out]# 15051  1988     12  24.0      F    4024
#[Out]# 15052  1988     12  24.0      M    4269
#[Out]# 15053  1988     12  25.0      F    3874
#[Out]# 15054  1988     12  25.0      M    3961
#[Out]# 15055  1988     12  26.0      F    4274
#[Out]# 15056  1988     12  26.0      M    4409
#[Out]# 15057  1988     12  27.0      F    5633
#[Out]# 15058  1988     12  27.0      M    5895
#[Out]# 15059  1988     12  28.0      F    5858
#[Out]# 15060  1988     12  28.0      M    5989
#[Out]# 15061  1988     12  29.0      F    5760
#[Out]# 15062  1988     12  29.0      M    5944
#[Out]# 15063  1988     12  30.0      F    5742
#[Out]# 15064  1988     12  30.0      M    6095
#[Out]# 15065  1988     12  31.0      F    4435
#[Out]# 15066  1988     12  31.0      M    4698
#[Out]# 
#[Out]# [14610 rows x 5 columns]
births['day'] = births['day'].astype(int)
births.index = pd.to_datetime(10000*births.year + 100 * births.month + births.day,format='%Y%m%d')
births_by_date = births.pivot_table('births',[births.index.month,births.index.day])
births_by_date.index = [pd.datetime(2012,month,day) for (month,day) in births_by_date.index]
fig,ax = plt.subplots(figsize=(12,4))
births_by_date.plot(ax=ax)
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x26577dd7240>
style = dict(size=10,color='gray')
ax.text('2012-1-1',3950,'New Year"s Day',**style)
ax.text('2012-1-1',3950,'New Year"s Day',**style)
ax.text('2012-1-1',3950,'New Year Day',**style)
ax.text('2012-1-1',3950,'New Year Day')
ax.text('2012-1-1',3950,'New Year Day',**style)
get_ipython().run_line_magic('pinfo', 'ax.text')
ax.text('2012-1-1',3950,'New Year Day',**style)
style = dict(size=10,color='gray')
ax.text('2012-1-1',4250,'Independence Day',ha='center',**style)
ax.text('2012-1-1',3950,'New Year Day',**style)
ax
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x26577dd7240>
ax.text('2012-12-25',3850,'Christmas',ha='right',**style)
fig,ax = plt.subplots(facecolor='lightgray')
ax.axis([0,10,0,10])
#[Out]# [0, 10, 0, 10]
ax.text(1,5,'.Data:(1,5)',transform=ax.transData)
#[Out]# Text(1,5,'.Data:(1,5)')
ax.text(0.5,0.1,'.Axes:(0.5,0.1)',transform=ax.transAxes)
#[Out]# Text(0.5,0.1,'.Axes:(0.5,0.1)')
ax.text(0.2,0.2,'.Figure:(0.2,0.2)',transform=fig.transFigure)
#[Out]# Text(0.2,0.2,'.Figure:(0.2,0.2)')
ax.set_xlim(0,2)
#[Out]# (0, 2)
plt.draw()
ax.set_ylim(-6,6)
#[Out]# (-6, 6)
fig
#[Out]# <matplotlib.figure.Figure at 0x265701d4780>
fig,ax = plt.subplots()
x = np.linspace(0,20,1000)
ax.plot(x,np.cos(x))
#[Out]# [<matplotlib.lines.Line2D at 0x26575f1b2b0>]
ax.axis('equal')
#[Out]# (0.0, 20.0, -1.0, 1.0)
ax.annotate('local maximum',xy=(6.28,1),xytext=(10,4),arrowprops=dict(facecolor='black',shrink=0.05))
#[Out]# Text(10,4,'local maximum')
ax.annotate('local maximum',xy=(5 * np.pi,-1),xytext=(2,-6),arrowprops=dict(arrowstyle='->',connectionstyle='angle3,angleA=0,angleB=0))
ax.annotate('local maximum',xy=(5 * np.pi,-1),xytext=(2,-6),arrowprops=dict(arrowstyle='->',connectionstyle='angle3,angleA=0,angleB=0'))
#[Out]# Text(2,-6,'local maximum')
ax.annotate('local maximum',xy=(5 * np.pi,-1),xytext=(2,-6),arrowprops=dict(arrowstyle='->',connectionstyle='angle3,angleA=0,angleB=1'))
#[Out]# Text(2,-6,'local maximum')
get_ipython().run_line_magic('pinfo', 'ax.annotate')
ax.annotate('local maximum',xy=(5 * np.pi,-1),xytext=(2,-6),arrowprops=dict(arrowstyle='->',connectionstyle='angle3'))
#[Out]# Text(2,-6,'local maximum')
ax.annotate('local maximum',xy=(5 * np.pi,-1),xytext=(2,-6),arrowprops=dict(arrowstyle='->',connectionstyle='angle3,angleA=0,angleB=0'))
#[Out]# Text(2,-6,'local maximum')
ax.annotate('local maximum',xy=(5 * np.pi,-1),xytext=(2,-6),arrowprops=dict(arrowstyle='->',connectionstyle='angle3,angleA=90,angleB=0'))
#[Out]# Text(2,-6,'local maximum')
ax.annotate('local maximum',xy=(5 * np.pi,-1),xytext=(2,-6),arrowprops=dict(arrowstyle='->',connectionstyle='arc3'))
#[Out]# Text(2,-6,'local maximum')
ax.annotate('local maximum',xy=(5 * np.pi,-1),xytexrrowprops=dict(arrowstyle='->',connectionstyle='arc3'))
ax.annotate('local maximum',xy=(5 * np.pi,-1),xytex,arrowprops=dict(arrowstyle='->',connectionstyle='angle3,angleA=0,angleB=0'))
ax.annotate('local maximum',xy=(5 * np.pi,-1),xytex,arrowprops=dict(arrowstyle='->',connectionstyle='angle3,angleA=90,angleB=0'))
ax.annotate('local minimum',xy=(5 * np.pi,-1),xytext=(2.-6),arrowprops=dict(arrowstyle='->',connectionstyle='angle3,angleA=0,angleB=0'))
ax.annotate('local minimum',xy=(5 * np.pi,-1),xytext=(2,-6),arrowprops=dict(arrowstyle='->',connectionstyle='angle3,angleA=0,angleB=0'))
#[Out]# Text(2,-6,'local minimum')
ax.annotate('local minimum',xy=(5 * np.pi,-1),xytext=(2,-6),arrowprops=dict(arrowstyle='->',connectionstyle='arc3'))
#[Out]# Text(2,-6,'local minimum')
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy
ax = plt.axes(xscale='log',yscale='log')
ax = plt.axes(xscale='log',yscale='log')
print(ax.xaxis.get_major_locator())
print(ax.xaxis.get_minor_locator())
print(ax.xaxis.get_major_formatter())
print(ax.xaxis.get_minor_formatter())
ax = plt.axes()
ax.plot(np.random.rand(50))
#[Out]# [<matplotlib.lines.Line2D at 0x26577620128>]
ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())
fig,ax = plt.subplots(5,5,figsize=(5,5))
fig.subplots_adjust(hspace=0,wspace=0)
from  sklearn.datasets import fetch_olivetti_faces
faces = fetch_olivetti_faces().images
for j in range(5):
    ax[i,j].xaxis.set_major_locator(plt.NullLocator())
    ax[i,j].yaxis.set_major_locator(plt.NullLocator())
    ax[i,j].imshow(faces[10*i + j],cmap='bone')
    
for i in range(5):
    for j in range(5):
        ax[i,j].xaxis.set_major_locator(plt.NullLocator())
        ax[i,j].yaxis.set_major_locator(plt.NullLocator())
        ax[i,j].imshow(faces[10*i + j],cmap='bone')
        
    
plt.show()
fig,ax = plt.subplots(5,5,figsize=(5,5))
fig.subplots_adjust(hspace=0,wspace=0)
for i in range(5):
    for j in range(5):
        ax[i,j].xaxis.set_major_locator(plt.NullLocator())
        ax[i,j].yaxis.set_major_locator(plt.NullLocator())
        ax[i,j].imshow(faces[10*i + j],cmap='bone')
        
    
fig,ax = plt.subplots(4,4,sharex=True,sharey=True)
for axi in ax.flat:
    axi.xaxis.set_major_locator(plt.MaxNLocator(3))
    axi.yaxis.set_major_locator(plt.MaxNLocator(3))
    
get_ipython().run_line_magic('logstop', '')
