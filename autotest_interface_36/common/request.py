# -*- coding: utf-8 -*-
'''
封装HTTP请求操作
http_request是主方法，直接供外部调用
__http_get, __http_post是实际底层分类调用的方法
'''
# review 190926

import requests, logging, sys
sys.path.append('../')
from common import opmysql
from public import config

class RequestInterface(object):
    def __new_param(self, param):
        try:
            if isinstance(param, str) and param.startswith('{'):
                new_param = eval(param)
            elif param == None:
                new_param = ''
            else:
                new_param = param
        except Exception as error:
            new_param = ''
            logging.basicConfig(filename = config.src_path + '/log/syserror.log', 
                                level = logging.DEBUG, 
                                format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(error)     
        return new_param
    
    def __http_post(self, interface_url, headerdata, interface_param):
        try:
            if interface_url != '':
                temp_interface_param = self.__new_param(interface_param)
                response = requests.post(url=interface_url,
                                         headers=headerdata,
                                         data=temp_interface_param,
                                         verify=False,
                                         timeout=10)
                if response.status_code == 200:
#                    durtime = (response.elapsed.microseconds) / 1000
                    result = {'code': '0000', 'message':'Success!', 'data':response.text}
                else:
                    result = {'code': '2004', 'message':'Interface State Error!', 'data':[]}
            elif interface_url == '':
                result = {'code': '2002', 'message':'Interface Address Param is None', 'data':[]}
            else:
                result = {'code': '2003', 'message':'Interface Address Error', 'data':[]}
        except Exception as error:
            result = {'code': '9999', 'message':'Systerm Abnormal', 'data':[]}
            logging.basicConfig(filename = config.src_path + '/log/syserror.log', 
                                level = logging.DEBUG, 
                                format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(error)     
        return result

      
    def __http_get(self, interface_url, headerdata, interface_param):
        try:
            if interface_url != '':
                temp_interface_param = self.__new_param(interface_param)
                if interface_url.endswith('?'):
                    requrl = interface_url + temp_interface_param
                else:
                    requrl = interface_url + '?' + temp_interface_param
                response = requests.get(url=requrl)
                print('HTTP GET RESULT ---> %s' % response)
                if response.status_code == 200:
#                    durtime = (response.elapsed.microseconds) / 1000
                    result = {'code': '0000', 'message':'Success!', 'data':response.text}
                else:
                    result = {'code': '3004', 'message':'Interface State Error!', 'data':[]}
            elif interface_url == '':
                result = {'code': '3002', 'message':'Interface Address Param is None', 'data':[]}
            else:
                result = {'code': '3003', 'message':'Interface Address Error', 'data':[]}
        except Exception as error:
            result = {'code': '9999', 'message':'Systerm Abnormal', 'data':[]}
            logging.basicConfig(filename = config.src_path + '/log/syserror.log', 
                                level = logging.DEBUG, 
                                format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(error)     
        return result
    
    def http_request(self, interface_url, headerdata, interface_param, request_type):
        try:
            if request_type == 'get' or request_type == 'GET':
                result = self.__http_get(interface_url, headerdata, interface_param)
            elif request_type == 'post' or request_type == 'POST':
                result = self.__http_post(interface_url, headerdata, interface_param)
            else:
                result = {'code':'1000', 'message':'Request Type Error. Type is Neighter GET nor POST.', 'data': request_type}
        except Exception as error:
            result = {'code': '9999', 'message':'Systerm Abnormal', 'data':[]}
            logging.basicConfig(filename = config.src_path + '/log/syserror.log', 
                                level = logging.DEBUG, 
                                format='%(asctime)s %(filename)s  [line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(error)     
        return result

if __name__ == '__main__':
    test_interface = RequestInterface()
    test_db = opmysql.OperationDbInterface(host_db='127.0.0.1',
                                           user_db='root',
                                           passwd_db='123456',
                                           name_db='test_interface',
                                           port_db=3306, link_type=0)
    sen_sql = 'select exe_mode, url_interface, header_interface, params_interface from case_interface where id=1'
    params_interface = test_db.select_one(sen_sql)
    if params_interface['code'] == '0000':
        url_interface=params_interface['data']['url_interface']
        temp=params_interface['data']['header_interface']
        headerdata=eval(params_interface['data']['header_interface'])#unicode转换成字典
        param_interface=params_interface['data']['params_interface']
        type_interface=params_interface['data']['exe_mode']
        if url_interface !='' and headerdata !='' and param_interface !='' and type_interface !='':
            result=test_interface.http_request(interface_url=url_interface,
                                               headerdata=headerdata,
                                               interface_param=param_interface,
                                               request_type=type_interface)
            if result['code']=='0000':
                result_resp=result['data']
                test_db.op_sql("UPDATE case_interface SET result_interface='%s' WHERE id=1" % result_resp)
                print("处理http请求成功，返回数据是：%s" % result_resp)
            else:
                print("处理http请求失败")
        else:
            print("测试用例数据中有空值")
    else:
        print("获取接口测试用例数据失败")        
