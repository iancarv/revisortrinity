# -*- coding: utf-8 -*-

import os
import logging

from app import app, envs, collection, db
from flask import render_template, request
from bson.objectid import ObjectId


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
    print(a['_id'])
    print(str(a['_id']))
    a_id = int(str(a['_id']), base=16)
    print(hex(a_id - 1)[2:])
    next = collection.find_one({'_id': ObjectId(hex(a_id + 1)[2:])})
    prev = collection.find_one({'_id': ObjectId(hex(a_id - 1)[2:])})
    b = db.css.find_one({'type': 'css'})
    print(a)
    return render_template('verbete.html',
                           verbete=a,
                           css=b,
                           next=next,
                           prev=prev)


@app.route('/savecss', methods=['POST'])
def saveCSS():
    new_css = request.form.get('css')
    print(db.css.update({'type': 'css'}, {'$set': {'text' : new_css}}, upsert=False))
    return "OK"


@app.route('/savehtml', methods=['POST'])
def saveHTML():
    verbete_id = request.form.get('id')
    desc = request.form.get('html')
    phon = request.form.get('phonema')
    logging.debug(phonema)
    logging.debug(verbete_id)
    print(collection.update({'normalized':verbete_id},
        {'$set': {'description' : desc, 'phonema' : phon}}, upsert=False))
    return "OK"
