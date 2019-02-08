import csv

'''
def open_question(csv_file):
    with open(csv_file, "r") as f:
        opened_file = f.readlines()
        table = [element.replace("\n", "").split(",") for element in opened_file]

    return table



def write_to_csv(csv_file, data):
    with open(csv_file, "a") as f:
        csv.DictWriter(f, data)
    return None

'''


def get_data_from_csv(csv_file="sample_data/question.csv", id=None):
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        table = []

        for data in reader:
            item = dict(data)

            if id is not None and id == item["id"]:
                return item
            table.append(item)
        return table


def get_headers(csv_file):
    with open(csv_file, "r") as file:
        headers = file.readline()
        header = headers.split(",")
    return header


def get_id_by_title(csv_file, title):
    table = get_data_from_csv(csv_file, id=None)
    for line in table:
        if line['title'] == title:
            return line['id']


answer_id = 2


def create_right_format(message, type, question_id):
    global answer_id
    submission_time = 9876523
    answer_id += 1
    if type == 'answer':
        answer_row = {"id": answers, "submission_time": submission_time, "vote_number": 0, "question_id": question_id,
                      "message": message, "image": 0}
        return answer_row


def write_to_the_file(data, file, type):
    if type == 'question':
        headers_q = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
        with open(file, 'a') as questions:
            newquestion = csv.DictWriter(questions, fieldnames=headers_q)
            newquestion.writerow(data)
    elif type == 'answer':
        headers_a = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
        with open(file, 'a') as questions:
            newquestion = csv.DictWriter(questions, fieldnames=headers_a)
            newquestion.writerow(data)


answers = get_data_from_csv(csv_file="sample_data/answer.csv", id="1")
print(answers)
for key in answers.keys():
    print(answers[key])

print(get_id_by_title("sample_data/question.csv", "How to make lists in Python?"))
