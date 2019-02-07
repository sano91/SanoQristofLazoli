from flask import Flask, render_template, redirect, request, url_for, make_response
import util
import data_manager
import connection

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def home():
    header = data_manager.get_headers("sample_data/question.csv")

    table = data_manager.get_data_from_csv("sample_data/question.csv", id=None)
    return render_template("home.html", questions=table, headers=header)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    pass


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
