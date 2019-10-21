# coding:utf-8
# 通过socket编程实现的web服务
import socket
import errno
import threading
import time


eol1 = b'\n\n'
eol2 = b'\n\r\n'
boby = '''hello world! 
<h1> from the5fire 《Django 企业开发实战》</h1>  
- from {thread_name}
'''

response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sun, 27 may 2018 01:01:01 GMT',
    'Content-Type: text/html; charset=utf-8',
    'Content-Length {length}\r\n',
    boby
]

response = '\r\n'.join(response_params)

def handle_connection(conn, addr):

    print('conn:', conn)
    print('addr:', addr)
    time.sleep(3)
    request = b''
    while eol1 not in request and eol2 not in request:
        request += conn.recv(1024)  # 非阻塞模式会报错, 修改了main中的except进行适配
    print('recv request--->', request)
    current_thread = threading.currentThread()
    content_length = len(boby.format(thread_name=current_thread.name).encode())
    print('current_thread.namerequest--->', current_thread.name)
    conn.send(response.format(thread_name=current_thread.name,
                              length=content_length).encode())
    conn.close()

def main():
    # WEB Server
    # AF_INET用于服务器与服务器之间的网络通信
    # SOCK_STREAM用于基于TCP的流式socket通信
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # SO_REUSEADDR 设置端口可复用，保证我们每次按ctrl+c组合键之后，快速重启
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(10)  # 设置backlog-socket连接最大排队(挂起)数量
    print('Click URL--->', 'http://127.0.0.1:8000')
    serversocket.setblocking(False)  # 设置成非阻塞模式报错啊

    try:
        i = 0
        while True:
            try:
            #  addr 连接客户端的地址
            #  conn是新的套接字对象，可以用来接收和发送数据
                conn, address = serversocket.accept()  # 进入循环，不断接受客户端的连接请求
            # except socket.error as e:
            #     if e.args[0] != errno.EAGAIN:
            #         raise
            except BlockingIOError:
                continue
            i += 1
            print('request--->', i)
            t = threading.Thread(target=handle_connection,
                                 args=(conn, address),
                                 name='thread name--->%s' % i)
            t.start()
    finally:
        serversocket.close()


if __name__ == '__main__':
    main()