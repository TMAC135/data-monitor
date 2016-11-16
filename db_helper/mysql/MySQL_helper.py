#-*- coding:utf-8 -*-
'''
Author: TianRan
Date: 8/13/16
Version:

Update:

11/15/2016 QI MO
add executemany
'''
import logging
class MySQLHelper(object):
    '''
    Helper class for SQL language in mysql
    '''
    def __init__(self,db):
        '''
        :param db: The db connection from torndb.Connection
        '''
        self.logger = logging.getLogger(type(self).__name__)
        self._db = db

    def excute(self, sql, *kwargs,**kwargsdict):
        """
        Update, Insert, Delete
        :param sql: 传入的SQL 语句，参数用 %s 对应
        :param kwargs:
        :return:
        """
        return self._db.execute(sql, *kwargs,**kwargsdict)

    def executemany(self, sql,  *kwargs,**kwargsdict):
        """
        Update, Insert, Delete
        :param sql: 传入的SQL 语句，参数用 %s 对应
        :param kwargs:
        :return:
        """
        return self._db.executemany(sql,  *kwargs,**kwargsdict)

    def query(self, sql, *kwargs, **kwargsdict):
        """
        Select operation
        :param sql:
        :param kwargs:
        :return:
        """
        return self._db.query(sql, *kwargs, **kwargsdict)

    def get(self, sql, *kwargs,  **kwargsdict):
        """
        Select operation, but only return the first query element
        :param sql:
        :param kwargs:
        :return:
        """
        return self._db.get(sql, *kwargs, **kwargsdict)


if __name__ == '__main__':
    from db_connections import houisng_price_db_connection
    helper = MySQLHelper(houisng_price_db_connection)
    print helper.query('select * from housing_price')