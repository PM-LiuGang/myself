# coding:utf8

import time
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        t1 = time.time()
        self._func()
        t2 = time.time()
        print('Spend is {}'.format(t2 - t1))

@Foo  # bar = Foo(bar)
def bar():
    print('bar...')
    time.sleep(2)

if __name__ == '__main__':
    bar()