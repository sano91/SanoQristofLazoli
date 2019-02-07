import csv


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















