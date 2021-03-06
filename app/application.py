import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash


from helpers import apology, login_required, time_convert

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["time_convert"] = time_convert

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
db = SQL("sqlite:///timer.db")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Record timer session"""
    
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # record the users timer session title and description into database
        db.execute("INSERT INTO history1 (user_id, description, title, session_length) VALUES(:user_id, :description, :title, :session_length)",
                   description=request.form.get("description"), session_length=request.form.get("set_time"), title=request.form.get("title"), user_id=session["user_id"])
        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("index.html")
    

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    """Show dashboard of logged time intervals"""
    
    # retrieve data to display on the dashboard. Store as dictionary in variable.
    data_log = db.execute("SELECT SUM(session_length) total_min, title, description, start_time, session_length, COUNT(interval_id) intervals FROM history1 WHERE user_id = :user_id GROUP BY interval_id", 
                          user_id=session["user_id"])
    # retrieve total pomodoro sessions and total time of intervals. 
    totals = db.execute("SELECT SUM(session_length) total_min, COUNT(interval_id) intervals FROM history1 WHERE user_id = :user_id", 
                        user_id=session["user_id"])
    # render dashboard.html sending data_log dictionary data to be inserted into html table
    return render_template("dashboard.html",  data_log=data_log, minutes=totals[0]["total_min"], intervals=totals[0]["intervals"])   


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)
        
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        
        # check if user entered confirmation 
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)
       
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        
        # Check if password matches the confirmation field
        if password != confirmation:
            return apology("must match passwords", 400)
        
        # Hash user password
        encrypt = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        
        # Check if username already exists
        result = db.execute("SELECT * FROM users WHERE username = :username", 
                            username=request.form.get("username"))
        if not result:
            # Inset username and password into table
            insert = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
                                username=request.form.get("username"), hash=encrypt)
            # Remember which user has logged in
            session["user_id"] = insert
            # Redirect user to home page
            return redirect("/")
        else:
            return apology("username taken", 400)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
