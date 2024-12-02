import os
from flask import Flask, render_template, request, redirect, url_for, flash, render_template_string
from end_point_sripts import correct_text

app = Flask(__name__)

app.secret_key = "b9f1a3d5c3e47f5a94e7b6b8a3c1d6e8"

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
    error_analysis = correct_text(question=essay_question, answer=essay_input) 
    # print("question: ", essay_question, "\n", file = sys.stderr)
    # print("essay: ", essay_input, "\n", file = sys.stderr)
    # print("analysis: ", error_analysis, "\n", file = sys.stderr)
    return render_template("index.html", 
                         essay_question=essay_question,
                         essay_text=essay_input, 
                         error_analysis=error_analysis)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=True)