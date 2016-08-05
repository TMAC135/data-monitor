# -*- coding:utf-8 -*-
'''
Author: Ran Tian
Created: 16/8/5
Version: 1.0
Update:
'''
from databases_config import database_config

class HousingPriceMysql(object):
    '''
    The mongo database for storing the housing prices
    '''

    def __init__(self):

        self.__housing_mongo_config()

    def __housing_mongo_config(self):
        self.host = database_config.get('myql_crawling', 'host')
        self.user = database_config.get('myql_crawling', 'user')
        self.password = database_config.get('myql_crawling', 'password')
        self.db_name = database_config.get('myql_crawling', 'db_name')


if __name__ == '__main__':
    housing_mongo = HousingPriceMysql()
    print housing_mongo.password