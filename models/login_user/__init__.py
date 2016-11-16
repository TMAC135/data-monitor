# -*- coding:utf-8 -*-
'''
Author: Qi Mo
Created: November 15, 2016
Version: 1.0
Update:
'''
import os
import sys

current_path = os.path.abspath(__file__)
current_path += "/../../../"

sys.path.append(os.path.normpath(current_path))
reload(sys)


if __name__ == '__main__':
    pass