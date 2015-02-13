import time
from flask import Flask,flash
from flask.ext.pymongo import PyMongo  
from pymongo import Connection

# app = Flask(__name__)
# mongo = PyMongo(app)
connection = Connection()
db = connection.test_database

class Images(object):
    def find(sel):
        return db.posts.find()

    def insert(sel,image):
        db.images.insert(image)
        return True
