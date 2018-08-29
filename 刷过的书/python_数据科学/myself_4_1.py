# IPython log file

get_ipython().run_line_magic('cd', 'c')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'myself_x/')
get_ipython().run_line_magic('ls', '')
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('classic')
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,100)
#100个0-10的数，平均分布，间隔
plt.plot(x,np.sin(x))
#[Out]# [<matplotlib.lines.Line2D at 0x1f2a55aa160>]
plt.plot(x,np.cos(x))
#[Out]# [<matplotlib.lines.Line2D at 0x1f2a5484cf8>]
plt.show()
get_ipython().run_line_magic('pylab', '')
from IPython.display import Image
get_ipython().run_line_magic('ls', '')
Image('Figure_4_1.png')#不显示图片，还是用plt show（）
#[Out]# <IPython.core.display.Image object>
plt.show()
plt.show()
fig.canvas.get_supported_filetypes()
############
plt.figure()
#[Out]# <matplotlib.figure.Figure at 0x1f2abc5d438>
plt.subplot(2,1,1)
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x1f2abc8bcc0>
plt.plot(x,np.sin(x))
#[Out]# [<matplotlib.lines.Line2D at 0x1f2ac469f28>]
plt.subplot(2,1,2)
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x1f2aac35470>
plt.plot(x,np.cos(x))
#[Out]# [<matplotlib.lines.Line2D at 0x1f2abb70c50>]
plt.gca()#？
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x1f2aac35470>
plt.gcf()#？
#[Out]# <matplotlib.figure.Figure at 0x1f2abc5d438>
###########################
fig,ax = plt.subplots(2)
ax[0].plot(x,np.sin(x))
#[Out]# [<matplotlib.lines.Line2D at 0x1f2acc0e048>]
ax[1].plot(x,np.cos(x))
#[Out]# [<matplotlib.lines.Line2D at 0x1f2acbe1710>]
pylab
#[Out]# <module 'matplotlib.pylab' from 'C:\\Users\\Administrator\\Anaconda3\\lib\\site-packages\\matplotlib\\pylab.py'>
get_ipython().run_line_magic('pylab', '')
get_ipython().run_line_magic('pylab', '-off')
plt.style.use('seaborn-whitegrid')
get_ipython().run_line_magic('pinfo', 'plt.style.use')
####################
import numpy as np
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0,10,1000)
ax.plot(x,np.sin(x))
#[Out]# [<matplotlib.lines.Line2D at 0x1f2acb840b8>]
plt.plot(x,np.sin(x))
#[Out]# [<matplotlib.lines.Line2D at 0x1f2acb63828>]
plt.plot(x,np.cos(x))
#[Out]# [<matplotlib.lines.Line2D at 0x1f2acb9b898>]
get_ipython().run_line_magic('logstop', '')
