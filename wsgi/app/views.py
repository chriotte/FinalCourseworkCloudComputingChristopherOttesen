from app import app
from flask import render_template, request
import unirest
import database
import simple
from forms import MessageForm
from flask_navigation import Navigation

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/emotion/')
def emotion():
	return render_template("my_form.html",mood='happy',form=MessageForm())


@app.route('/emotion/', methods=['POST'])
def emotion_post():
	msg = request.form['message']
	response = unirest.post("https://community-sentiment.p.mashape.com/text/",
	  headers={
	    "X-Mashape-Key": "6VWQcE5umumsh9oLsHfFlOseFGbDp1caaUKjsnj6PJRqxZKslv",
	    "Content-Type": "application/x-www-form-urlencoded",
    	"Accept": "application/json"
    	},
  		params={
    	"txt": msg
  		}
	)
	return render_template("my_form.html",mood=response.body['result']['sentiment'],form=MessageForm())

nav = Navigation(app)

nav.Bar('top', [
nav.Item('Home', 'index'),
nav.Item('Emotion App', 'emotion'),
nav.Item('Vizualisation', 'polynomial'),
nav.Item('Database collections', 'get_all_databases'),
nav.Item('Database get personell', 'get_all_personnel'),
nav.Item('Database London sample', 'get_sample_document')


])
