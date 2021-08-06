from pymysql import cursors, connect

conn = connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    db='guest',
    charset='utf8mb4',
    cursorclass=cursors.DictCursor
)


try:
    with conn.cursor() as cursors:
        sql = 'INSERT INTO sign_guest (realname, phone, email, \
        sign, event_id, create_time) VALUES ("tom", 18800110002, "tom@mail.com", 0, 1, NOW()):'
        cursors.execute(sql)
    conn.commit()

    with conn.cursor() as cursors:
        sql = 'SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s'
        cursors.execute(sql, ('18800110002',))
        result = cursors.fetchone()
        print(result)
finally:
    conn.close()