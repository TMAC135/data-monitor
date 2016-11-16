# -*- coding:utf-8 -*-
'''
Author: TianRan
Date: 8/14/16
Version:

Update:

November 16, 2016 by QI MO
add get_city_housing_price
'''
import logging
from db_helper import houisng_price_db_connection, MySQLHelper


class HousingPriceMysqlDao(object):
    '''
    The dao layer for houisng price in Mysql
    '''

    def __init__(self, table_name):
        '''
        :param table_name:
        '''
        self.logger = logging.getLogger(type(self).__name__)
        self._mysql_helper = MySQLHelper(houisng_price_db_connection)  # get the db connection for housing price
        self._table_name = table_name

    def get_city_housing_price(self,date_end,date_begin,city_name):
        """
        get the sql result by date_time and city_name
        :param date_end:
        :param date_begin:
        :param city_name:
        :return:
        """

        sql = "SELECT date_time, city, avg(value) FROM {table_name} " \
              "WHERE date_time<=%(date_end)s AND date_time>=%(date_begin)s " \
              "AND city=%(city_name)s GROUP BY date_time, city ;".format(table_name=self._table_name)
        result = self._mysql_helper.query(sql,date_end=date_end, date_begin=date_begin,city_name=city_name)
        return result

    def insert_update_one(self, date_time, city, area, type, value):
        '''
        Insert or update one query into mysql,if the contend exist in database,
            do update operation
        :param date_time: datetime type,
        :param city: str type, like 北京
        :param area: str type, like  朝阳
        :param type: str type, like 链家
        :param value: float type, like 19230.00
        :return: True or False, representing whether we succ update or insert.
        '''
        if self.exist_in_database(date_time, city, area, type):  # update sql
            sql = "UPDATE {table_name} " \
                  "SET value=%(value)s " \
                  "WHERE date_time=%(date_time)s AND city=%(city)s " \
                  "AND area=%(area)s AND type=%(type)s;".format(table_name=self._table_name)
        else:  # insert sql
            sql = "INSERT INTO {table_name} (date_time,type,city,area,value) VALUES " \
                  "(%(date_time)s,%(type)s,%(city)s,%(area)s,%(value)s);".format(table_name=self._table_name)
        try:
            self._mysql_helper.excute(sql, date_time=date_time, city=city,type=type,
                                      area=area, value=value)
            return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def delete_one(self, date_time, city, area, type):
        '''
        Delete one record from mysql
        :param date_time: datetime type,
        :param city: str type, like 北京
        :param area: str type, like  朝阳
        :param type: str type, like 链家
        :return:
        '''
        sql = "DELETE FROM {table_name} " \
              "WHERE date_time=%(date_time)s AND " \
              "city=%(city)s AND type=%(type)s AND area=%(area)s;".format(table_name=self._table_name)
        try:
            self._mysql_helper.excute(sql, date_time=date_time, type=type,
                                      city=city, area=area)
        except Exception as e:
            self.logger.exception(e)

    def exist_in_database(self, date_time, city, area, type):
        '''
        judge whether the query from given fields exist in database
        :param date_time: datetime type,
        :param city: str type, like 北京
        :param area: str type, like  朝阳
        :param type: str type, like 链家
        :return: True or False
        '''
        sql = "SELECT value from {table_name} " \
              "WHERE date_time=%(date_time)s AND " \
              "city=%(city)s AND type=%(type)s AND area=%(area)s;".format(table_name=self._table_name)
        try:
            ret_list = self._mysql_helper.query(sql, date_time=date_time, type=type,
                                                city=city, area=area)
            return True if len(ret_list) is 1 else False
        except Exception as e:
            self.logger.exception(e)
            return False




if __name__ == '__main__':
    from utils import log_format, PROJECT_DIR

    log_format(PROJECT_DIR + '/logs/test')
    housing_price_dao = HousingPriceMysqlDao('housing_price')
    housing_price_dao.insert_update_one('2016-07-12', 'Beijing', '朝阳', '链家', 2222.2323)
    housing_price_dao.insert_update_one('2016-07-12', 'Beijing', '海淀', '链家', 222233)
    # print housing_price_dao.exist_in_database('2016-08-11','Beijing','朝阳','链家')
    # housing_price_dao.delete_one('2016-07-12','北京','朝阳','链家')
