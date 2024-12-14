from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Login')
@app.route('/Menu')

def home():
    return render_template('Login.html')

def menu():
    return render_template('Menu.html')