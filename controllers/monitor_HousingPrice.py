# -*- coding:utf-8 -*-
'''
Author: Qi Mo
Created: August 19, 2016
Version: 1.0
Update:

November 16, 2016
add city_list and picture the housing_price

November 20, 2016
    1: add Minneapolis crime prediction controller,
    2: add us airline delay prediction controller

Dec 7, 2016
    the github for flask google map is: https://github.com/rochacbruno/Flask-GoogleMaps
    1: add more templates for the crime prediction for google map with flask
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
                           title='Choose City',
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

###########################################################################
# minneapolis crime prediction
###########################################################################
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons

from models.minneapolis_crime_prediction import *
crime_model = MinneapolisCrimePrediction()

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4"

# you can also pass key here
GoogleMaps(app, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")

@app.route('/minneapolis_simple_analysis',methods=['POST','GET'])
@flask_login.login_required
def minneapolis_simple_analysis():
    '''
    choose housing price city
    :return:
    '''
    # permission manage
    perm1 = Permission(Need('need1', 'my_value'))
    perm2 = Permission(Need('need2', 'my_value'))

    # get the parameter from the form
    lat = request.args.get('lati',44.977276 , type=float)
    lon = request.args.get('long', -93.232266, type=float)
    date = request.args.get('date', '', type=str)
    time = request.args.get('time', "12:00", type=str)

    global crime_model
    top_2_result = crime_model.predict_from_lr(lat,lon,date,time,2)

    maker_box = "Latitude:{0}<br>Longtitude:{1}<br>Time:{2}<br>Predictions: <ol>{3} for {4}</ol><ol>{5} for {6}</ol>".format(lat,lon,time,
                top_2_result[0][0],top_2_result[0][1],top_2_result[1][0],top_2_result[1][1])
    sndmap = Map(
        identifier="sndmap",
        varname="sndmap",
        zoom=11,
        lat=44.977276,
        lng=-93.232266,
        style="height:600px;width:1200px;margin:0;",
        markers={
            # icons.dots.green: [(37.4419, -122.1419), (37.4500, -122.1350)],
            icons.dots.blue: [(lat, lon, maker_box)]
        }
    )


    return render_template(
            'minneapolis_crime_prediction/data_analysis_crimes.html',
            permission1=perm1.can(),
            permission2=perm2.can(),
            user=session['username'],
            sndmap=sndmap,
    )


###########################################################################
# us airline delay prediction
###########################################################################
@app.route('/us_airline_delay_prediction')
@flask_login.login_required
def us_airline_delay_prediction():
    '''
    choose
    :return:
    '''
    # permission management
    # 权限管理

    perm1 = Permission(Need('need1', 'my_value'))
    perm2 = Permission(Need('need2', 'my_value'))

    return render_template('us_airline_delay_prediction/data_analysis.html',
                           permission1=perm1.can(),
                           permission2=perm2.can(),
                           user=session['username'],
                           )