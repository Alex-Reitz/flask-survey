from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import personality_quiz, satisfaction_survey



app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def home_page():
    return render_template("home.html", personality_Title=personality_quiz.title, personality_Intructions=personality_quiz.instructions, 
    satisfaction_Title=satisfaction_survey.title, satisfaction_Instructions=satisfaction_survey.instructions)

@app.route('/personality')
def show_survey():
    return render_template("personality.html", personality_Title=personality_quiz.title)
    
@app.route('/satisfaction')
def satisfaction_text():
    return render_template("satisfaction.html", satisfaction_Title=satisfaction_survey.title)

#Route for satisfaction questions
@app.route("/satisfaction_questions/question/<int:index>")
def satisfactions_questions(index):
    question = satisfaction_survey.questions[index].question.self
    return render_template("satisfaction_questions.html", question=question)


@app.route("/add-response", methods=["POST"])
def add_response():
    response = request.form("name")
    responses.append(response)
    index = responses.length




