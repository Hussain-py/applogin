from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

# @app.route('/', methods=['POST', 'GET'])
# def home():
#     if request.method=='POST':
#         username = request.form['username']
#         password = request.form['password']
#         dbHandler.insertUser(username, password)
#         users = dbHandler.retrieveUsers()
#         return render_template('profile.html', users=users)
#     else:
#         return render_template('index.html')

from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
app.secret_key = "super secret key"
@app.route("/", methods =["GET","POST"])
def login():
    r = ""
    msg = ""
    if(request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = '"+username+"' and password = '"+password+"' ")
        r=c.fetchall()
        print(r)
        for i in r:
            if (username == i[1] and password==i[2]):
                session["logedin"] = True
                session["username"] = username
                return redirect(url_for("profile"))
            else:
                msg = "please enter valid username and password"
    return render_template("index.html", msg=msg)

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=False)
