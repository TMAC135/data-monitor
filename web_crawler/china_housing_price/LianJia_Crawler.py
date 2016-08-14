# -*- coding=utf-8 -*-
'''
Author: TianRan
Date: 7/22/16
Version:
07/22:
    1: only consider the Beijing housing at this time
    2: consider different area in Beijing, like HaiDian, ChaoYang, etc

07/23:
    1: add the configurations for area and web mapping for different cities in china,

08/03:
    1: add the log
08/09:
    1: modify the url for Suzhou and Shanghai for special after debuging
    2: save the result to the json file
'''
import requests
from bs4 import BeautifulSoup
import re
from collections import defaultdict
import logging
import json

# functions from util package
from utils.path_util import *
from utils.log_util import log_format

# Beijing area map for different url in lianjia website
from lianjia_confg import LIANJIA_MAP

# set the format for the log
log_format(PROJECT_DIR + '/logs/crawler')


class LianJiaCrawler(object):
    '''
    crawling the housing price for different areas in china
    '''

    def __init__(self, url, area_map):
        '''

        :param url: the root website: 'http://bj.fang.lianjia.com'

        :field
            _url_dict: url for different area, key is area in Beijing(str),
                      value is list of url in this area
            _html_dict: html for different area, key is area in Beijing(str),
                       value is list of url in this area
            _price_dict: average price for different area, key is area in Beijing(str),
                       value is list of url in this area

        '''
        if url[7:9] == 'sh' or url[7:9] == 'su': # special url for Shanghai and Suzhou
            self._url = url + '/list'
        else:
            self._url = url + '/loupan'  # the price information is with this suffix
        self._url_dict = defaultdict(list)
        self._html_dict = defaultdict(list)
        self._price_dict = {}

        self._area_map = area_map

        self.logger = logging.getLogger(type(self).__name__)

    def _generate_url_dict(self):
        '''
        generate urls for different area, store them into the _url_dict,
        parse all
        :return:
        '''
        for area, url_name in self._area_map.items():
            try:
                url_root_area = self._url + '/' + url_name  # root url for this area
                response = requests.get(url_root_area)
            except Exception as e:
                self.logger.exception(e)

            if response.status_code != 200:
                # log the info
                pass
            else:
                soup = BeautifulSoup(response.text, 'lxml')
                # get the number of pages for this area

                # print soup.find('div',class_='page-box house-lst-page-box')
                page_block = soup.find('div', class_='page-box house-lst-page-box')
                if page_block is None:
                    continue
                else:
                    dict_tmp = eval(page_block.get('page-data', ''))
                    page_num = dict_tmp.get('totalPage', 0)

                # append the url
                for page_index in range(1, page_num + 1):
                    self._url_dict[area].append(url_root_area + '/pg{}'.format(page_index))

    def _get_html_dict(self):
        '''
        parse the url in url_dict and store them in html_dict.
        :return:

        :notice:
            call _generate_url_dict() first before this function
        '''
        for area, url_list in self._url_dict.items():
            if len(url_list) == 0:
                raise ValueError('please generate url dict first')
            for url in url_list:
                try:
                    response = requests.get(url)
                except Exception as e:
                    # log
                    # print traceback.print_exc()
                    self.logger.exception(e)
                if response.status_code == 200:
                    self._html_dict[area].append(response.text)
                else:
                    # log
                    pass

    def get_price_dict(self):
        '''
        generate the average prices for different areas
        :return:

        :notice:
            1: call _generate_url_dict() and _get_html_dict() first
            2: I only consider the average price here, thus the price calculated is based on
                average, eg, 20000 RMB/m^2
        '''
        # generate the url and html first
        self._generate_url_dict()
        self._get_html_dict()

        for area, html_list in self._html_dict.items():
            total_price = 0
            succ_count = 0

            # get the price in the html,
            for html in html_list:
                count_tmp, price_tmp = self._cal_average_price_from_html(html)
                succ_count += count_tmp
                total_price += price_tmp

            if succ_count == 0:
                # log
                pass
            else:
                average_price = round(total_price * 1.0 / succ_count, 0)
                self._price_dict[area] = average_price

    def _cal_average_price_from_html(self, html):
        '''
        parse the html and return the count and price for this html
        :param html:
        :return:
            succ_count: the succ count for the price for this html
            total_price: total price for the counts for this html
        '''
        soup = BeautifulSoup(html, 'lxml')

        div_list = soup.find_all('div', class_='col-2')
        succ_count = 0
        total_price = 0
        for index in range(len(div_list)):
            # print div_list[index].text.replace('\n','')
            each_line = div_list[index].text.replace('\n', '')
            each_line_no_space = re.sub('\s*', '', each_line)
            # print each_line_no_space
            # print each_line_no_space[:3]

            # print each_line_no_space[:2]
            # print each_line_no_space[:2] == u'场均'
            if each_line_no_space[:2] == u'均价':
                try:
                    # extract the price for every line and add them to the total price
                    price = re.findall('\d+', each_line_no_space)
                    if len(price) is not 0:
                        total_price += float(price[0])
                        succ_count += 1
                except Exception as e:
                    self.logger.exception(e)
        return succ_count, total_price


if __name__ == '__main__':
    # lianjia_root_site = 'http://bj.fang.lianjia.com'
    # lianjia = LianJiaCrawler(lianjia_root_site)


    # debug code
    # print lianjia._url_dict
    # print lianjia._html_dict
    # print lianjia._html_dict[u'HuaiRou'][0]
    # lianjia._cal_average_price_from_html(lianjia._html_dict[u'HuaiRou'][0])
    # print lianjia._price_dict

    from datetime import date
    from utils.file_utils import ensure_dir
    ensure_dir(PROJECT_DIR + '/data/json/crawler/housing')
    json_out_path = PROJECT_DIR + '/data/json/crawler/housing/{0}_lianjia_housing.json'.format(str(date.today()))

    json_dict = {}
    for city, confg in LIANJIA_MAP.items():
        lianjia = LianJiaCrawler(confg['website'], confg['area_map'])
        lianjia.get_price_dict()
        # print lianjia._price_dict
        json_dict[city] = lianjia._price_dict


     # save the price to the json file
    with open(json_out_path, 'w') as f:
        json.dump(json_dict,f)




