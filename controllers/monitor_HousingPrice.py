# -*- coding:utf-8 -*-
'''
Author: Qi Mo
Created: August 19, 2016
Version: 1.0
Update:
'''

import hashlib
import sys

import flask.ext.login as flask_login
from flask import request, render_template, url_for, session, redirect
from flask.ext.principal import Principal, identity_loaded, identity_changed, Identity, Need

from __init__ import app
from forms import LoginForm
import json

reload(sys)
sys.setdefaultencoding('utf-8')

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

principals = Principal(app)

@app.route('/first_tier_city')
def first_tier_city():
    value_data = [
        {'name': "'海门'", 'value': 9},
    ]
    geoCoordMap = {
        "'海门'": [121.15, 31.89],
    }
    value_data = json.dumps(value_data)
    print value_data

    return render_template('housing_price/first_tier_city.html',value_data=value_data, geoCoordMap = geoCoordMap)