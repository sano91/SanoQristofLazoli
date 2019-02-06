import csv


def open_question(csv_file):
    with open(csv_file, "r") as f:
        opened_file = f.read()
        opened_file = opened_file.split('\n')

        for lines in opened_file:
            print(lines)



open_question("sample_data/answer.csv")