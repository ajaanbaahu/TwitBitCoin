from flask import Flask
from flask.ext.mongoengine import MongoEngine
app = Flask(__name__)
app.config["MONGODB_SETTINGS"]={'DB':"my_CI_log"}
app.config["SECRET_KEY"]= "password123!"

db=MongoEngine(app)

from app import views