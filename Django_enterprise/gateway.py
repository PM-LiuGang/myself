# coding:utf8
# 2.2.4 简单的WSGI Application
# WSGI协议分为两部分，
# 其中一部分是WEB Server，它监听在某个端口上接受外部的请求
# 另一部分是WEB Application， WEB Server接受请求之后，会通过WSGI协议规定的方式把数据传递给WEB Application
# 在WEB Application中处理完后，设置对应的状态和Header，之后返回boby部分
# WebServer拿到返回数据之后，再进行http协议的封装，最终返回完整的httpResponse数据
# 运行应用程序的CGI脚本

import os
import sys

from app import AppClassIter

def wsgi_to_bytes(s):
    return s.encode()

def run_with_cgi(AppClassIter):
    environ = dict(os.environ.items())
    # environ并没有以下属性/window下
    environ['wsgi.input'] = sys.stdin.buffer
    environ['wsgi.errors'] = sys.stderr
    environ['wsgi.version'] = (1, 0)
    environ['wsgi.multithread'] = False
    environ['wsgi.multprocess'] = True
    environ['wsgi.run_once'] = True
    # environ.get？
    if environ.get('HTTPS', 'off') in ('on' , '1'): # Return the value for key if key is in the dictionary, else default
        environ['wsgi.url_scheme'] = 'https'
    else:
        environ['wsgi.url_scheme'] = 'http'

    headers_set = []
    headers_sent = []

    def write(data):
        out = sys.stdout.buffer

        if not headers_set:  # [] -> False
            raise AssertionError('write() before start_response()')

        elif not headers_sent:
            # 在输出第一行数据之前，先发送响应头
            status, response_headers = headers_sent[:] = headers_set
            out.write(wsgi_to_bytes('Status: %s\r\n' % status))
            for header in response_headers:
                out.write(wsgi_to_bytes('%s: %s\r\n' % header))
            out.write(wsgi_to_bytes('\r\n'))

        out.write(data)
        out.flush()

    def start_response(status, response_headers, exc_info=None):
        if exc_info:
            try:
                if headers_sent:
                    raise (exc_info[0], exc_info[1], exc_info[2])
            finally:
                exc_info = None
        elif headers_set:
            raise AssertionError('Headers already set!')

        headers_set[ : ] = [status, response_headers]
        return write

    result = AppClassIter(environ, start_response)

    try:
        for data in result:
            if data:
                write(data)
        if not headers_sent:
            write('')
    finally:
        if hasattr(result, 'close'):
            result.close()

if __name__ == '__main__':
    run_with_cgi(AppClassIter)

# 运行脚本gateway.py,应在命令行上能够看到对应的输出
'''
Status: 200 OK
Content-type: text/plain

Hello World！ by the5fire
'''