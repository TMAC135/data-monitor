# -*- coding:utf-8 -*-
'''
Author: Qi Mo
Created: August 19, 2016
Version: 1.0
Update:

November 16, 2016
add city_list and picture the housing_price
'''

import hashlib
import sys
import datetime
from base import smooth_num_list
import flask.ext.login as flask_login
from flask import request, render_template, url_for, session, redirect
from flask.ext.principal import Principal, identity_loaded, identity_changed, Identity, Need, Permission

from __init__ import app
from web_crawler.china_housing_price.lianjia_confg import LIANJIA_MAP
from forms import LoginForm
from models.housing_price.housing_price_model import HousingPriceModel
import json

reload(sys)
sys.setdefaultencoding('utf-8')

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

principals = Principal(app)

@app.route('/first_tier_city_list')
@flask_login.login_required
def first_tier_city_list():
    '''
    choose housing price city
    :return:
    '''
    # 权限管理
    city_list = { x for x in LIANJIA_MAP}
    city_dict = {}
    for pos,x in enumerate(city_list):
        city_dict[pos+1] = x

    perm1 = Permission(Need('need1', 'my_value'))
    perm2 = Permission(Need('need2', 'my_value'))

    return render_template('housing_price/city_dict.html',
                           title='选择城市',
                           permission1=perm1.can(),
                           permission2=perm2.can(),
                           user=session['username'],
                           city_dict=city_dict
                           )

@app.route('/housing_price', methods=['POST', 'GET'])
@flask_login.login_required
def housing_price():
    '''
    controller layer for housing_price
    :return:
    '''
    # 与界面交互

    now = datetime.datetime.utcnow() - datetime.timedelta(days=1)
    last_day = now - datetime.timedelta(days=80)
    now_str = str(now)[:10]
    last_day_str = str(last_day)[:10]

    date_begin = request.args.get('begin', last_day_str, type=str)
    date_end = request.args.get('end', now_str, type=str)
    smooth_days = request.args.get('day', 0, type=int)

    # get city name
    city_name = request.args.get('city', 'Beijing', type=str)

    # get housing_price_list
    housing_price_model = HousingPriceModel()
    housing_price_list = housing_price_model.get_housing_price_list(date_end,date_begin,smooth_days,city_name)

    print housing_price_list
    # list to json
    housing_price_list_json = json.dumps(housing_price_list,encoding='utf-8')

    # permission
    perm1 = Permission(Need('need1', 'my_value'))
    perm2 = Permission(Need('need2', 'my_value'))
    perm3 = Permission(Need('need3', 'my_value'))

    if perm2.can():
        return render_template('housing_price/housing_price.html',
                               title=("{0}  HousingPrice ".format(city_name)).decode('utf8'),
                               smooth=u'smooth days',
                               city_name=city_name,
                               module_list=housing_price_list_json,
                               smooth_num_list=smooth_num_list,
                               user=session['username'],
                               permission1=perm1.can(),
                               permission2=perm2.can(),
                               permission3=perm3.can(),
                               date_begin=date_begin,
                               date_end=date_end
                               )
    return redirect(url_for('housing_price', _external=True, _scheme='http'))