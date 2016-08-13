# -*- coding:utf-8 -*-
'''
Author: Qi Mo
Created: August 12, 2016
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

reload(sys)
sys.setdefaultencoding('utf-8')

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

principals = Principal(app)


@app.route('/')
def index1():
    return redirect(url_for('login'))

@app.route('/index')
def index():
    return render_template('index.html')

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(Username):
    users = dict()
    users['name'] = 'momo'

    if Username == users['name']:
        user = User()
        user.id = Username
        return user
    return

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():

            users = dict()
            users['name'] = 'momo'
            users_hash_md5 = hashlib.md5('momo123123')
            users['passwd'] = users_hash_md5.hexdigest()

            hash_md5 = hashlib.md5(form.password.data)
            Password = hash_md5.hexdigest()

            return redirect(url_for('index'))

    #         if form.username.data == users['name'] and Password == users['passwd']:
    #             user = User()
    #             user.id = users['name']
    #             flask_login.login_user(user)
    #
    #             return redirect(url_for('index', _external=True, _scheme='http'))
    #
    #         return render_template('login.html', title='', form=form)
        else:
            return render_template('login.html', title='', form=form)
    except Exception as e:
        print e
        return 'error'
        # return render_template('login.html', title='', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@flask_login.login_required
def logout():
    session.pop('username', None)
    identity_changed.send(app, identity=Identity('none'))
    flask_login.logout_user()
    return redirect(url_for('login', _external=True, _scheme='http'))