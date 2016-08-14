#-*- coding:utf-8 -*-
'''
Author: TianRan
Date: 8/13/16
Version:
'''
import torndb
import logging
from config import housing_price_mysql

logger = logging.getLogger('MySQLDbConnection')
def housing_price_sql_connection(mysql_config):
    '''
    Connect the mysql database from configuration file
    :param mysql_config:
    :return:
    '''
    db_name = mysql_config.db_name
    host = mysql_config.host
    user = mysql_config.user
    passward = mysql_config.password
    print db_name,host,user,passward

    try:
        return torndb.Connection(host=host,database=db_name,user=user,password=passward)
    except Exception as e:
        print e
        logger.exception(e)

houisng_price_db_connection = housing_price_sql_connection(housing_price_mysql)

if __name__ == '__main__':
    # print houisng_price_db_connection
    print houisng_price_db_connection.query('select * from housing_price')