
from flask import Flask, render_template, redirect, request, url_for, make_response
import util
import data_manager
import connection

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def home():
    headers = ["Date", "Title", "Question", "Show"]
    table = {"SFG", "2018-10-11 13:12", "Title", "Question", "Watch"}

    return render_template("home.html", table=table, headers=headers)


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
        port=6000,
        debug=True,
    )