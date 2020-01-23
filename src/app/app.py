import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
    f"postgresql://" \
    f"{os.environ.get('POSTGRES_USER', 'git_user')}:" \
    f"{os.environ.get('POSTGRES_PASSWORD', 'git_pass')}@" \
    f"{os.environ.get('CONN_STRING', 'database')}/" \
    f"{os.environ.get('POSTGRES_DB', 'git_db')}"
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 3
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

# create flask instance, and connect to db