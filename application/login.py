from flask import Blueprint, request, redirect, render_template, request, url_for, session, flash

from application import db_execute

bp = Blueprint('login', __name__, url_prefix='/login')

USERS = {"pokuston": "kouzelnik", "admin": "admin", "student":"zak"}

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        command = "SELECT username FROM users WHERE username = ? and password = ?"

        result = db_execute(command, (username,password))
        print(result)


        if request.form['username'] == password in USERS:
            flash("Login successful", "message")
            return redirect(url_for('index'))
        flash("Login failed", "warning")
    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        register_command = "INSERT INTO users (username, password, email) VALUES (?, ?, ?)"
        result = db_execute(register_command, (username, password, email))
        print(result)

        if request.form == ["username", "password", "email"]:
            if USERS[request.form['username']] == username and USERS[request.form['password']] == password and USERS[request.form['email']] == email:
                flash("Registration successful", "message")
                return redirect(url_for('index'))
            else:
                flash("Registration failed", "warning")
    return render_template('register.html')

@bp.route("/users")
def user_list():
    command = "SELECT username, password FROM users"
    results = db_execute(command)
    print(results)
    return render_template("user.html", results=results)