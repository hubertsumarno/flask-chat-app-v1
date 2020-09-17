from flask import Flask, render_template, request, redirect
from cs50 import SQL

# Configure application
app = Flask(__name__)

# Configure database
db = SQL("sqlite:///chat.db")

@app.route("/")
def index():
    rows = db.execute("SELECT * FROM messages")
    return render_template("index.html", rows = rows)

@app.route("/send", methods = ["GET", "POST"])
def send():
    if request.method == "GET":
        return render_template("send.html")
    else:
        message = request.form.get("message")
        name = request.form.get("name")

        # Check if message and name is entered
        if not message:
            return render_template("apology.html", message = "Please provide a message.")
        elif not name:
            return render_template("apology.html", message = "Please provide a name.")

        # Insert message into database
        db.execute("INSERT INTO messages (message, name) VALUES (:message, :name)", message = message, name = name)

        # Redirect user to chat room
        return redirect("/")