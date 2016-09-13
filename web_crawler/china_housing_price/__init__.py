#-*- coding=utf-8 -*-
'''
Author: TianRan
Date: 7/22/16
Version:
'''
import os
import sys

current_path = os.path.abspath(__file__)
project_dir = current_path + '/../../..'

sys.path.append(os.path.normpath(project_dir))
reload(sys)

if __name__ == '__main__':
    print os.path.normpath(current_path)
    print os.path.normpath(project_dir)
    # print sys.path