from flask import Blueprint, request, redirect, render_template, request, url_for, session, flash
bp = Blueprint('login', __name__, url_prefix='/login')

USERS = {"pokuston": "kouzelnik", "admin": "admin", "student":"zak"}

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username':'password'] in USERS:
            flash("Login successful", "message")
            return redirect(url_for('index'))
        flash("Login failed", "warning")
    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form == ["username", "password", "email"]:
            if USERS[request.form['username']] == "admin":
                flash("Register successful", "message")
                return redirect(url_for('index'))
            flash("User registration failed", "warning")
    return render_template('register.html')