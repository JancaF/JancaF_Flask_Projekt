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

def role_required(role_id):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if "user" not in session or session["user"]["role_id"] != role_id:
                flash("Nemáte oprávnění k zobrazení této stránky.", "warning")
                return redirect(url_for("login.login"))
            return func(*args, **kwargs)
        return wrapper
    return decorator
@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        command = "SELECT id, username, password, role_id FROM users WHERE username = ?"
        result = db_execute(command, (username,))

        if result:
            user_data = result[0]
            # Porovnání hesla
            if user_data[2] == password:
                # Pokud není role definována, přiřadíme výchozí roli VISITOR
                role_id = user_data[3] if user_data[3] else get_default_role_id()

                session["user"] = {
                    "id": user_data[0],
                    "username": user_data[1],
                    "role_id": role_id
                }
                flash("Login successful", "message")
                return redirect(url_for('index'))
            else:
                flash("Invalid password", "warning")
        else:
            flash("Login failed: User not found", "warning")

    return render_template('login.html')

def get_default_role_id():
    command = "SELECT id FROM roles WHERE name = ?"
    result = db_execute(command, ("VISITOR",))
    if result:
        return result[0][0]  # Vrátí id role VISITOR
    return None  # Pokud roli VISITOR nenajdeme, můžeš přidat výchozí chování


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
@login_required
def user_list():
    if session["user"]["role_id"] != 3:  # ADMIN (ID = 3?)
        flash("Nemáte oprávnění k zobrazení této stránky.", "warning")
        return redirect(url_for("index"))

    command = "SELECT id, username, password FROM users"
    results = db_execute(command)
    # Převeďte seznam n-tic na seznam slovníků, pokud je potřeba
    results = [{'id': user[0], 'username': user[1], 'password': user[2]} for user in results]
    return render_template("user.html", results=results)


@bp.route('/user/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
@role_required(1)  # Pouze pro administrátory
def edit_user(user_id):
    # Nejprve zjisti, zda uživatel existuje
    command = "SELECT id, username, email, role_id FROM users WHERE id = ?"
    user = db_execute(command, (user_id,))

    if not user:
        flash("Uživatel nebyl nalezen.", "warning")
        return redirect(url_for('login.user_list'))

    user = user[0]  # Předpokládám, že db_execute vrací seznam výsledků, takže první uživatel je na indexu 0

    if request.method == 'POST':
        new_username = request.form['username']
        new_email = request.form['email']
        new_role_id = request.form['role_id']  # Možná chceš, aby administrátor mohl změnit i roli

        update_command = """
            UPDATE users
            SET username = ?, email = ?, role_id = ?
            WHERE id = ?
        """
        db_execute(update_command, (new_username, new_email, new_role_id, user_id))
        flash("Uživatel byl úspěšně upraven.", "message")
        return redirect(url_for('login.user_list'))

    return render_template('edit_user.html', user=user)


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

