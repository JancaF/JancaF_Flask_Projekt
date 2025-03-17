from flask import Flask, render_template
from flask import Blueprint, session
from application.db import db_execute, create_db
from os import path
app = Flask(__name__, template_folder='../templates', static_folder='../static')
bp = Blueprint('application', __name__, url_prefix='/application')
app.config["SECRET_KEY"] = "dev"
app.config["DATABASE"] = "database.sqlite"


@app.route("/")
def index():
    return render_template("index.html")

@app.context_processor
def inject_user():
    return dict(current_user=session.get("user"))