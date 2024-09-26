from pymysql import connect, cursors
from pymysql import OperationalError

import os
import configparser as cparser

cf = cparser.ConfigParser()
cf.read(r'C:\Users\admin\guest\pyrequest\db_config.ini')

host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
db = cf.get('mysqlconf', 'db_name')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')


class DB:

    def __init__(self):
        try:
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8',  # most bytes 4
                                cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print('Mysql Error %d : %s' % (e.args[0], e.args[1]))

    def clear(self, table_name):
        real_sql = 'delete from' + table_name + ';'
        with self.conn.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;') # 取消外键约束
            cursor.execute(real_sql)
        self.conn.commit()

    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.key())
        value = ','.join(table_data.value())
        # INSERT INTO TABLE_NAME [(COLUMN1, COLUMN2,....)] VALUES ('VALUE1','VALUE2',...)
        real_sql = 'INSERT INTO ' + table_name + '(' + key + ') VALUES (' + value + ")"
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == '__mian__':
    db = DB()
    table_name = 'sign_event'
    data = {
        'id': 2,
        'name': 红米,
        'limit': 1000,
        'status': 1,
        'address': '北京会展中心',
        'start_time': '2016-08-20 12:00:00',
    }
    db.clear(table_name)
    db.insert(table_name)
    db.close()





