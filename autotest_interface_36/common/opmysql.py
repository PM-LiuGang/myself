# -*- coding: utf-8 -*-
#__author__ = 'PM_LiuGang'
#review 190926
import logging, pymysql
import sys
import config

sys.path.append(r'C:\Users\admin\autotest_interface_36\public')


class OperationDbInterface(object):
    #  初始化数据库连接
    def __init__(self,
                 host_db='127.0.0.1',
                 user_db='root',
                 passwd_db='123456',
                 name_db='test_interface',
                 port_db=3306,
                 link_type=0):
        try:
            if link_type == 0:
                self.conn = pymysql.connect(host=host_db,
                                            user=user_db,
                                            passwd=passwd_db,
                                            db=name_db,
                                            port=port_db,
                                            charset='utf8',
                                            cursorclass=pymysql.cursors.DictCursor)
            else:
                self.conn = pymysql.connect(host=host_db,
                                            user=user_db,
                                            passwd=passwd_db,
                                            db=name_db,
                                            port=port_db,
                                            charset='utf8')
            self.cur = self.conn.cursor()
        except pymysql.Error as e:
            print('创建数据库失败 | from Mysql Error %d: %s' % (e.args[0], e.args[1]))
            logging.basicConfig(filename = config.src_path + '/log/syserror.log',
                                level = logging.DEBUG,
                                format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)



    #  定义单条数据的操作、删除、更新操作 
    def op_sql(self, condition):
        try:
            self.cur.execute(condition)
            self.conn.commit()
            result = {'code': '0000', 'message':'执行通用操作成功', 'data':[]}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {'code': '9999', 'message': '执行通过操作异常', 'data':[]}
            print('数据库错误|op_sql %d: %s' % (e.args[0], e.args[1]))
            logging.basicConfig(filename = config.src_path + '/log/syserror.log', level = logging.DEBUG, format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)     
        return result       
    
                                                          
    #  查询表中单条数据
    def select_one(self, condition):
        try:
            rows_affect = self.cur.execute(condition)
            if rows_affect > 0:
                results = self.cur.fetchone()
                result = {'code': '0000', 'message':'执行单条查询操作成功', 'data':results}
            else:
                result = {'code': '0000', 'message':'执行单条查询操作成功', 'data':[]}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {'code': '9999', 'message':'执行单条查询异常', 'data':[]}
            print('数据库错误|select_one %d: %s' % (e.args[0], e.args[1]))
            logging.basicConfig(filename = config.src_path + '/log/syserror.log', level = logging.DEBUG, format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)     
        return result
    

    #  查询表中多条数据
    def select_all(self, condition):
        try:
            rows_affect = self.cur.execute(condition)
            if rows_affect > 0:
                self.cur.scroll(0, mode='absolute')
                results = self.cur.fetchall()
                result = {'code': '0000', 'message':'执行批量查询操作成功', 'data':[results]}
            else:
                result = {'code': '0000', 'message':'执行批量查询操作成功', 'data':[]}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {'code': '9999', 'message':'执行批量查询异常', 'data':[]}
            print('数据库错误|select_one %d: %s' % (e.args[0], e.args[1]))
            logging.basicConfig(filename = config.src_path + '/log/syserror.log', level = logging.DEBUG, format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)     
        return result
    
    
    #  插入数据操作
    def insert_data(self, condition, params):
        try:
            results = self.cur.executemany(condition, params)
            self.conn.commit()
            result = {'code': '9999', 'message': '执行批量查询操作成功', 'data':results}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {'code': '9999', 'message': '执行批量插入异常', 'data':[]}
            print('数据库错误|insert_more %d: %s' % (e.args[0], e.args[1]))
            logging.basicConfig(filename = config.src_path + '/log/syserror.log', level = logging.DEBUG, format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)     
        return result
    
    
    #  关闭数据库
    def __del__(self):
        if self.cur != None:
            self.cur.close()
        if self.conn != None:
            self.conn.close()
    
if __name__ == '__main__':
    test= OperationDbInterface()
    result_self_all = test.select_all('select * from config_total')
    result_self_one = test.select_one('select * from config_total WHERE id=1')
    result_op_sql = test.op_sql("update config_total set value_config='test' WHERE id=1")
    result = test.insert_data("insert into config_total (key_config, value_config, description, status) values (%s, %s, %s, %s)", [('mytese1', 'mytest11','我的测试1',1),('mytese2', 'mytest22','我的测试2',0)])
    print(result_self_all['data'], result_self_all['message'])
    print(result_self_one['data'], result_self_one['message'])
    print(result_op_sql['data'], result_op_sql['message'])
    print(result['data'], result['message'])


    
    
    

    

