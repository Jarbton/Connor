from flask import Flask, render_template, g
import time


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/home_form', methods=['GET'])
def home_form():
    return render_template('home.html', methods=['GET'])

@app.route('/four_form')
def four_form():
    return render_template('4x4.html', methods=['GET'])

@app.route('/saloon_form')
def saloon_form():
    return render_template('Saloon.html', methods=['GET'])

@app.route('/hatchback_form')
def hatchback_form():
    return render_template('Hatchback.html', methods=['GET'])

@app.route('/convertible_form')
def convertible_form():
    return render_template('Convertible.html', methods=['GET'])

@app.route('/estate_form')
def estate_form():
    return render_template('Estate.html', methods=['GET'])

@app.route('/coupe_form')
def coupe_form():
    return render_template('Coupe.html', methods=['GET'])

@app.route('/contact_form')
def contact_form():
    return render_template('Contact.html', methods=['GET'])

@app.route('/login_form')
def login_form():
    return render_template('login.html', methods=['GET'])

@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
