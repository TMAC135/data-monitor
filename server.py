# -*- coding:utf-8 -*-
'''
Author: Qi Mo
Created: August 12, 2016
Version: 1.0
Update:
'''

from controllers import app
from utils.path_util import *
from utils.log_util import log_format
import logging

log_format(PROJECT_DIR + '/logs/server')

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=8086,debug=True)
    except Exception as e:
        logger = logging.getLogger('server error')
        logger.exception(e)