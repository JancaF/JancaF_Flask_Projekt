# NAČÍTÁNÍ DO MAIN.PY (INIT)
from flask import Flask, render_template
from flask import Blueprint, session
from application.db import db_execute, create_db
from os import path
app = Flask(__name__, template_folder='../templates', static_folder='../static')
bp = Blueprint('application', __name__, url_prefix='/application')
app.config["SECRET_KEY"] = "dev"
app.config["DATABASE"] = "database.sqlite"
app.config["DB_SCHEME"] = "shop.sql"


@app.route("/")
def index():
    """Hlavní homepage funkce (index.html) pro načtení __init__"""
    return render_template("index.html")

@app.context_processor
def inject_user():
    """Umožňuje provést session uživatele pro registraci a přihlašování"""
    return dict(current_user=session.get("user"))