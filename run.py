from flask import Flask, render_template, request, jsonify, url_for, session
from flask.ext.session import Session
import aiml
import os.path
import sqlite3

app = Flask(__name__)
# Check Configuration section for more details
app.config.from_object(__name__)
Session(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/ask", methods=['POST','GET'])
def ask():

    # Initiate connection with database
    with sqlite3.connect(r"C:\Users\jbart\OneDrive\Documents\GitHub\Connor\db\connor.db") as conn:
        c = conn.cursor()

    # Prepare kernel
    kernel = aiml.Kernel()
    if os.path.isfile("connor_brain.brn"):
	    kernel.bootstrap(brainFile = "connor_brain.brn")
    else:
	    kernel.bootstrap(learnFiles = os.path.abspath("aiml/start.xml"), commands = "load aiml b")
	    kernel.saveBrain("connor_brain.brn")

    # Get response from HTML/JS
    bot_response = kernel.respond(str(request.form['chatmessage']))

    # Get variables and test by printing
    session['colour'] = kernel.getPredicate("colour")
    session['model'] = kernel.getPredicate("model")
    print session['colour']
    print session['model']

    # Query database and test by printing
    # TODO: create concat string from session loop
    c.execute("SELECT * FROM CarTable WHERE Colour =  AND Model = '%s'")
    results = c.fetchall()
    print results

    # Return response
    return jsonify({'status':'OK','answer':"bot_response"})

@app.route("/shop")
def shop():
    return render_template("search.html", )

if __name__ == "__main__":
    app.run()

class Dealer:
    firstname = None
    lastname = None
    streetName = None
    houseNameNumber = None
    city = None
    postcode = None
    email = None
    contactNumber = None

class SParameter:
    make = None
    model = None
    variant = None
    price = None
    year = None
    colour = None
    mileage = None
    seats = None
    doors = None
    body = None
    engine = None
    gearbox = None
    drivetrain = None
    fuel = None
    insurance = None
    consumption = None
    tax = None
    acceleration = None
    emissions = None
