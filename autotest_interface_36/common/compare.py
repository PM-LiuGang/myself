# -*- coding: utf-8 -*-
'''
定义数据比较方法
compare_param:对外比较的参数类
compare_code:是关键参数值的比较方法
compare_params_complete:参数完整性的比较方法
get_compare_params:获得返回包数据去重后集合的方法
recur_params：递归操作方法，辅助去重
'''

from public import config
from common import opmysql
import json
import logging
import sys

sys.path.append('../')

operation_db = opmysql.OperationDbInterface()


class CompareParam(object):
    def __init__(self, params_interface):
        self.params_interface = params_interface
        self.id_case = params_interface['id']
        self.result_list_response = []
        self.params_to_compare = params_interface['params_to_compare']

    def get_compare_params(self, result_interface):
        try:
            if result_interface.startswith(
                    '{') and isinstance(result_interface, str):
                temp_result_interface = json.loads(result_interface)
                self.result_list_response = temp_result_interface.keys()
                result = {
                    'code': '0000',
                    'message': 'Success',
                    'data': self.result_list_response}
            else:
                result = {
                    'code': '1000',
                    'message': 'Return Packets Format Illegal.'}
        except Exception as error:
            result = {
                'code': '9999',
                'message': 'Handle Abnormal.',
                'data': []}
            operation_db.op_sql(
                'UPDATE case_interface set result_code_compare="%s" where id=%s' %
                (9, self.id_case))
            logging.basicConfig(
                filename=config.src_path + '/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(error)
        finally:
            return result

    def compare_params_complete(self, result_interface):
        try:
            temp_compare_params = self.__recur_params(result_interface)
            if temp_compare_params['code'] == '0000':
                temp_result_list_response = temp_compare_params['data']
                if self.params_to_compare.startswith(
                        '{') and isinstance(self.params_to_compare, str):
                    list_params_to_compare = eval(self.params_to_compare)
                    if set(list_params_to_compare).issubset(
                            set(temp_result_list_response)):
                        result = {
                            'code': '0000',
                            'message': 'Params Integrity Compare Same',
                            'data': []}
                        operation_db.op_sql(
                            'UPDATE case_interface set params_actual="%s", result_params_compare=%s where id="%s"' %
                            (temp_result_list_response, 1, self.id_case))
                    else:
                        result = {
                            'code': '3001',
                            'message': 'Real Result isn"t Except Result.',
                            'data': []}
                        operation_db.op_sql(
                            'UPDATE case_interface set params_actual="%s", result_params_compare=%s where id="%s"' %
                            (temp_result_list_response, 0, self.id_case))
                else:
                    result = {
                        'code': '4001',
                        'message': 'Compare Params Set Error In Case',
                        'data': []}
            else:
                result = {
                    'code': '2001',
                    'message': 'Callable __recur_params method Return Error.',
                    'data': []}
                operation_db.op_sql(
                    'UPDATE case_interface set result_code_compare="%s" where id=%s' %
                    (2, self.id_case))
        except Exception as error:
            result = {
                'code': '9999',
                'message': 'Keyword Params Integrity Compare Abnormal',
                'data': []}
            operation_db.op_sql(
                'UPDATE case_interface set result_code_compare="%s" where id=%s' %
                (9, self.id_case))
            logging.basicConfig(
                filename=config.src_path + '/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(error)
        finally:
            return result

    def __recur_params(self, result_interface):
        try:
            if result_interface.startswith(
                    '{') and isinstance(result_interface, str):
                temp_result_interface = json.loads(result_interface)
                self.__recur_params(temp_result_interface)
            elif isinstance(result_interface, dict):
                for param, value in result_interface.items():
                    self.result_list_response.append(param)
                    if isinstance(value, list):
                        for param in value:
                            self.__recur_params(param)
                    elif isinstance(value, dict):
                        self.__recur_params(value)
                    else:
                        continue
            else:
                pass
        except Exception as error:
            logging.basicConfig(
                filename=config.src_path + '/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(error)
            return {
                'code': '9999',
                'message': 'Handle Data Abnormal',
                'data': []}
        return {'code': '0000', 'message': 'Success',
                'data': list(set(self.result_list_response))}

    def compare_code(self, result_interface):
        try:
            if result_interface.startswith(
                    '{') and isinstance(result_interface, str):
                temp_result_interface = json.loads(result_interface)
                temp_code_to_compare = self.params_interface['code_to_compare']
                if temp_code_to_compare in temp_result_interface.keys():
                    if str(
                            temp_result_interface[temp_code_to_compare]) == str(
                            self.params_interface['code_expect']):
                        result = {
                            'code': '0000',
                            'message': 'KeyWord Param Value Equal.',
                            'data': []}
                        operation_db.op_sql(
                            'UPDATE case_interface set code_actual="%s",result_code_compare=%s where id=%s' %
                            (temp_result_interface[temp_code_to_compare], 1, self.id_case))
                    else:
                        result = {
                            'code': '1002',
                            'message': 'Keyword Param Value Compare Error.',
                            'data': []}
                        operation_db.op_sql(
                            'UPDATE case_interface set code_actual="%s",result_code_compare=%s where id=%s' %
                            (temp_result_interface[temp_code_to_compare], 3, self.id_case))
                else:
                    result = {
                        'code': '1001',
                        'message': 'Return Packets Hasn"t Keyword Params',
                        'data': []}
                    operation_db.op_sql(
                        'UPDATE case_interface set result_code_compare="%s" where id=%s' %
                        (2, self.id_case))
            else:
                result = {
                    'code': '1000',
                    'message': 'Return Packets Format Illegal',
                    'data': []}
                operation_db.op_sql(
                    'UPDATE case_interface set result_code_compare="%s" where id=%s' %
                    (4, self.id_case))
        except Exception as error:
            result = {
                'code': '9999',
                'message': 'Keyword Params Values Compare Abnormal',
                'data': []}
            operation_db.op_sql(
                'UPDATE case_interface set result_code_compare="%s" where id=%s' %
                (9, self.id_case))
            logging.basicConfig(
                filename=config.src_path + '/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(error)
        finally:
            return result


if __name__ == '__main__':
    sen_sql = 'select * from case_interface where id=1'
    params_interface = operation_db.select_one(sen_sql)
    result_interface = params_interface['data']['result_interface']
    test_compare_param = CompareParam(params_interface['data'])
    result_compare_code = test_compare_param.compare_code(result_interface)
    print(result_compare_code)
    result_compare_params_complete = test_compare_param.compare_params_complete(
        result_interface)
    print(result_compare_params_complete)
