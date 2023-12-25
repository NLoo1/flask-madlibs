from flask import Flask, request, render_template 
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['KEY'] = "abc123"
debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/story")
def create_story():
    return

