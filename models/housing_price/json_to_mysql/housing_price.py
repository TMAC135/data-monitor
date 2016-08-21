# -*- coding:utf-8 -*-
'''
Author: TianRan
Date: 8/14/16
Version:
    08/18:
        1: parse the housing pirce of json format to mysql database
        2: add the start time and end time for json path file
        3: add more log logistic when updating the data to databse

'''
import logging
import json
import arrow as ar
from dao.mysql.housing_price_mysql import *
from datetime import timedelta, date
import os


class UpdateHousingPriceToMysql(object):
    '''
    Put the houisng price to the MySQL database, to modify the
    config of the database, go to the defaults.cfg under config/databases
    '''

    def __init__(self, table_name, start_time, end_time):
        '''
        :param table_name: table name of mysql datebase
        :param start_time: start_time of the json,str type,like '2016-06-01'
        :param end_time: end_time of the json,str type,like '2016-07-01'
        '''
        self.logger = logging.getLogger(type(self).__name__)
        self._mysql_dao = HousingPriceMysqlDao(table_name)
        try:
            self._start_time = ar.get(start_time).naive.date()
            self._end_time = ar.get(end_time).naive.date()
        except Exception as e:
            self.logger.exception(e)

    def update(self, json_dir):
        '''
        update the contend of the json to mysql from start_time
            to end_time, if the json path is not existing,just
            jump this file
        :param json_dir: the root dir of the json data
        :return:
        '''
        iter_time = self._start_time
        while iter_time <= self._end_time:
            json_path = "{json_dir}/{date}_lianjia_housing.json".format(json_dir=json_dir,
                                                                        date=iter_time)
            if not os.path.exists(json_path):
                iter_time += timedelta(days=1)
                continue
            try:
                pricing_dict_one_day = self._get_json_contend(json_path)
                for city, area_dict in pricing_dict_one_day.items():
                    for area, value in area_dict.items():
                        if not self._mysql_dao.insert_update_one(iter_time, city, area, '链家', value):
                            self.logger.info("Fail to update,city:{city},area:{area},value:{value}".format(city=city,
                                                area=area,value=value))
                        # print city,area,value
                self.logger.info('Finishing update the lianjia housing price for {date_time}'
                                 ''.format(date_time=iter_time))
            except Exception:
                self.logger.error('Fail to update the lianjia housing price for {date_time}'
                                  ''.format(date_time=iter_time))
            iter_time += timedelta(days=1)

    def _get_json_contend(self, json_path):
        '''
        Parse the json file and get the contend as dict
        :return: return the dict of the json file
        '''
        try:
            with open(json_path, 'r') as f:
                housing_price_json = json.load(f)
                return housing_price_json
        except Exception as e:
            self.logger.exception(e)


if __name__ == '__main__':
    from utils import PROJECT_DIR
    from utils import log_format

    log_format(PROJECT_DIR + 'logs/test')
    json_dir = "{project_dir}/data/json/crawler/housing".format(project_dir=PROJECT_DIR)
    update_to_mysql = UpdateHousingPriceToMysql('housing_price', '2016-08-11', '2016-08-16')
    update_to_mysql.update(json_dir)
