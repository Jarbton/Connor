from flask import Flask, render_template, g
import time


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
