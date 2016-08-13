# -*- coding:utf-8 -*-
'''
Author: Ran Tian
Created: 16/8/3
Version: 1.0
Update:
    08/03: ensure_dir
'''
import os
import logging

def ensure_dir(file_dir):
    '''
    Make sure the file directory exist, if not, create it.
    :param file_path:
    :return:
    '''
    logger = logging.getLogger('LogUtils')
    try:
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
    except Exception as e:
        logger.exception(e)








if __name__ == '__main__':
    pass