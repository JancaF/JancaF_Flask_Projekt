from flask import Flask, render_template
from app import app, login

app.register_blueprint(login.bp)

@app.route('/homepage')
def homepage():
    return render_template('index.html')
@app.route('/abeceda/')
def abeceda():
    return render_template('abeceda.html')
@app.route('/alfabeta/')
def alfabeta():
    return render_template('alfabeta.html')
@app.route('/hebrejstina/')
def hebrejstina():
    return render_template('hebrej.html')
@app.route('/kontakty')
def kontakty():
    return '<h1>Kontakty</h1> <a href="/">Domů</a>'
@app.route('/gallery/')
def gallery():
    return '<h1>Galerie</h1> <a href="/">Domů</a>'

if __name__ == '__main__':
    app.run(debug=True)