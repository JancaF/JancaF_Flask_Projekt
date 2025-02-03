from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kontakty')
def kontakty():
    return '<h1>Kontakty</h1> <a href="/">Domů</a>'

@app.route('/nasobek/<cislo1>/<cislo2>)')
def cislo(cislo1, cislo2):
    try:
        return f'Násobek je {int(cislo1) * int(cislo2)}'
    except ValueError:
        return 'Neplatné číslo.'
@app.route('/<jmeno>/<prijmeni>')
def uzivatel(jmeno, prijmeni):
    return f'<h2> Vítej {jmeno} {prijmeni}</h2>'
@app.route('/<jmeno>')
def jmeno(jmeno):
    return f'<h2> Vítej {jmeno} </h2>'
if __name__ == '__main__':
    app.run(debug=True)