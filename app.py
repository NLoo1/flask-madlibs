from flask import Flask, request, render_template 
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "abc123"
debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/story")
def create_story():
    # print(request.args)
    p = request.args["place"]
    n = request.args["noun"]
    v = request.args["verb"]
    a = request.args["adjective"]
    plural = request.args["plural_noun"]
    # return request.args
    return render_template("story.html", place=p, noun=n,verb=v,adjective=a, plural_noun=plural)

