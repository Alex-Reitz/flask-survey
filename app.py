from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route('/personality')
def show_survey(survey):
    personality = surveys.personality_quiz
    return render_template("personality.html", personality=personality)
    