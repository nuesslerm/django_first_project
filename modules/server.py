from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///friends.db"


@app.route("/")
def hello_world():
    return "Hello, Markus!"


@app.route("/blog")
def blog():
    return "These are my thoughts on blogs!"


@app.route("/something")
def something():
    return "These are my thoughts on something!"


__all__ = "app"
