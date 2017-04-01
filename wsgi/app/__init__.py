from flask import Flask

app = Flask(__name__)

app.secret_key = 'ZoltaR2'

from app import views

