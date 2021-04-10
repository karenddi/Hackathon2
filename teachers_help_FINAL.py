import pandas

def csv_reader(file):

    data = pandas.read_csv(file, sep=";")
    print(data)
    return data


def open_file(file):
    with open(file,  encoding="utf-8") as file_opened:
        lines = file_opened.readlines()
        return lines

def data_imported(data):

    names = data.name.tolist()
    surnames = data.surname.tolist()
    tasks_missing = data.tasks_missing.tolist()
    grade = data.grade.tolist()

    dict_data = {"names": names,
                 "surnames": surnames,
                 "tasks_missing": tasks_missing,
                 "grade": grade}

    return dict_data





if __name__ == '__main__':
        try:
            s_read = csv_reader("students.csv")

        except FileNotFoundError as err:
            print(err, "File not found. Check the spelling.")



        s_data = data_imported(s_read)

        message = str(open_file("message.txt"))

        try:
            for names, surnames, tasks_missing, grade in zip(s_data["names"], s_data["surnames"], s_data["tasks_missing"], s_data["grade"]):
                print(message.format((names +" "+ surnames), tasks_missing, grade, int(grade) + 1))

        except ValueError as err2:
            print(err2, "It is not an integer!Check this out.")





