# -*- coding:utf-8 -*-
'''
Author: Qi Mo
Created: November 16, 2016
Version: 1.0
Update:
'''

import hashlib
import sys

import flask.ext.login as flask_login
from flask import request, render_template, url_for, session, redirect
from flask.ext.principal import Permission, Principal, identity_loaded, identity_changed, Identity, Need

from __init__ import app
from forms import LoginForm
from models.login_user import user_right_model as model

reload(sys)
sys.setdefaultencoding('utf-8')

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

principals = Principal(app)


@app.route('/')
def index1():
    return redirect(url_for('login'))

@app.route('/index', methods=['POST', 'GET'])
@flask_login.login_required
def index():
    perm1 = Permission(Need('need1', 'my_value'))
    perm2 = Permission(Need('need2', 'my_value'))
    perm3 = Permission(Need('need3', 'my_value'))
    return render_template('index.html',
                           # rate_graph_dianshang_list=rate_graph_dianshang_list,
                           # rate_graph_work_list = rate_graph_work_list,
                           # rate_graph_others_list = rate_graph_others_list,
                           permission1=perm1.can(),
                           permission2=perm2.can(),
                           permission3=perm3.can(),
                           user=session['username']
                           )

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(Username):
    F = model.UserRightModel()
    user_info = F.get_usr(Username)

    for users in user_info:
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
            session['username'] = form.username.data
            username = session['username']
            F = model.UserRightModel()
            user_info = F.get_usr(username)

            for users in user_info:
                hash_md5 = hashlib.md5(form.password.data)
                Password = hash_md5.hexdigest()
                if form.username.data == users['name'] and Password == users['passwd']:
                    user = User()
                    user.id = users['name']
                    flask_login.login_user(user)
                    identity_changed.send(app, identity=Identity(form.username.data))
                    return redirect(url_for('index', _external=True, _scheme='http'))

            return render_template('login.html', form=form)
        else:
            return render_template('login.html', form=form)
    except:
        return render_template('login.html', form=form)

@app.route('/guest_login')
def guest_login():
    try:
        session['username'] = 'guest'
        username = session['username']

        F = model.UserRightModel()
        user_info = F.get_usr(username)

        for users in user_info:
            hash_md5 = hashlib.md5('guest')
            Password = hash_md5.hexdigest()
            if username == users['name'] and Password == users['passwd']:
                user = User()
                user.id = users['name']
                flask_login.login_user(user)
                identity_changed.send(app, identity=Identity('guest'))
                return redirect(url_for('index', _external=True, _scheme='http'))
        return render_template('login.html')

    except:
        return render_template('login.html')


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    myusername = identity.id
    if myusername == 'none':
        return
    F = model.UserRightModel()
    rights = F.get_right(myusername)
    for right in rights:
        identity.provides.add(Need('need' + str(right['right_id']), 'my_value'))


@app.route('/logout', methods=['GET', 'POST'])
@flask_login.login_required
def logout():
    session.pop('username', None)
    identity_changed.send(app, identity=Identity('none'))
    flask_login.logout_user()
    return redirect(url_for('login', _external=True, _scheme='http'))
