from flask import Flask, render_template, request, jsonify, url_for
import aiml
import os.path
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST','GET'])
def ask():
    with sqlite3.connect(r"C:\Users\Dave\Desktop\connor.db") as conn:
        c = conn.cursor()

    kernel = aiml.Kernel()

    if os.path.isfile("bot_brain.brn"):
	    kernel.bootstrap(brainFile = "bot_brain.brn")
    else:
	    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
	    kernel.saveBrain("bot_brain.brn")
    
    bot_response = kernel.respond(str(request.form['chatmessage']))
    
    colour = kernel.getPredicate("colour")
    model = kernel.getPredicate("model")
    print colour
    print model

    c.execute("SELECT Make, Price FROM CarTable WHERE Colour = '%s' AND Model = '%s'" % (colour, model))
    results = c.fetchall()

    print results

    # print bot_response
    return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run()