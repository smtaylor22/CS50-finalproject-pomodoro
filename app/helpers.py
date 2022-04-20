from flask import redirect, render_template, request, session
from functools import wraps
import time


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


# convert time to 12 hr time 
# https://stackoverflow.com/questions/13855111/how-can-i-convert-24-hour-time-to-12-hour-time
def time_convert(s):
    """test"""
    t = time.strptime(s, "%H:%M:%S")
    timevalue_12hour = time.strftime("%I:%M:%S %p", t)
    return timevalue_12hour