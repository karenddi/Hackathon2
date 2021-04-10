import pandas

def csv_reader(file):

    data = pandas.read_csv(file, sep=";")
    print(data)
    return data

def data_imported(data):

    names = data.name.tolist()
    surnames = data.surname.tolist()
    tasks_missing = data.tasks_missing.tolist()
    grade = data.grade.tolist()
    print(names)
    print(surnames)
    print(tasks_missing)
    print(grade)
    return names and surnames and tasks_missing and grade

def open_file(file):
    with open(file,  encoding="utf-8") as file_opened:
        lines = file_opened.readlines()
        print(lines)
        return lines

def personalised_message(data, message):

    for names, surnames, tasks_missing, grade in data:#zip(names, surnames, tasks_missing, grade):
     print(message.format(names, surnames, tasks_missing, grade, int(grades) + 1))





if __name__ == '__main__':
        try:
            students_read = csv_reader("students.csv")

        except FileNotFoundError as err:
            print(err, "File not found. Check the spelling.")

students_data = data_imported(students_read)
message = str(open_file("message.txt"))
message_final = personalised_message(students_data, message)



