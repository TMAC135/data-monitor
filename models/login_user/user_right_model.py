# -*- coding:utf-8 -*-
'''
Author: Qi Mo
Created: November 15, 2016
Version: 1.0
Update:
'''

from __init__ import  *
import hashlib
from dao.mysql import *

class UserRightModel(object):
    """
    model layer for login user
    """
    def __init__(self):
        self.F = UserRightDao()

    def get_usr(self,user_name):
        """
        get user_name and pass_word
        :param user_name:
        :return:
        """
        result = self.F.get_usr(user_name)
        return result

    def get_right(self, user_name):
        """
        get user_right by user_name
        :param user_name:
        :return:
        """
        result = self.F.get_right_by_user_name(user_name)
        return result

    def insert_usr(self,name,email,passwd,create_time):
        """
        add user
        :param name:
        :param email:
        :param passwd:
        :param create_time:
        :return:
        """
        hash_md5 = hashlib.md5(passwd)
        passwd = hash_md5.hexdigest()
        self.F.insert_usr(name,email,passwd,create_time)

    def insert_right(self,user_name,right_list):
        """
        add user_right
        :param user_name:
        :param right_list:
        :return:
        """

        result = self.F.get_usr_id(user_name)
        if len(result) >1:
            print 'error! exist repeat username'
        elif len(result) == 0:
            print 'error! not exit this username'
        else:
            user_id = result[0]['id']
            self.F.insert_user_right(user_id, right_list)

if __name__ == '__main__':
    F = UserRightModel()
    # 新增用户
    name = 'moqi'
    email = '185986777@qq.com'
    passwd = 'moqi123'
    creat_time = ar.now().naive
    F.insert_usr(name,email,passwd,creat_time)
    # 新增用户权限
    ritht_list = [1,2,3]
    F.insert_right(name,ritht_list)
    # 查看用户权限
    print F.get_right(name)

    F = UserRightModel()
    # 新增用户
    name = 'tianran'
    email = ''
    passwd = 'tianran123'
    creat_time = ar.now().naive
    F.insert_usr(name, email, passwd, creat_time)
    # 新增用户权限
    ritht_list = [1, 2, 3]
    F.insert_right(name, ritht_list)
    # 查看用户权限
    print F.get_right(name)

    F = UserRightModel()
    # 新增用户
    name = 'guest'
    email = ''
    passwd = 'guest'
    creat_time = ar.now().naive
    F.insert_usr(name, email, passwd, creat_time)
    # 新增用户权限
    ritht_list = [1, 2]
    F.insert_right(name, ritht_list)
    # 查看用户权限
    print F.get_right(name)

