from flask import Flask, render_template
from application import app, login
from application.db import create_db
from os import path

app.register_blueprint(login.bp)

if __name__ == '__main__':
    print(app.config["DATABASE"])
    if not path.exists(app.config["DATABASE"]):
        print("Inicializace database")
        create_db()


    app.run(debug=True)

@app.route('/homepage')
def homepage():
    return render_template('index.html')