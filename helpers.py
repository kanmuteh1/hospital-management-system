import os
import requests
import urllib.parse
import random

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    # def escape(s):
    #     """
    #     Escape special characters.

    #     https://github.com/jacebrowning/memegen#special-characters
    #     """
    #     for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
    #                      ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
    #         s = s.replace(old, new)
    #     return s
    return render_template("apology.html", top=code, bottom=message), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("name") is None:
            return redirect("/patient-login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"

def carousel(direction,pages):
    if direction == 'next':
        pages = pages + 4
        return pages
    elif direction == 'prev':
        pages = pages - 4
        return pages
    else:
        return 0

def statusCheck(status,choosen_status):
    if choosen_status == status[0]:
        return 0
    elif choosen_status == status[1]:
        return 1
    else:
        return 2

def hospitalNum(x, leading_zeroes=True):
    """Return an X digit number, leading_zeroes returns a string, otherwise int"""
    if not leading_zeroes:
        # wrap with str() for uniform results
        generated_num = random.randint(10**(x-1), 10**x-1)

        if generated_num in hospinal_numbers:
            hospitalNum(x, false)
        else:
            hospinal_numbers.append(generated_num)
            return generated_num
    else:
        if x > 6000:
            generated_num = ''.join([str(random.randint(0, 9)) for i in xrange(x)])

            if generated_num in hospinal_numbers:
                hospinal_numbers.append(generated_num)
                hospitalNum(x)
            else:
                return generated_num
        else:
            generated_num = '{0:0{x}d}'.format(random.randint(0, 10**x-1), x=x)

            if generated_num in hospinal_numbers:
                hospitalNum(x)
            else:
                return generated_num