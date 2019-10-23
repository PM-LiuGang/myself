# -*-coding: utf8-*-

import requests
from bs4 import BeautifulSoup
import csv


def get_html():
    url = 'https://bj.58.com/wangjing/pinpaigongyu/?minprice=2000_3000'
    csv_file = open('renting.csv', 'w', encoding='utf_8_sig', newline='')
    writer = csv.writer(csv_file, dialect='excel')
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = BeautifulSoup(response.text, 'html.parser')
    # <ul class='list'>
    #   <li class='' logr='' ...
    house_list = html.select('.list > li')
    print('正在下载网页')
    write_file(house_list, writer)
    csv_file.close()


def write_file(house_list, writer):
    for house in house_list:
        if house != None:
            house_title = house.find('div', class_='img').img.get('alt')
            house_info_list = house_title.split()
            house_location = house_info_list[1]
            house_url = house.select('a')[0]['href']
            writer.writerow([house_title, house_location, house_url])


if __name__ == '__main__':
    get_html()