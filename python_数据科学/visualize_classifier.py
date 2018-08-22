improt numpy as np

def visualize_classifier(model,x,y,ax=None,cmap='rainbow'):
    '''辅助函数，对分类器的结果进行可视化'''
    '''画出训数据'''
    ax = ax or plt.gca()
    ax.scatter(x[:,0],x[:,1],c=y,s=30,cmap=cmap,clim=(y.min(),y.max()),zorder=3)
    ax.axis('tight')
    ax.axis('off')
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    '''用评估器拟合数据'''
    model.fit(x,y)
    xx,yy = np.meshgrid(np.linspace(*xlim,num=200),np.linspace(*ylim,num=200))
    z = model.predict(np.c_[xx.ravel(),yy.ravel()]).reshape(xx.shape)
    '''为结果生成彩色图'''
    n_classes = len(np.unique(y))
    contours = ax.contourf(xx,yy,z,alpha=0.3,levels=np.arange(n_classes+1) - 0.5,cmap=cmap,clim=(y.min(),y.max()),zorder=1)
    ax.set(xlim=xlim,ylim=ylim)
    

