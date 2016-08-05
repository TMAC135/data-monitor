# -*- coding:utf-8 -*-
'''
Author: Ran Tian
Created: 16/8/5
Version: 1.0
Update:
'''

from databases_config import database_config

class HousingPriceMongo(object):
    '''
    The mongo database for storing the housing prices
    '''

    def __init__(self):

        self.__housing_mongo_config()

    def __housing_mongo_config(self):
        self.mongodb_address = database_config.get('mongodb_crawling', 'db_address')
        self.user = database_config.get('mongodb_crawling', 'user')
        self.passwd = database_config.get('mongodb_crawling', 'passwd')
        self.db_name = database_config.get('mongodb_crawling', 'db_name')


if __name__ == '__main__':
    housing_mongo = HousingPriceMongo()
    print housing_mongo.mongodb_address