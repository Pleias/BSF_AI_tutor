import os
from flask import Flask, render_template, request, redirect, url_for, flash, render_template_string
from end_point_sripts import correct_text
import sys

app = Flask(__name__)

app.secret_key = "b9f1a3d5c3e47f5a94e7b6b8a3c1d6e8"

def sanitize_text(text):
    return text.strip().replace('\n', ' ').replace('\r', ' ')

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", 
                         essay_text="", 
                         essay_question="Quel animal de la nature vous fascine le plus et pourquoi ?",
                         error_analysis="")

@app.route("/submit", methods=['POST'])
def submit():
    essay_question = request.form.get("questionInput") 
    essay_input = request.form.get("essayInput")
    question = sanitize_text(essay_question)
    answer = sanitize_text(essay_input)
    error_analysis = correct_text(question=question, answer=answer) 
    # print("question: ", essay_question, "\n", file = sys.stderr)
    # print("essay: ", essay_input, "\n", file = sys.stderr)
    # print("analysis: ", error_analysis, "\n", file = sys.stderr)
    return render_template("index.html", 
                         essay_question=essay_question,
                         essay_text=essay_input, 
                         error_analysis=error_analysis)

@app.route("/analyze", methods=['POST'])
def api_analyze():
    essay_input = request.form.get("essayInput")
    essay_question = request.form.get("questionInput")
    
    question = sanitize_text(essay_question)
    answer = sanitize_text(essay_input)
    
    analysis = correct_text(question=question, answer=answer)
    
    return {"analysis": analysis}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=True)