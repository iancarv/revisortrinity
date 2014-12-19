#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app
@app.route('/')
@app.route('/index')
def index():
	env_var = os.environ['OPENSHIFTDATADIR']
    f = open('/static/verbetes.json')


@app.route('/verbetes/<verbete>')
def show_user_profile(verbete):
    return render_template('verbetes.html', verbete)