# -*- coding:utf-8 -*-
'''
Author: Ran Tian
Created: 16/8/5
Version: 1.0
Update:
'''
import ConfigParser

class DatabaseConfig(object):
    '''
    The config object for the databases including mongodb and mysql, The corresponding
    config file is default.cfg under the same directory.
    '''
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open("defaults.cfg"))

    def get(self,section,key):
        '''
        Extract the specific value under section and key
        :param section:
        :param key:
        :return:
        '''
        return self.config.get(section,key)

database_config = DatabaseConfig()

if __name__ == '__main__':
    pass