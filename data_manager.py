import csv
from datetime import datetime
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
def get_data_from_csv(csv_file, id=None):
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        table = []
        selected_question = []
        for data in reader:
            item = dict(data)
            if id is not None and id == item["id"]:
                selected_question.append(item)
            table.append(item)
        if len(selected_question) > 0:
            return selected_question
        else:
            return table

def convert_time(time):
    normal_time = datetime.fromtimestamp(time)
    return normal_time


def get_headers(csv_file):
    with open(csv_file, "r") as file:
        headers = file.readline()
        header = headers.split(",")
    return header[1:5]


def get_id_by_title(csv_file, title):
    table = get_data_from_csv(csv_file, id=None)
    for line in table:
        if line['title'] == title:
            return line['id']


