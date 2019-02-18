from flask import Flask, render_template, redirect, request
import util
import data_manager
import connection
import csv
from datetime import datetime

app = Flask(__name__)

generated_ids = []

@app.route('/')
@app.route('/list')
def home():
    header = data_manager.get_headers("sample_data/question.csv")
    header = header[1:5]
    table = data_manager.get_data_from_csv("sample_data/question.csv", id=None)
    return render_template("home.html", questions=table, headers=header)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    headers = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
    if request.method == 'POST':
        with open('sample_data/question.csv', 'a') as questions:
            newquestion = csv.DictWriter(questions, fieldnames=headers)
            newquestion.writerow(
                {'id': util.generate_random(generated_ids), 'submission_time': 'Couldnt do',
                 'view_number': '0', 'vote_number': '0',
                 'title': request.form['title'],
                 'message': request.form['message']})

        return redirect('/')

    return render_template('add-question.html')


@app.route("/question/<question_id>")
def display_question(question_id):
    my_data = data_manager.get_data_from_csv(csv_file="sample_data/question.csv", id=question_id)
    question_header = data_manager.get_headers("sample_data/question.csv")
    answers = data_manager.get_data_from_csv(csv_file="sample_data/answer.csv", id=question_id)
    answers_headers = data_manager.get_headers("sample_data/answer.csv")

    return render_template('q-and-a.html', question=my_data, questionheader=question_header, answer=answers,
                           answerheader=answers_headers)


@app.route("/question/<id>/new-answer", methods=["GET", "POST"])
def give_answer(id):
    if request.method == "POST":

        answer_message = request.form["message"]
        new_answer = data_manager.create_right_format(id, answer_message, "answer")
        data_manager.write_to_the_file(new_answer, "sample_data/answer.csv", "answer")
        return redirect("/")
    return render_template("answer.html")


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
