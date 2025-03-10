from flask import Flask, render_template
from application.db import db_execute
from flask import Blueprint

bp = Blueprint('application', __name__, url_prefix='/application')
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'dev'
app.config['DATABASE'] = 'DATABASE'



@app.route('/')
def index():
    return render_template('base.html')

@bp.route("/users")
def user_list():
    command = "SELECT (username, password) FROM users"
    result = db_execute(command)
    print(result)
    return render_template("user.html", result=result)
