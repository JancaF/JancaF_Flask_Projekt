from flask import Flask, render_template, session
from application import app, login
from application.db import create_db
from os import path

app.register_blueprint(login.bp)
app.secret_key = "dev"

if __name__ == '__main__':

    if not path.exists(app.config["DATABASE"]):
        print("Inicializace database")
        create_db()


    app.run(debug=True)

@app.route('/homepage')
def homepage():
    return render_template('index.html')
