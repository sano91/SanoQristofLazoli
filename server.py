from flask import Flask, render_template, redirect, request, url_for, make_response
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

    return render_template('q-and-a.html', data=my_data)


@app.route("/question/<question_id>/new_answer")
def give_answer(id):
    pass


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
