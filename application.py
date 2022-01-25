import os
import json
import random

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, jsonify,  session, make_response
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, carousel, statusCheck

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

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///health-care.db")

@app.route("/")
def index():
    return render_template('index.html')
    
# Log patient in       
@app.route("/patient-login", methods=["GET", "POST"])
def patient_login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure patient name was submitted
        if not request.form.get("name"):
            return apology("must provide Name", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for patient name
        rows = db.execute("SELECT * FROM patients WHERE patient_name = ?", request.form.get("name"))

        # Ensure patient name exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password_hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["name"] = rows[0]["patient_name"]

        # Redirect patient to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("patient-login.html")

# Log facility in 
@app.route("/facility-login", methods=["GET", "POST"])
def facility_login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure facility name was submitted
        if not request.form.get("name"):
            return apology("must provide Facility Name", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for facility name
        rows = db.execute("SELECT * FROM facilities WHERE facility_name = ?", request.form.get("name"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password_hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)


        # Remember which facility has logged in
        session["name"] = rows[0]["facility_name"]

        # Redirect facility to home page
        return render_template("./facility-dashboard/index.html",data=rows)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("facility-login.html")

@app.route("/facility-carousel")
def carousel():
    data = db.execute("SELECT facility_id, facility_name, facility_address FROM facilities")
    return render_template('carousel-facility.html',data=data)

@app.route("/facilities", methods=["GET", "POST"])
def ficility():
    if request.method == "POST":
        session.clear()
        facility_name = request.form.get("name")
        head_doc = request.form.get("head-doc")
        email = request.form.get("email")
        address = request.form.get("address")
        orange_num = request.form.get("orange-num")
        lonestar_num = request.form.get("lonestar-num")
        founding_date = request.form.get("founding-date")
        impact = request.form.get("impact")
        history = request.form.get("history")
        password = request.form.get("password")
        confirmation = request.form.get("c-password")
        if not facility_name:
            return apology("Please provide Facility name", 400)
        elif not head_doc:
            return apology("Please provide Chief Medical Officier name", 400)
        elif not email:
            return apology("Please provide Email", 400)
        elif not address:
            return apology("Please provide Address", 400)
        elif not lonestar_num:
            return apology("Please provide Lonestar number", 400)
        elif not founding_date:
            return apology("Please provide Founding date", 400) 
        elif not impact:
            return apology("Please provide text of impact", 400) 
        elif not history:
            return apology("Please provide a brief history", 400)  
        elif not password or not confirmation:
            return apology("Sorry, password is empty", 400)
        # If keys are different render an anumberpology
        elif password != confirmation:
            return apology("Sorry, passwords do not match", 400)

        # hash password before storing it.
        key = generate_password_hash(confirmation, method='pbkdf2:sha256', salt_length=8)

        # # Checking if facility name exists in the database
        rows = db.execute("SELECT * FROM facilities WHERE facility_name = ?", facility_name)
        if len(rows) != 1:
            # Include register into our database
            db.execute("INSERT INTO facilities (facility_name, facility_address, funding_date, head_doctor, impact, history, email, orang_number,lonestar_number, password_hash) VALUES(?,?,?,?,?,?,?,?,?,?)", facility_name, address, founding_date, head_doc, impact, history, email, orange_num, lonestar_num, key)

            rows = db.execute("SELECT * FROM facilities WHERE facility_name = ?", facility_name)

            session["name"] = rows[0]["facility_name"]

            return render_template("./facility-dashboard/index.html",data=rows)

        else:
            return apology("Sorry, username already exists", 400)
    else:
        rows = db.execute("SELECT * FROM facilities WHERE facility_name = ?", request.args.get("name"))
        return render_template("facility.html",data=rows)

@app.route("/patients", methods=["GET", "POST"])
def create_patient():
    if request.method == "POST":
        session.clear()
        patient_name = request.form.get("name")
        email = request.form.get("email")
        address = request.form.get("address")
        orange_num = request.form.get("orange-num")
        lonestar_num = request.form.get("lonestar-num")
        date_of_birth = request.form.get("dob")
        password = request.form.get("password")
        confirmation = request.form.get("c-password")

        if not patient_name:
            return apology("Please provide Chief Medical Officier name", 400)
        elif not email:
            return apology("Please provide Email", 400)
        elif not address:
            return apology("Please provide Address", 400)
        elif not orange_num:
            return apology("Please provide Orange number", 400)
        elif not lonestar_num:
            return apology("Please provide Lonestar number", 400)
        elif not date_of_birth:
            return apology("Please provide your Date Of Birth", 400)  
        elif not password or not confirmation:
            return apology("Sorry, password is empty", 400)
        # If keys are different render an anumberpology
        elif password != confirmation:
            return apology("Sorry, passwords do not match", 400)

        # hash password before storing it.
        key = generate_password_hash(confirmation, method='pbkdf2:sha256', salt_length=8)

        # # Checking if facility name exists in the database
        rows = db.execute("SELECT * FROM patients WHERE patient_name = ?", patient_name)
        if len(rows) != 1:
            # Include register into our database
            db.execute("INSERT INTO patients (patient_name, patient_address, date_of_birth, email, orang_number,lonestar_number, password_hash) VALUES(?,?,?,?,?,?,?)", patient_name, address, date_of_birth, email, orange_num, lonestar_num, key)

            # Query database for username
            rows = db.execute("SELECT * FROM patients WHERE patient_name = ?", patient_name)

            # Remember which user has logged in
            session["name"] = rows[0]["patient_name"]
            # Redirect user to home page
            return redirect("/")
            # return render_template("./patient-dashboard/index.html",data=rows)

        else:
            return apology("Sorry, username already exists", 400)
    else:
        # # Query database for username
        return "TODO"

# log user out
@app.route("/logout")
def logout():
    # Forget any user_id
    session.clear()

    # Redirect user to landing page
    return redirect("/")

@app.route("/registration", methods=["GET", "POST"])
def register():
    # registration status 
    status = ['Patient', 'Health Facility']
    choosen_status = request.args.get('status')
    
    if request.method == "POST":
        patient_name = session.get("name")
        facility_name = request.args.get("facility_name")
        account_number = request.form.get("number")
        account_pin = request.form.get("password")
        # generate health-facility number
        hospital_num = '{0:0{x}d}'.format(random.randint(0, 10**12-1), x=12)
        # If user does not have an account or is not login
        if patient_name is None:
            return redirect("/patient-login")
        else: 
            # If user has an account or is login
            patient_id = db.execute("SELECT patient_id FROM patients WHERE patient_name = ?", patient_name)
            facility_id = db.execute("SELECT facility_id FROM facilities WHERE facility_name = ?", facility_name)
            data = db.execute("SELECT * FROM registration WHERE facility_id = ? AND patient_id = ?",facility_id[0]["facility_id"], patient_id[0]["patient_id"])
            if len(data) < 1:
                db.execute("INSERT INTO registration  (facility_id, patient_id,account_num, account_pin, facility_assign_num,registration_date) VALUES(?,?,?,?,?,datetime('now'))", facility_id[0]["facility_id"], patient_id[0]["patient_id"], account_number, account_pin, hospital_num)
                return redirect(f"/facilities?name={facility_name}")
            else:
                data = db.execute("SELECT * FROM registration WHERE facility_id = ? AND patient_id = ?",facility_id[0]["facility_id"], patient_id[0]["patient_id"])
                db.execute("INSERT INTO registration  (facility_id, patient_id,account_num, account_pin, facility_assign_num,registration_date) VALUES(?,?,?,?,?,datetime('now'))", facility_id[0]["facility_id"], patient_id[0]["patient_id"], account_number, account_pin, data[0]["facility_assign_num"])
                return redirect(f"/facilities?name={facility_name}")

    status_value = statusCheck(status,choosen_status)
    if status_value == 0:
        return render_template('patient-register.html')
    elif status_value == 1:
        return render_template('facility-register.html')
    else:
        return redirect("/")

@app.route("/dashboards")
def display_dashboard():
    client_name = session.get("name")
    facility_data = db.execute("SELECT * FROM facilities WHERE facility_name = ? ", client_name)
    patient_data = db.execute("SELECT * FROM patients WHERE patient_name = ? ", client_name)
    if len(facility_data) != 1:
        return render_template('./patient-dashboard/index.html',data=patient_data)
    elif len(patient_data) != 1:
        return render_template('./facility-dashboard/index.html',data=facility_data)

@app.route("/services", methods=["GET", "POST"])
def service():
    if request.method == "POST":
        facility_name = session.get("name")
        service = request.form.get("service")
        about_service = request.form.get("service-discription")
        if not service:
            return apology("Please provide Service", 400)
        elif not about_service:
            return apology("Please provide Text that discribes Servise", 400)
        else:
            facility_id = db.execute("SELECT facility_id FROM facilities WHERE facility_name = ?", facility_name)
            db.execute("INSERT INTO services  (facility_id,facility_service,about_service) VALUES(?,?,?)", facility_id[0]["facility_id"],service,about_service)
            return redirect('/dashboards')
    return render_template('./facility-dashboard/service.html')

@app.route("/services-view", methods=["GET", "POST"])
def serviceView():
    facility_name = request.args.get("facility_name")
    if facility_name[0] == "[":
        return apology("No such facility", 404)
    facility_id = db.execute("SELECT facility_id FROM facilities WHERE facility_name = ?", facility_name)
    data = db.execute("SELECT * FROM services WHERE facility_id = ?", facility_id[0]["facility_id"])
    return render_template('service-view.html',data=data)

@app.route("/hospitals", methods=["GET", "POST"])
def viewHospitals():
    patient = session["name"]
    ID = db.execute("SELECT patient_id FROM patients WHERE  patient_name = ?",patient)
    data = db.execute("SELECT DISTINCT facility_name, facility_assign_num FROM registration INNER JOIN facilities ON facilities.facility_id = registration.facility_id WHERE patient_id = ?",ID[0]["patient_id"])
    return render_template('./patient-dashboard/hospital.html',data=data)

@app.route("/diagnosis", methods=["GET", "POST"])
def diagnose():
    return "TODO"

@app.route("/treatments", methods=["GET", "POST"])
def treatment():
    return "TODO"