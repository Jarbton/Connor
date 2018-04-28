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

    # Get variables
    session['make'] = kernel.getPredicate("make")
    session['model'] = kernel.getPredicate("model")
    session['variant'] = kernel.getPredicate("variant")
    session['price'] = kernel.getPredicate("price")
    session['year'] = kernel.getPredicate("year")
    session['colour'] = kernel.getPredicate("colour")
    session['mileage'] = kernel.getPredicate("mileage")
    session['seats'] = kernel.getPredicate("seats")
    session['doors'] = kernel.getPredicate("doors")
    session['body'] = kernel.getPredicate("body")
    session['engine'] = kernel.getPredicate("engine")
    session['gearbox'] = kernel.getPredicate("gearbox")
    session['drivetrain'] = kernel.getPredicate("drivetrain")
    session['fuel'] = kernel.getPredicate("fuel")
    session['insurance'] = kernel.getPredicate("insurance")
    session['consumption'] = kernel.getPredicate("consumption")
    session['tax'] = kernel.getPredicate("tax")
    session['acceleration'] = kernel.getPredicate("acceleration")
    session['emissions'] = kernel.getPredicate("emissions")

    # Format the query from the users inputs
    sQuery = "SELECT * FROM cars WHERE make = ehaeh"
    for k, v in user_input.iteritems():
    	if v:
    		sQuery += " AND %s = %s" % (k, v)
    print sQuery

    # Query the database
    c.execute(sQuery)
    results = c.fetchall()
    print results

    #Load results if typed 'search'
    if request.form['chatmessage'] == "search"
        results_cars = []
        for result in results:
        	results_cars.append(car(result))
        return render_template("search.html", results_cars)

    # Return response
    return jsonify({'status':'OK','answer':"bot_response"})

@app.route("/shop")
def shop():
    return render_template("search.html", )

if __name__ == "__main__":
    app.run()

## TODO: Create dealer stuff

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
