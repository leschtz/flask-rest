from flask import json, render_template, jsonify, Response
from bson import json_util

from models.User import User
from config import MONGO_DB


def index():
    return jsonify(json_util.dumps(MONGO_DB.db.users.find()))


def store():
    user = User(1, "TestUser", 19).serialize
    print(user)
    MONGO_DB.db.users.insert_one(user)
    return render_template("pass.html")


def show(userId):
    pass


def update(userId):
    pass


def delete(userId):
    pass