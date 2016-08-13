# -*- coding:utf-8 -*-
'''
Author: Qi Mo
Created: August 13, 2016
Version: 1.0
Update:
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import Required, DataRequired


class LoginForm(Form):

    username = TextField("UserName:", validators=[DataRequired()])
    password = PasswordField('PassWord:', validators=[DataRequired()])
    submit = SubmitField("Login")