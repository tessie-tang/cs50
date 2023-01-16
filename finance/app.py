import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user_id = session["user_id"]
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    user_cash = user_cash[0]
    stocks = db.execute("SELECT symbol, SUM(shares) as shares, operation FROM stocks WHERE userId = ? GROUP BY symbol HAVING (SUM(shares)) > 0", user_id)
    total_cash = 0
    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["name"] = quote["name"]
        stock["price"] = quote["price"]
        stock["total"] = stock["price"] * stock["shares"]
        total_cash = total_cash + stock["total"]
    total_cash = total_cash + user_cash["cash"]
    return render_template("index.html", stocks=stocks, user_cash=user_cash, total_cash=total_cash)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")

    if request.method == "POST":
        # gather input
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("please provide a symbol", 500)
        symbol = symbol.upper()

        shares = request.form.get("shares")
        if not shares:
            return apology("please provide a share", 500)

        try:
            shares = int(shares)
            if shares < 1:
                return apology("share must be greater than one", 500)
        except ValueError:
            return apology("share must be int", 500)

        price = lookup(symbol)
        if price is None:
            return apology("please provide a valid price", 500)

        user_id = session["user_id"]
        output = db.execute("SELECT cash FROM users WHERE id = ? ", user_id)
        if len(output) < 1:
             return apology("unexpected error", 500)
        user_cash = output[0]["cash"]
        price = price["price"]

        total_price = price * shares
        if user_cash < total_price:
            return apology("insufficient balance", 500)

        # execute order
        db.execute("UPDATE users SET cash = ? WHERE id = ?", user_cash - total_price, user_id)
        db.execute("INSERT INTO stocks (userId, symbol, shares, price, operation) VALUES (?, ?, ?, ?, ?)", user_id, symbol, shares, price, "buy")
        flash("success")
        return redirect("/")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    stocks = db.execute("SELECT * FROM stocks WHERE userId = ?", user_id)
    return render_template("history.html", stocks = stocks)


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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("get_quote.html")

    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("please provide a symbol", 500)

        quote = lookup(symbol)
        if quote is None:
            return apology("must provide valid symbol", 400)

        return render_template("quote.html", name=quote["name"], symbol=quote["symbol"], price=quote["price"])

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return apology("please provide a username", 500)

        password = request.form.get("password")
        if not password:
            return apology("please provide a password", 500)

        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("please provide a password", 500)

        users = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(users) != 0:
            return apology("username exists", 500)

        if not password == confirmation:
            return apology("passwords should match", 500)

        hash = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?) ", username, hash)
        return redirect("/")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]
    if request.method  == "GET":
        stocks = db.execute("SELECT symbol FROM stocks WHERE userId = ? GROUP BY symbol", user_id)
        return render_template("sell.html", stocks=stocks)

    if request.method == "POST":
        symbol = request.form.get("symbol")
        symbol = symbol.upper()
        if not symbol:
            return apology("please provide a symbol", 500)

        shares = request.form.get("shares")
        if not shares:
            return apology("please provide a shares", 500)

        try:
            shares = int(shares)
            if shares < 1:
                return apology("share must be greater than one", 500)
        except ValueError:
            return apology("share must be int", 500)

        stocks = db.execute("SELECT SUM(shares) as shares FROM stocks WHERE userId = ? AND symbol = ?;", user_id, symbol)[0]
        if shares > stocks["shares"]:
            return apology("you don't have any shares")

        price = lookup(symbol)
        price = price["price"]
        total_value = price * shares

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_value, user_id)
        db.execute("INSERT INTO stocks (userId, symbol, shares, price, operation) VALUES (?, ?, ?, ?, ?)", user_id, symbol, -shares, price, "sell")
        flash("sold")
        return redirect("/")