# - Import flask and import the controller - This is the Flask setup


from flask import Flask

app = Flask(__name__)

from app import controller

