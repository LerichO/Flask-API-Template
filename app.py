# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
import model
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

# add route for your gif results
@app.route("/yourgif", methods=["GET", "POST"])
def yourgif():
    # get the giph for giphy and puts the link on webpage
    user_response = request.form["gifchoice"]
    gifLink = getImageUrlFrom(user_response)
    print(gifLink)
    # pass URL to render_template and have that URL appear as an image in yourgif.html
    return render_template("yourgif.html", time = datetime.now(), gifLink = gifLink)
    # time = datetime.now forces css to refresh in real time with any changes
