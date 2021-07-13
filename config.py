import os
from flask_pymongo import PyMongo

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
MONGO_URI = "mongodb://localhost:27017/flask-rest"

MONGO_DB = PyMongo()