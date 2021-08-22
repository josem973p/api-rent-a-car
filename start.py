from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from connection import DatabaseConn

app = Flask(__name__)
conn = DatabaseConn(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)