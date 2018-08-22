#coding=utf-8
#将不同类型的归类（py,xlsx,txt)
#

import zipfile, os,shutil
#folder=input('请输入需要归类的文件夹')

folder = r'c:\python\50'

for foldername, subfolders, filenames in os.walk(folder):
    print('现在归类的文件夹是 %s...' % (foldername))
    for filename in filenames:
        if filename.endswith('.txt'):
            shutil.copy(os.path.join(foldername,filename),'d:\\txt')
        elif filename.endswith('.xlsx'):
        	shutil.copy(os.path.join(foldername,filename),'d:\\xlsx')
        elif filename.endswith('.py'):
        	shutil.copy(os.path.join(foldername,filename),'d:\\py')
        else:
        	print('不需要归档')

print('Done.')