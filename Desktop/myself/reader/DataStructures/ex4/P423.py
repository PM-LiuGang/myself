# P423

import os

import os

def _find(path, filename):
    if os.path.isdir(path) and path:
        disk_usage(os.path.join(path, filename))
    else:
        print('参数错误，请检查')

def disk_usage(dirpath, dirnames=[], filenames=[]):
    for filename in os.listdir(dirpath):
        if os.path.isdir(os.path.join(dirpath, filename)):
            dirnames = []
            filenames = []
            dirnames.append(filename)
            for filename_1 in os.listdir(os.path.join(dirpath, filename)):
                filenames.append(filename_1)
            print(dirpath, '\n', dirnames, '\n',filenames)
            print('#' * 50)
            dirnames = []
            filenames = []
        else:
            filenames.append(filename)
    print(dirpath, dirnames, filenames)
    print('-' * 50)

if __name__ == '__main__':
    print(disk_usage(r'C:\Users\admin\Desktop\myself\reader\DataStructures'))


