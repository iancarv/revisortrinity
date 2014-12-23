# -*- coding: utf-8 -*-

import os

from app import app, envs, collection, db
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    lastGroup = ''
    a = []
    index = 0
    a = collection.find({})
    return render_template('listaverbetes.html', groups=a)


@app.route('/verbete/<verbete>')
def show_user_profile(verbete):
    a = collection.find_one({'normalized': verbete})
    b = db.css.find_one({'type': 'css'})
    return render_template('verbete.html', verbete=a, css=b)


@app.route('/savecss', methods=['POST'])
def saveCSS():
    new_css = request.form.get('css')
    print(db.css.update({'type': 'css'}, {'$set': {'text' : new_css}}, upsert=False))
    return "OK"


@app.route('/savehtml', methods=['POST'])
def saveHTML():
    verbete_id = request.form.get('id')
    text = request.form.get('html')
    print(verbete_id)
    print(collection.update({'normalized':verbete_id}, {'$set': {'description' : text}}, upsert=False))
    return "OK"
