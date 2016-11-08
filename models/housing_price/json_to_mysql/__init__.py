#-*- coding:utf-8 -*-
'''
Author: TianRan
Date: 8/14/16
Version:
'''
import os
import sys

current_path = os.path.abspath(__file__)
current_path += "/../../../../"

sys.path.append(os.path.normpath(current_path))
reload(sys)

if __name__ == '__main__':
    pass
    # print sys.path.append()