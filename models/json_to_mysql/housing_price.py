#-*- coding:utf-8 -*-
'''
Author: TianRan
Date: 8/14/16
Version:
'''
import logging


class UpdateHousingPriceToMysql(object):
    '''
    Put the houisng price to the MySQL database, to modify the
    config of the database, go to the defaults.cfg under config/databases
    '''
    def __init__(self,table_name):
        self.logger = logging.getLogger(type(self).__name__)



if __name__ == '__main__':
    pass