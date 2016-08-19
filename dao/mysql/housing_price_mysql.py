#-*- coding:utf-8 -*-
'''
Author: TianRan
Date: 8/14/16
Version:
'''
import logging
from db_helper import houisng_price_db_connection,MySQLHelper

class HousingPriceMysqlDao(object):
    '''
    The dao layer for houisng price in Mysql
    '''
    def __init__(self,table_name):
        '''
        :param table_name:
        '''
        self.logger = logging.getLogger(type(self).__name__)
        self._mysql_helper = MySQLHelper(houisng_price_db_connection) # get the db connection for housing price
        self._table_name = table_name

    def insert_one(self,date_time,city,area,type,value):
        '''
        Inser one record into mysql
        :param date_time: datetime type,
        :param city: str type, like 北京
        :param area: str type, like  朝阳
        :param type: str type, like 链家
        :param value: float type, like 19230.00
        :return:
        '''
        # Insert sql, format the table_name
        sql = "INSERT INTO {table_name} (date_time,type,city,area,value) VALUES " \
              "(%(date_time)s,%(type)s,%(city)s,%(area)s,%(value)s);".format(table_name = self._table_name)
        try:
            self._mysql_helper.excute(sql,date_time=date_time,city=city,
                                      area=area,type=type,value=value)
        except Exception as e:
            self.logger.exception(e)



if __name__ == '__main__':
    from utils import log_format,PROJECT_DIR
    log_format(PROJECT_DIR + '/logs/test')
    housing_price_dao = HousingPriceMysqlDao('housing_price')
    housing_price_dao.insert_one('2016-07-12','北京','朝阳','链家','19232.2')