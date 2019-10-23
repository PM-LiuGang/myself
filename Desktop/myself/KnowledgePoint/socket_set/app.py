# coding:utf-8
# 简单的WSGI Application

'''
def simple_app(environ, start_response):
    status = '200 Ok'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b'Hello world! - by the5fire \n']
'''
'''
class AppClass():
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]

    def __call__(self, environ, start_response):
        # print(environ, start_response)
        start_response(self.status, self.response_headers)
        return [b'Hello AppClass.__call__\n']


application = AppClass()
'''

'''
另一种方式实现WSGI协议,调不通
'''
class AppClassIter(object):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response(self.status, self.response_headers)
        yield b'Hello AppClassIter\n'  # WSGI Server只需要返回一个可迭代的对象

