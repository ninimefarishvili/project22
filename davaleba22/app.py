from flask import Flask, session, render_template, redirect, url_for, request
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "nkwhook1818"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        name = request.form["name"]
        session["name"] = name

        lastname = request.form["lastname"]
        session["lastname"] = lastname

        username = request.form["username"]
        session["username"] = username

        email = request.form["email"]
        session["email"] = email

        inputPassword = request.form["inputPassword"]
        session["inputPassword"] = inputPassword

        return redirect(url_for("home"))

    return render_template("Login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)