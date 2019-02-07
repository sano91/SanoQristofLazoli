from flask import Flask, render_template, redirect, request, url_for, make_response
import util
import data_manager
import connection
import csv

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def home():
    header = data_manager.get_headers("sample_data/question.csv")

    table = data_manager.get_data_from_csv("sample_data/question.csv", id=None)
    return render_template("home.html", questions=table, headers=header)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    headers = ['id', 'submission_time', 'view_number', 'title', 'message', 'image']
    if request.method == 'POST':
        with open('sample_data/question.csv', 'a') as questions:
            newquestion = csv.DictWriter(questions, fieldnames=headers)
            newquestion.writerow(
                {'id': '23232', 'submission_time': '1493015438', 'view_number': '0', 'title': request.form['title'],
                 'message': request.form['message']})

        return redirect('/')

    return render_template('add-question.html')


@app.route("/question/<question_id>")
def display_question(id):
    pass


@app.route("/question/<question_id>/new_answer")
def give_answer(id):
    pass


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
