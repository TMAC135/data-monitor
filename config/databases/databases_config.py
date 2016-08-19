# -*- coding:utf-8 -*-
'''
Author: Ran Tian
Created: 16/8/5
Version: 1.0
Update:
'''
import ConfigParser
import logging
from utils import PROJECT_DIR

class DatabaseConfig(object):
    '''
    The config object for the databases including mongodb and mysql, The corresponding
    config file is default.cfg under the same directory.
    '''
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)

        self.config = ConfigParser.ConfigParser()
        try:
            self.config.readfp(open(PROJECT_DIR + "/config/databases/defaults.cfg"))
        except Exception as e:
            self.logger.exception(e)

    def get(self,section,key):
        '''
        Extract the specific value under section and key
        :param section:
        :param key:
        :return:
        '''
        try:
            return self.config.get(section,key)
        except Exception as e:
            self.logger.exception(e)

database_config = DatabaseConfig()

if __name__ == '__main__':
    print database_config.get('mysql_crawling','db_name')