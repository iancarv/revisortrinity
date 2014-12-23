from flask import Flask
from pymongo import MongoClient
import os
envs = {}
envs['data'] = os.environ.get('OPENSHIFT_DATA_DIR') or '../../local_data'
envs['db_url'] = os.environ.get('OPENSHIFT_MONGODB_DB_URL') or 'localhost:27017'
app = Flask(__name__)
client = MongoClient(envs['db_url'])
db = client['trinity']
collection = db['verbetes']
from app import views
