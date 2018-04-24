from flask import Flask, render_template, g
import time

app = Flask(__name__)

# Render index page
@app.route('/')
def main():
    return render_template('index.html')

@app.route("/ask", methods=['POST','GET'])
def ask():
	# Gather input
	message = str(request.form['chatmessage'])

	kernel = aiml.Kernel()

	# Ready kernel
	if os.path.isfile("connor_brain.brn"):
	    kernel.bootstrap(brainFile = "connor_brain.brn")
	else:
	    kernel.bootstrap(learnFiles = os.path.abspath("aiml/start.xml"), commands = "load aiml")
	    kernel.saveBrain("connor_brain.brn")

	# Get and return response
	while True:
	    if message == "quit":
	        exit()
	    elif message == "save":
	        kernel.saveBrain("connor_brain.brn")
	    else:
	        bot_response = kernel.respond(message)
	        return jsonify({'status':'OK','answer':bot_response})
            
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
