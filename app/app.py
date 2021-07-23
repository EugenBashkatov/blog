from flask import Flask
import flask_sqlalchemy


from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
db = flask_sqlalchemy(app)