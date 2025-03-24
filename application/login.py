import functools

from flask import Blueprint, request, redirect, render_template, request, url_for, session, flash

from application import db_execute

bp = Blueprint('login', __name__, url_prefix='/login')

def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            flash("SEKCE POUZE PRO PŘIHLÁŠENÉ", "warning")
            return redirect(url_for("login.login"))
        return func(*args, **kwargs)
    return wrapper

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        command = "SELECT username FROM users WHERE username = ? and password = ?"
        result = db_execute(command, (username, password))

        if result:
            session["user"] = username
            flash("Login successful", "message")
            return redirect(url_for('index'))

        flash("Login failed", "warning")

    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']
        error = False


        checkout_command = "SELECT id FROM users WHERE username = ? OR email = ?"
        existing_user = db_execute(checkout_command, (username, email))

        if existing_user:
            flash("Username or email already exists", "warning")
        elif password != confirm_password:
            error = True
            flash("Passwords don't match", "warning")
        else:
            register_command = "INSERT INTO users (username, password, email) VALUES (?, ?, ?)"
            db_execute(register_command, (username, password, email))
            flash("Registration successful", "message")
            return redirect(url_for('index'))

    return render_template('register.html')

@bp.route("/users")
def user_list():
    command = "SELECT username, password FROM users"
    results = db_execute(command)
    print(results)
    return render_template("user.html", results=results)

@bp.route("/homepage")
def homepage():
    return render_template("index.html")

@bp.route('/logout')
def logout():
    session.pop("user", None)
    flash("Odhlášení bylo úspěšné", "message")
    return redirect(url_for('login.login'))

@bp.route("/shop")
def shop():
    product_command = "SELECT name, price FROM products"
    results = db_execute(product_command)
    print(results)
    return render_template("shop.html", results=results)

