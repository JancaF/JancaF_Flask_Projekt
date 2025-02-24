from flask import Flask, render_template, request, flash, redirect, url_for, session
app = Flask(__name__)
app.config['SECRET_KEY'] = "dev"
@app.route('/')
def index():
    return render_template('base.html')
@app.route('/homepage')
def homepage():
    return render_template('index.html')
@app.route('/odkaz', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        if request.form["username"] == "pokuston" and request.form["password"] == "heslo":
            flash("Login successful", "message")
            return redirect(url_for('index'))
        flash("Login failed", "warning")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)