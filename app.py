from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import personality_quiz, satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def home_page():
    return render_template("home.html", personality_Title=personality_quiz.title, personality_Intructions=personality_quiz.instructions, satisfaction_Title=satisfaction_survey.title, satisfaction_Instructions=satisfaction_survey.instructions)

@app.route('/personality')
def show_survey():
    return render_template("personality.html")
    
@app.route('/satisfaction')
def satisfaction_text():
    return render_template("satisfaction.html")

#Route for satisfaction questions
@app.route("/satisfaction/<question>/0")
def satisfactions_questions(question):
    print(satisfaction_survey.questions)
    return render_template("satisfaction_questions.html", question=satisfaction_survey.questions)
