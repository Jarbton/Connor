from flask import Flask, render_template, request, jsonify, url_for
import aiml
import os.path
import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/ask", methods=['POST','GET'])
def ask():
    # Initiate connection with database
    with sqlite3.connect(r"C:\Users\Dave\Desktop\connor.db") as conn:
        c = conn.cursor()

    # Preper kernel
    kernel = aiml.Kernel()

    if os.path.isfile("connor_brain.brn"):
	    kernel.bootstrap(brainFile = "connor_brain.brn")
    else:
	    kernel.bootstrap(learnFiles = os.path.abspath("aiml/start.xml"), commands = "load aiml")
	    kernel.saveBrain("connor_brain.brn")
    
    # Get response from HTML/JS
    bot_response = kernel.respond(str(request.form['chatmessage']))
    
    # Get variables and test by printing
    colour = kernel.getPredicate("colour")
    model = kernel.getPredicate("model")
    print colour
    print model

    # Query databse and test by printing
    c.execute("SELECT Make, Price FROM CarTable WHERE Colour = '%s' AND Model = '%s'" % (colour, model))
    results = c.fetchall()
    print results

    # Return response
    return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run()