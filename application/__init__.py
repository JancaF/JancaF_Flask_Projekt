from flask import Flask, render_template
from flask import Blueprint, session
from application.db import db_execute, create_db
from flask_login import current_user, LoginManager, UserMixin
from os import path
app = Flask(__name__, template_folder='../templates', static_folder='../static')
bp = Blueprint('application', __name__, url_prefix='/application')
app.config["SECRET_KEY"] = "dev"
app.config["DATABASE"] = "database.sqlite"
app.config["DB_SCHEME"] = "sqlite"

login_manager = LoginManager()
login_manager.login_view = 'login'
@app.route("/")
def index():
    return render_template("index.html")


class Role:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def get_role_by_id(cls, role_id):
        role_data = db_execute(f"SELECT name FROM roles WHERE id = {role_id}")  # Příklad s databází
        if role_data:
            return cls(role_id, role_data[0])  # vrátí roli podle ID
        return None

class User(UserMixin):
    def __init__(self, id, username, password, role_id):
        self.id = id
        self.username = username
        self.password = password
        self.role_id = role_id

    @classmethod
    def get(cls, user_id):
        # Implementuj způsob, jak získat uživatele z DB na základě user_id
        # například:
        return db_execute(f"SELECT * FROM users WHERE id = {user_id}")


@login_manager.user_loader
def load_user(user_id):
    if 'user' in session:
        print(session['user'])  # Toto ti ukáže, co je uloženo v session['user']
        return User(session['user']['id'], session['user']['username'], "", session['user']['role_id'])
    return None

@app.context_processor
def inject_user_and_role():
    if 'user' in session:
        print(session['user'])  # Přidej tento výpis pro kontrolu
        role = Role.get_role_by_id(session['user']['role_id'])
        return {
            'current_user': session['user']['username'],
            'current_role': role.name if role else 'Bez role'
        }
    return {
        'current_user': None,
        'current_role': None
    }