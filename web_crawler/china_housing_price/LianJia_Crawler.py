#-*- coding=utf-8 -*-
'''
Author: TianRan
Date: 7/22/16
Version:
07/22:
    1: only consider the Beijing housing at this time
    2: consider different area in Beijing, like HaiDian, ChaoYang, etc
'''
import requests
from bs4 import BeautifulSoup
import re
from collections import defaultdict
import traceback

# Beijing area map for different url in lianjia website
BEIJING_AREA_MAP = {u'ChaoYang':u'chaoyang',u'ChangPing':u'changping',u'DongCheng':u'dongcheng',
                u'DaXing':u'daxing',u'FangShan':u'fangshan',u'FengTai':u'fengtai',
                u'HaiDian':u'haidian',u'HuaiRou':u'huairou'}

class LianJiaCrawler(object):
    '''
    crawling the housing price for different areas in china
    '''
    def __init__(self,url):
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
        self._url = url + '/loupan' #the price information is with this suffix
        self._url_dict = defaultdict(list)
        self._html_dict = defaultdict(list)
        self._price_dict = defaultdict(list)


    def _generate_url_dict(self):
        '''
        generate urls for different area, store them into the _url_dict,
        parse all the
        :return:
        '''
        for area,url_name in BEIJING_AREA_MAP.items():
            try:
                url_root_area = self._url + '/' + url_name #root url for this area
                response = requests.get(url_root_area)
            except Exception as e:
                print traceback.print_exc()

            if response.status_code != 200:
                # log the info
                pass
            else:
                soup = BeautifulSoup(response.text,'lxml')
                # get the number of pages for this area

                # print soup.find('div',class_='page-box house-lst-page-box')
                page_block = soup.find('div',class_='page-box house-lst-page-box')
                dict_tmp = eval(page_block['page-data'])
                page_num = dict_tmp['totalPage']

                #append the url
                for page_index in range(1,page_num+1):
                    self._url_dict[area].append(url_root_area + '/pg{}'.format(page_index))

    def _get_html_dict(self):
        '''
        parse the url in url_dict and store them in html_dict.
        :return:

        :notice:
            call _generate_url_dict() first before this function
        '''
        for area,url_list in self._url_dict.items():
            if len(url_list) == 0:
                raise ValueError('please generate url dict first')
            for url in url_list:
                try:
                    response = requests.get(url)
                except Exception as e:
                    #log
                    print traceback.print_exc()
                if response.status_code == 200:
                    self._html_dict[area].append(response.text)
                else:
                    #log
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
        for area,html_list in self._html_dict.items():
            total_price = 0
            succ_count = 0

            #get the price in the html,
            for html in html_list:
                pass

            if succ_count == 0:
                # log
                pass
            else:
                self._price_dict[area].append(total_price*1.0/succ_count)



if __name__ == '__main__':
    lianjia_root_site = 'http://bj.fang.lianjia.com'
    lianjia = LianJiaCrawler(lianjia_root_site)

    lianjia._generate_url_dict()
    lianjia._get_html_dict()
    # print lianjia._url_dict
    print lianjia._html_dict