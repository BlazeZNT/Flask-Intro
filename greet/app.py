from flask import Flask
app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "<h1>welcome home</h1>"

@app.route("/welcome/home")
def welcomehome():
    return "welcome home"

@app.route("/welcome/back")
def welcomeback():
    return "welcome back"



    