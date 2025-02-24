from flask import Blueprint, request, redirect, render_template, request, url_for, session, flash
bp = Blueprint('login', __name__, url_prefix='/login')

USERS = {"pokuston": "kouzelnik", "admin": "admin", "student":"zak"}

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username] == password:
            flash("Login successful", "message")
            return redirect(url_for('index'))
        flash("Login failed", "warning")
    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        if username and password and email:
            if username not in USERS:
                USERS[username] = password
                flash("Register successful", "message")
                return redirect(url_for('index'))
            flash("User already exists", "warning")
    return render_template('register.html')
