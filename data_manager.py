import csv


def open_file(csv_file):
    with open(csv_file, "r") as f:
        opened_file = csv.DictReader(f)
        main_file= []
        for line in opened_file:
            main_file.append(dict(line))

    return main_file

open_file("sample_data/question.csv")