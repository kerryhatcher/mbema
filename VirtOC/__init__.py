__author__ = 'kwhatcher'

from os import environ

from flask import Flask, render_template

from mongoengine import connect

from flask_bootstrap import Bootstrap

from status import StatusApp


app = Flask(__name__)
Bootstrap(app)

connect('heroku_app34423226', host=environ.get('MONGOLAB_URI'))


app.register_blueprint(StatusApp, url_prefix='/status')
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')


@app.route('/')
def hello():
    return render_template('home.html')