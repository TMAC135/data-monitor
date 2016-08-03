# -*- coding:utf-8 -*-
'''
Author: Ran Tian
Created: 16/7/28
Version: 1.0
Update:
'''
import logging, logging.handlers
import os
from path_util import PROJECT_DIR

log_dir = PROJECT_DIR + '/logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


def log_format(log_path):
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    #The default stdout is on the screen
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=format)

    # format of the log on the file
    # 2015-06-04 16:12:56,510 - root - WARNING - fail to get the name
    log_formatter = logging.Formatter(format)
    handler = logging.handlers.TimedRotatingFileHandler('{0}/time.log'.format(log_path),
                                                        when='H',
                                                        interval=1,
                                                        backupCount= 7 * 24)
    # set handler config
    handler.setLevel(logging.INFO)
    handler.setFormatter(log_formatter)
    # add handler to the logger
    logging.getLogger().addHandler(handler)


if __name__ == '__main__':

    log_format(PROJECT_DIR + '/logs/test1')
    logger = logging.getLogger('test1').info('haha')