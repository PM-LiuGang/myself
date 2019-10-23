# coding:utf8

import time

def showtime(func):
    def wrapper(a, b):
        t1 = time.time()
        func(a, b)
        t2 = time.time()
        print('The time is {}'.format(t2 - t1))
    return wrapper

@showtime
def add(a, b):
    print(a + b)
    time.sleep(1)

if __name__ == '__main__':
    add(5,5)