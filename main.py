from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1> <a href="/kontakty">Kontakty</a>'

@app.route('/kontakty')
def kontakty():
    return '<h1>Kontakty</h1> <a href="/">Domů</a>'

if __name__ == '__main__':
    app.run(debug=True)