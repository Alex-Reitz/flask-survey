from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question, Survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route('/user/<survey>')
def show_survey(survey):
    print(surveys)
    name = surveys
    survey = surveys[name]
    return f"{{survey}}"
    