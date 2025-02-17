from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')
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
@app.route('/nasobek/')
def nasobek():
    return '<h1>Nasobek</h1> <a href="/">Domů</a>'
@app.route('/nasobek/<a>/<b>)')
def number(a, b):
    try:
        return f'Násobek je {int(a) * int(b)}'
    except ValueError:
        return 'Neplatné číslo.'
@app.route('/user/<name>/<surname>')
def uzivatel(name, surname):
    return f'<h2> Vítej {name} {surname}</h2>'
@app.route('/odkaz', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        radio = request.form['radio']
        return render_template('zkouska.html', user=user, password=password, radio=radio)
    return render_template('link.html')
@app.route('/<name>')
def username(name):
    return f'<h2> Vítej {name} </h2>'

if __name__ == '__main__':
    app.run(debug=True)