import csv


def open_question(csv_file):
    with open(csv_file, "r") as f:
        opened_file = f.read()
        opened_file = opened_file.split('\n')


        for lines in opened_file:
            print(lines)

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


d = get_data_from_csv("sample_data/question.csv", id=None)
print(d[1]["vote_number"])


def get_headers(csv_file):
    with open(csv_file, "r") as file:
        headers = file.readline()
        header = headers.split(",")
    return header[1:5]

print(get_headers("sample_data/question.csv"))










