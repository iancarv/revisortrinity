# -*- coding: utf-8 -*-

import os

from app import app
from pymongo import MongoClient


@app.route('/')
@app.route('/index')
def index():
    return 'Hello'
    # env_uri = env_var = os.environ['OPENSHIFT_MONGODB_DB_URL']
    # client = MongoClient(env_uri)
    # db = client['trinity']
    # collection = db['verbetes']
    # return str(collections)


@app.route('/verbetes/<verbete>')
def show_user_profile(verbete):
    return render_template('verbetes.html', verbete)
