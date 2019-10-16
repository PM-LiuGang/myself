# -*- coding: utf-8 -*-

import re
import requests
import os
import json

def get_station():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9114'
    response = requests.get(url, verify=True)
    stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    stations = dict(stations)
    stations = str(stations)
    write(stations, 'stations.txt')

def write(stations, file_name):
    file = open(file_name, 'w', encoding='utf_8_sig')
    file.write(stations)
    file.close()

def read(file_name):
    file = open(file_name, 'r', encoding='utf_8_sig')
    data = file.readline()
    file.close()
    return data

def is_stations(file_name):
    is_stations = os.path.exists(file_name)
    return is_stations

def get_selling_time():
    url = 'https://www.12306.cn/index/script/core/common/qss_v10042.js'
    response = requests.get(url, verify=True)
    json_str = re.findall('{[^}]+}', response.text)
    time_js = json.loads(json_str[0])
    write(str(time_js), 'time.txt')

