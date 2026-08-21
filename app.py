from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect('/index')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')

#executar aplicacao

if __name__ == '__main__' :
    app.run(debug=True)