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
<<<<<<< HEAD

Dec 7, 2016
    the github for flask google map is: https://github.com/rochacbruno/Flask-GoogleMaps
    1: add more templates for the crime prediction for google map with flask
=======
>>>>>>> 65e2c7f642e623db598415fedfcbb5b7e7d38dd6
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
<<<<<<< HEAD
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons


# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4"

# you can also pass key here
GoogleMaps(app, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")

=======
>>>>>>> 65e2c7f642e623db598415fedfcbb5b7e7d38dd6
@app.route('/minneapolis_simple_analysis')
@flask_login.login_required
def minneapolis_simple_analysis():
    '''
    choose housing price city
    :return:
    '''
<<<<<<< HEAD
    # permission manage
    perm1 = Permission(Need('need1', 'my_value'))
    perm2 = Permission(Need('need2', 'my_value'))

    mymap = Map(
        identifier="view-side",  # for DOM element
        varname="mymap",  # for JS object name
        lat=37.4419,
        lng=-122.1419,
        style="height:500px;width:500px;margin:0;",
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        varname="sndmap",
        lat=37.4419,
        lng=-122.1419,
        style="height:500px;width:1000px;margin:0;",
        markers={
            icons.dots.green: [(37.4419, -122.1419), (37.4500, -122.1350)],
            icons.dots.blue: [(37.4300, -122.1400, "Hello World")]
        }
    )

    trdmap = Map(
        identifier="trdmap",
        varname="trdmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': icons.alpha.B,
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "Hello I am <b style='color:green;'>GREEN</b>!"
            },
            {
                'icon': icons.dots.blue,
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "Hello I am <b style='color:blue;'>BLUE</b>!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                'lat': 37.4500,
                'lng': -122.1350,
                'infobox': (
                    "Hello I am <b style='color:#ffcc00;'>YELLOW</b>!"
                    "<h2>It is HTML title</h2>"
                    "<img src='//placehold.it/50'>"
                    "<br>Images allowed!"
                )
            }
        ]
    )



    movingmap = Map(
        identifier="movingmap",
        varname="movingmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'lat': 37.4500,
                'lng': -122.1350
            }
        ],
        zoom=12
    )

    movingmarkers = [
        {
            'lat': 37.4400,
            'lng': -122.1350
        },
        {
            'lat': 37.4430,
            'lng': -122.1350
        },
        {
            'lat': 37.4450,
            'lng': -122.1350
        },
        {
            'lat': 37.4490,
            'lng': -122.1350
        }
    ]


    return render_template(
            'minneapolis_crime_prediction/data_analysis_crimes.html',
            permission1=perm1.can(),
            permission2=perm2.can(),
            user=session['username'],
            mymap=mymap,
            sndmap=sndmap,
            trdmap=trdmap,
            movingmap=movingmap,
            movingmarkers=movingmarkers,
    )

=======
    # 权限管理

    perm1 = Permission(Need('need1', 'my_value'))
    perm2 = Permission(Need('need2', 'my_value'))

    return render_template('minneapolis_crime_prediction/data_analysis_crimes.html',
                           permission1=perm1.can(),
                           permission2=perm2.can(),
                           user=session['username'],
                           )
>>>>>>> 65e2c7f642e623db598415fedfcbb5b7e7d38dd6

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
<<<<<<< HEAD
    # permission management
=======
    # 权限管理

>>>>>>> 65e2c7f642e623db598415fedfcbb5b7e7d38dd6
    perm1 = Permission(Need('need1', 'my_value'))
    perm2 = Permission(Need('need2', 'my_value'))

    return render_template('us_airline_delay_prediction/data_analysis.html',
                           permission1=perm1.can(),
                           permission2=perm2.can(),
                           user=session['username'],
                           )