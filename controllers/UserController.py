from flask import render_template, redirect, url_for, request, abort
from models.User import User
from config import MONGO_DB


def index():
    for x in MONGO_DB.db.users.find():
        print(x)
    return render_template("pass.html")


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