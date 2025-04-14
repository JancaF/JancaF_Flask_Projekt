from flask import Flask, render_template
from flask import Blueprint, session
from application.db import db_execute, create_db
from flask_login import current_user, LoginManager, UserMixin
from os import path
app = Flask(__name__, template_folder='../templates', static_folder='../static')
bp = Blueprint('application', __name__, url_prefix='/application')
app.config["SECRET_KEY"] = "dev"
app.config["DATABASE"] = "database.sqlite"
app.config["DB_SCHEME"] = "shop.sql"

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


def get_roles_dict():
    roles = db_execute("SELECT id, name FROM roles")
    return {role[0]: role[1] for role in roles}


@login_manager.user_loader
def load_user(user_id):
    if 'user' in session:
        # Pokud je 'user' pouze ID, musíš získat celý uživatelský objekt z databáze
        if isinstance(session['user'], str):  # Pokud je to ID
            user_data = db_execute(f"SELECT * FROM users WHERE id = {session['user']}")
            if user_data:
                user = user_data[0]
                role_id = user['role_id']

                # Pokud uživatel nemá roli, přiřaď mu roli VISITOR
                if not role_id:
                    role_id = db_execute("SELECT id FROM roles WHERE name = 'VISITOR'")[0][0]
                    db_execute(f"UPDATE users SET role_id = {role_id} WHERE id = {user['id']}")

                return User(user['id'], user['username'], user['password'], role_id)
        elif isinstance(session['user'], dict):  # Pokud je 'user' slovník
            return User(session['user']['id'], session['user']['username'], "", session['user']['role_id'])
    return None


@app.context_processor
def inject_user_and_role():
    if 'user' in session:
        if isinstance(session['user'], dict):
            roles_dict = get_roles_dict()
            role_id = session['user'].get('role_id')
            return {
                'current_user': session['user'].get('username'),
                'current_role': roles_dict.get(role_id, 'Neznámá role')
            }
        else:
            # Pokud 'user' není slovník, to znamená, že session obsahuje ID uživatele (nebo něco jiného)
            return {
                'current_user': None,
                'current_role': None
            }
    return {
        'current_user': None,
        'current_role': None
    }
