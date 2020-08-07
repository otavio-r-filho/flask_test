import sys
import os
import logging
from flask import Flask, escape, request, render_template
# from flask_restful import Resource, Api

sys.path.append("src")
from utils.dao import check_user_db, create_new_user

# Setting logging
LOG_FORMAT = "[%(asctime)s] %(levelname)s: %(message)s"
logging.basicConfig(filename='app.log', filemode="w", level=logging.INFO, format=LOG_FORMAT, datefmt='%m/%d/%Y - %H:%M:%S')

project_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
user_db = check_user_db(project_path)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", name=None)

@app.route("/new_user")
def new_user():
    new_user = create_new_user(user_db)
    if new_user:
        user_db[new_user] = []
        return new_user
    else:
        return "ERROR"

@app.route("/show_users")
def show_users():
    users_lst = list(user_db.keys())
    users_lst = "\n".join(["Users:"] + users_lst)
    return users_lst
