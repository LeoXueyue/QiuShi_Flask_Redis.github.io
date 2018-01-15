# coding:utf-8

from flask import Flask

app = Flask(__name__)

app.debug = True

from app.home import home as home_blueprint

app.register_blueprint(home_blueprint, url_prefix='/home')
