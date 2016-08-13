# -*- coding:utf-8 -*-
'''
Author: Qi Mo
Created: August 12, 2016
Version: 1.0
Update:
'''

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.secret_key = 'dsadasdefe'