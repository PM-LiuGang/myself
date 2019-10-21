# coding:utf8

def start_response(status, headers):
    #
    set_status(status)
    for k, v in headers:
        set_header(k, v)


def handle_conn(conn):
    #
    app = application(environ, start_response)
    for data in app:
        response += data

    conn.sendall(response)