# -*- coding:utf-8 -*-
'''
Author: Ran Tian
Created: 16/7/28
Version: 1.0
Update:
    07/28:
        1: generate the project directory which is independent from system
        2: add the project directory to the system path
'''

import os
import sys

# the project dir and project name
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/..'
PROJECT_DIR = os.path.normpath(PROJECT_DIR)
PROJECT_NAME = os.path.basename(PROJECT_DIR)

# add the project dir to the system path
sys.path.append(PROJECT_DIR)
reload(sys)


if __name__ == '__main__':
    print PROJECT_DIR #/Users/tianran/Desktop/umn_git/data_monitor
    print PROJECT_NAME #data_monitor

    print sys.path