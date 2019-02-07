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




print(get_id_by_title("sample_data/question.csv", "How to make lists in Python?"))


