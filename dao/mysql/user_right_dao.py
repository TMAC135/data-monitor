# -*- coding:utf-8 -*-
'''
Author: Qi Mo
Created: November 15, 2016
Version: 1.0
Update:
'''

import arrow as ar
import logging
from db_helper import houisng_price_db_connection, MySQLHelper

class UserRightDao(object):
    """
    The dao layer for login user info
    """
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)
        self._mysql_helper = MySQLHelper(houisng_price_db_connection)  # get the db connection for user_right

    def get_usr(self,user_name):
        """
        get user_name and passwd by user_name
        :param user_name:  login user_name
        :return:
        """
        sqlstr = """
            SELECT name,passwd FROM login_user WHERE name = '%s'
        """ % (user_name)
        try:
            result = self._mysql_helper.query(sqlstr)
            return result
        except Exception as e:
            self.logger.exception(e)

    def get_usr_id(self, user_name):
        """
        get user_id by user_name
        :param user_name:  user_name
        :return:
        """
        sqlstr = """
            SELECT id FROM login_user WHERE name = '%s'
        """ % (user_name)
        try:
            result = self._mysql_helper.query(sqlstr)
            return result
        except Exception as e:
            self.logger.exception(e)

    def get_right_by_user_id(self,user_id):
        """
        get user right by user_name
        :param user_name:  user_name
        :return:
        """
        sqlstr = """
            SELECT user_grant.right_id FROM login_user,user_grant WHERE user_grant.user_id = login_user.id AND
                 login_user.id = '%d'
        """ % (user_id)
        try:
            result = self._mysql_helper.query(sqlstr)
            return result
        except Exception as e:
            self.logger.exception(e)

    def get_right_by_user_name(self,user_name):
        """
        get user right by user_name
        :param user_name:  user_name
        :return:
        """
        sqlstr = """
            SELECT user_grant.right_id FROM login_user,user_grant WHERE user_grant.user_id = login_user.id AND
                 login_user.name = '%s'
        """ % (user_name)
        try:
            result = self._mysql_helper.query(sqlstr)
            return result
        except Exception as e:
            self.logger.exception(e)

    def insert_usr(self,name,email,passwd,create_time):
        """
        add user_info
        :param name:  user_name
        :param email:  email
        :param passwd:  password
        :param create_time:
        :return:
        """
        if len(self.get_usr(name))>0:
            sql = "UPDATE login_user " \
                  "SET passwd=%(passwd)s " \
                  "WHERE name=%(name)s;"
        else:
            sql = "INSERT INTO login_user (name,email,passwd,create_time) VALUES " \
            "(%(name)s,%(email)s,%(passwd)s,%(create_time)s);"
        try:
            self._mysql_helper.excute(sql, name=name, email=email,
                                      passwd=passwd, create_time=create_time)
        except Exception as e:
            self.logger.exception(e)


    def insert_user_right(self,user_id,right_id):
        """
        add user_right
        :param user_id:
        :param right_id:
        :return:
        """

        exist_list = [x['right_id'] for x in self.get_right_by_user_id(user_id)]

        sql_list = []
        for x in right_id :
            if x not in exist_list:
                data = (int(user_id),int(x))
                sql_list.append(data)

        if len(sql_list) == 0:
            return

        sql = """INSERT INTO user_grant (user_id, right_id) VALUES (%s, %s)"""
        try:
            self._mysql_helper.executemany(sql, sql_list)
        except Exception as e:
            self.logger.exception(e)

if __name__ == '__main__':
    F = UserRightDao();
    name = 'moqi'
    email = '185986777@qq.com'
    passwd = 'moqi123'
    creat_time = ar.now().naive
    F.insert_usr(name, email, passwd, creat_time)
    print F.get_usr("moqi");

    F.insert_user_right(1,[1,2,3])