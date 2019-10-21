# coding:utf8

import time

def showtime(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print('func cost time is {}'.format(t2 - t1))
    return wrapper

@showtime
def foo():
    print('I will be sleep in three seconds')
    time.sleep(3)

# foo = showtime(foo)
# foo()

if __name__ == '__main__':
    foo()