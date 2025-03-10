from application.db import create_db
from application import app, login
from flask import Flask, render_template
from os import path


app.register_blueprint(login.bp)

if __name__ == '__main__':
    print(app.config["DATABASE"])
    if not path.exists(app.config["DATABASE"]):
        create_db()
        print("Inicializace database")

    app.run(debug=True)


@app.route('/homepage')
def homepage():
    return render_template('index.html')
@app.route('/abeceda/')
def abeceda():
    return render_template('abeceda.html')
@app.route('/alfabeta/')
def alfabeta():
    return render_template('alfabeta.html')


