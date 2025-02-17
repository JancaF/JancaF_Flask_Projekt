from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')
@app.route('/homepage')
def homepage():
    return render_template('index.html')
@app.route('/obchod')
def obchod():
    return render_template('shop.html')
@app.route('/odkaz', methods=['GET', 'POST'])
def link(user='pokuston', password='heslo'):
    if request.method == 'POST':
        return render_template('login.html', user=user, password=password)
    return render_template('link.html')
@app.route('/<name>')
def username(name):
    return f'<h2> Vítej {name} </h2>'

if __name__ == '__main__':
    app.run(debug=True)