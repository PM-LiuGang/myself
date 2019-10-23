#coding:utf8

import time

def time_logger(flag=True):
    def showtime(func):
        def wrapper(a, b):
            t1 = time.time()
            func(a, b)
            t2 = time.time()
            print('spend is {}'.format(t2 - t1))
            if flag:
                print('Save Log.')
            else:
                print('Not Save Log.')
        return wrapper
    return showtime

@time_logger(False) # showtime, add = showtime(add)
def add(a, b):
    print(a + b)
    time.sleep(1)

if __name__ == '__main__':
    add(3,4)