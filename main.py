from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kontakty')
def kontakty():
    return '<h1>Kontakty</h1> <a href="/">Domů</a>'

@app.route('/gallery/')
def gallery():
    return '<h1>Galerie</h1>'
@app.route('/nasobek/<a>/<b>)')
def number(a, b):
    try:
        return f'Násobek je {int(a) * int(b)}'
    except ValueError:
        return 'Neplatné číslo.'
@app.route('/user/<name>/<surname>')
def uzivatel(name, surname):
    return f'<h2> Vítej {name} {surname}</h2>'

@app.route('/<name>')
def username(name):
    return f'<h2> Vítej {name} </h2>'
if __name__ == '__main__':
    app.run(debug=True)