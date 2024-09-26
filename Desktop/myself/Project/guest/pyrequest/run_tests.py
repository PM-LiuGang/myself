import sys, time
sys.path.append(r'C:\Users\admin\guest\pyrequest\db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data

test_dir = r'C:\Users\admin\guest\pyrequest\interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == '__main__':
    test_data.init_data()
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filename = now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='Guest Manage System Interface Test Report',
                            description='Implementation Example with:')
    runner.run(discover)
    fp.close()
