import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///health-care.db")

@app.route("/")
def index():
    data = db.execute("SELECT * FROM facilities")
    return render_template("index.html", data=data)

@app.route("/facilities", methods=["GET", "POST"])
def ficility():
    if request.method == "POST":
        return "TODO"
    name = request.args.get("name") 
    facility_data = db.execute("SELECT * FROM facilities WHERE facility_name=?",name)
    return render_template("facility.html",data=facility_data)
     

@app.route("/patients", methods=["GET", "POST"])
def create_patient():
    return apology("TODO")
