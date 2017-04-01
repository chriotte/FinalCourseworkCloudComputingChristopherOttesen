from flask_wtf import Form
from wtforms import TextField, validators

class MessageForm(Form):
   message = TextField(u'What is on your mind?', [validators.optional(), validators.length(max=200)])



