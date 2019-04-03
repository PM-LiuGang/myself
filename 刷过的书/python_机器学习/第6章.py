# -*- coding: utf-8 -*-
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import validation_curve
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
"""
创建时间 Mon Jan 28 15:15:36 2019
作者:PM.liugang
描述:
review:190330-6.1&6.2
遗留：plt图中画横竖线，表示点的具体坐标
#from sklearn.pipeline import Pipeline
#pipe_lr = Pipeline([('scl',ss),
#                    ('pca',pca),
#                    ('clf',LogisticRegression(solver="saga", random_state=1))])

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from warnings import filterwarnings
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold  # 分层K交叉
from sklearn.model_selection import cross_val_score

filterwarnings("ignore")

plt.rcParams['font.sans-serif'] = ['SimHei']  # 输出中文
plt.rcParams['axes.unicode_minus'] = False  # 正负轴显示

print("**********开始6.1章节**************")
print("用管道方法简化工作流")
print("获取数据....")
df = pd.read_csv('wdbc.data', header=None)
feature = df.iloc[:, 2:].values
label = df.iloc[:, 1].values

le = LabelEncoder()
label = le.fit_transform(label)

X_train, X_test, y_train, y_test = train_test_split(feature, label,
                                                    test_size=0.7)

print("转换标签......")
print("转换前的标签的是{0}".format(le.classes_))
print("转换后的标签的是{0}".format(le.transform(["M", "B"])))

print("开始用管道化流完成拟合和转换的步骤......")
ss = StandardScaler()
pca = PCA(n_components=2)
pipe_lr = make_pipeline(ss, pca, LogisticRegression(solver="saga",
                                                    max_iter=19999,
                                                    random_state=1))
pipe_lr.fit(X_train, y_train)
pipe_lr_score = pipe_lr.score(X_test, y_test)
print("开始预测....")
print('测试准确率：%.2f%%\n' % float(pipe_lr_score * 100))

print("**************开始6.2章节**************")
print("使用K折交叉验证评估模型性能")
print("开始分层K折交叉验证....")
kfold = StratifiedKFold(n_splits=10, random_state=1).split(X_train, y_train)
scores = []
for k, (train, test) in enumerate(kfold):  # 170, 17
    pipe_lr.fit(X_train[train], y_train[train])
    score = pipe_lr.score(X_train[test], y_train[test])
    scores.append(score)
    print("%2d折, Class dist.: %s, Acc: %.3f%%" %
          (k + 1, np.bincount(y_train[train]), float(score)*100))
print("交叉验证的准确率: %.3f +/- %.3f" % (np.mean(scores), np.std(scores)))
print("开始分层交叉验证(K折交叉验证得分器，这种方法更为简洁)....")
scores = cross_val_score(estimator=pipe_lr, X=X_train, y=y_train, cv=10,
                         n_jobs=1)
print("交叉验证的准确率: %.3f +/- %.3f\n" % (np.mean(scores), np.std(scores)))

print("**************开始6.3.1章节**************")
print("用学习曲线调试算法")
pipe_lr = make_pipeline(ss, LogisticRegression(solver="saga",
                                               max_iter=19099,
                                               random_state=1))
trainSize, trainScores, testScore = learning_curve(estimator=pipe_lr,
                                                   X=X_train,
                                                   y=y_train,
                                                   train_sizes=np.linspace(0.1, 1.0, 10), cv=10, n_jobs=1)

trainMean = np.mean(trainScores, axis=1)
trainStd = np.std(trainScores, axis=1)
testMean = np.mean(testScore, axis=1)
testStd = np.std(testScore, axis=1)

fig = plt.figure(dpi=80)
plt.plot(trainSize, trainMean, color="blue", marker="o", markersize=5,
         label="training accuracy")
plt.fill_between(trainSize, trainMean + trainStd, trainMean - trainStd,
                 alpha=.15,color="blue")
plt.plot(trainSize, testMean, color="green", marker="s", markersize=5,
         label="validation accuracy")
plt.fill_between(trainSize, testMean + testStd, testMean - testStd, alpha=.15,
                 color="green")
plt.axvline(50, ymin=0.0, ymax=0.78,linestyle="--", color="r" )
plt.text(x=.70, y=.50, s="50")
plt.grid()
plt.xlabel("训练样本数")
plt.ylabel("准确率")
plt.legend(loc="lower right")
plt.ylim([.7, 1.05])
plt.show()

print("**************开始6.3.2章节**************")
print("用验证曲线调试算法")
param_range = [.001, .01, .1, 1.0, 10.1, 100.]
trainScores, testScores = validation_curve(estimator=pipe_lr, X=X_train, y=y_train,
                                           param_name="logisticregression__C",
                                           param_range=param_range,
                                           cv=10)
trainMean = np.mean(trainScores, axis=1)
trainStd = np.std(trainScores, axis=1)
testMean = np.mean(testScores, axis=1)
testStd = np.std(testScores, axis=1)

fig1 = plt.figure(dpi=80)
plt.plot(param_range, trainMean, color="blue", marker="o", markersize=5,
         label="训练准确率")
plt.fill_between(param_range, trainMean + trainStd, trainMean - trainStd,
                 alpha=.15,
                 color="blue")
plt.plot(param_range, testMean, color="green", marker="s", markersize=5,
         label="测试准确率")
plt.fill_between(param_range, testMean + testStd, testMean - testStd, alpha=.15,
                 color="green")
plt.grid()
plt.xscale("log")
plt.xlabel("参数")
plt.ylabel("准确率")
plt.legend(loc="lower right")
plt.ylim([.7, 1.03])
plt.show()

print("**************开始6.4章节**************")
print("通过网格搜索为机器学习模型调优")
pipe_svc = make_pipeline(ss, SVC(random_state=1))
param_range = [.0001, .001, .01, .1, 1., 10., 100., 1000.]
param_grid = [{"svc__C": param_range, "svc__kernel": ["linear"]},  # must svc__
              {"svc__C": param_range, "svc__kernel": ["rbf"],
               "svc__gamma": param_range}]
gs = GridSearchCV(estimator=pipe_svc, param_grid=param_grid,
                  scoring="accuracy",
                  iid=True,  # furture change
                  cv=10,
                  n_jobs=1)
gs = gs.fit(X_train, y_train)
print("通过网格搜素后，最好模型的得分: \n", gs.best_score_)
print("通过网格搜索后，最好模型的参数: \n", gs.best_params_)

clf = gs.best_estimator_
clf.fit(X_train, y_train)
print("Test accuracy: %.3f" % clf.score(X_test, y_test))
print("以嵌套式交叉验证来选择算法")
gs = GridSearchCV(estimator=pipe_svc,
                  param_grid=param_grid,
                  scoring="accuracy",
                  iid=True,  # furture change
                  cv=2)
scores = cross_val_score(gs, X_train, y_train,
                         scoring="accuracy",
                         cv=5)
print("支持向量机模型的嵌套式交叉验证模型")
print("CV accuracy: %.3f +/= %.3f\n" % (np.mean(scores), np.std(scores)))
gs = GridSearchCV(estimator=DecisionTreeClassifier(random_state=0),
                  param_grid=[{"max_depth": [1, 2, 3, 4, 5, 6, 7, None]}],
                  scoring="accuracy",
                  iid=True,  # furture change
                  cv=2)
scores = cross_val_score(gs, X_train, y_train,
                         scoring="accuracy",
                         cv=5)
print("决策树模型验证模型")
print("CV accuracy: %.3f +/= %.3f\n" % (np.mean(scores), np.std(scores)))

print("**************开始6.5章节**************")
print("6.5.1混淆矩阵分析")
from sklearn.metrics import confusion_matrix
pipe_svc.fit(X_train, y_train)
y_pred = pipe_svc.predict(X_test)
confmat = confusion_matrix(y_true=y_test, y_pred=y_pred)
print("混淆矩阵")
print(confmat)

fig, ax = plt.subplots(figsize=(2.5, 2.5))  # subplots
ax.matshow(confmat, alpha=.3)  # cmap=plt.cm.Blues
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
        ax.text(x=j, y=i,  # 坐标 可以通过transform进行改变
                s=confmat[i, j],  # 文本
                va="center", ha="center")
plt.xlabel("预测分类标签")
plt.ylabel("真实分类标签")
plt.show()

print("6.5.2优化分类模型的准确度和召回率")
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score, f1_score

print("精度: %.3f" % precision_score(y_true=y_test, y_pred=y_pred))
print("召回率: %.3f" % recall_score(y_true=y_test, y_pred=y_pred))
print("F1-得分: %.3f" % f1_score(y_true=y_test, y_pred=y_pred))

from sklearn.metrics import make_scorer, f1_score
scorer = make_scorer(f1_score,  # 性能矩阵或损失函数
                     pos_label=0)  # ?
gs = GridSearchCV(estimator=pipe_svc, param_grid=param_grid, scoring=scorer,
                  cv=10)
gs = gs.fit(X_train, y_train)
print("通过网格搜素后，最好模型的得分:\n", gs.best_score_)
print("通过网格搜索后，最好模型的参数:\n", gs.best_params_)

print("6.5.3-ROC图")
from sklearn.metrics import roc_curve, auc
from scipy import interp  # 一维线性内插法

pipe_lr = make_pipeline(ss, pca, LogisticRegression(random_state=1, C=100.))
X_train2 = X_train[:, [4, 14]]  # 为什么取4-14
cv = list(StratifiedKFold(n_splits=3, random_state=1).split(X_train, y_train))
fig = plt.figure(figsize=(7, 5))
mean_tpr = .0
mean_fpr = np.linspace(0, 1, 100)
all_tpr = []

# cv = [((113),(57)),((113),(57)),((113),(57))]
for i, (train, test) in enumerate(cv):
    probas = pipe_lr.fit(X_train2[train],  # probas.shape = (56,2)
                         y_train[train]).predict_proba(X_train2[test])
    # roc_curve(y_true真实标签, scores多种概率估计值, pos_label积极标签)
    fpr, tpr, thresholds = roc_curve(y_train[test], probas[:, 1], pos_label=1)
    mean_tpr += interp(mean_fpr, fpr, tpr)  # X1,X,Y
    mean_tpr[0] = .0
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label="ROC 折 %d (面积= %.2f)" % (i+1, roc_auc))

plt.plot([0, 1], [0, 1], linestyle="--", color=(.6, .6, .6), label="随机猜测")

mean_tpr /= len(cv)
mean_tpr[-1] = 1.0
mean_auc = auc(mean_fpr, mean_tpr)
plt.plot(mean_fpr, mean_tpr, "k--",
         label="mean ROC (area = %.2f)" % mean_auc, lw=2)
plt.plot([0, 0, 1], [0, 1, 1], linestyle=":", color="black",
         label="Prefect Performance")
plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend(loc="best")
plt.show()
