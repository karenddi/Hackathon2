import csv


def csv_reader(file):

    line_count = 0

    with open(file, encoding="utf-8") as csv_open:
        csv_file_reader = csv.reader(csv_open, delimiter=';')
        list_of_rows = list(csv_file_reader)
        print(list_of_rows)
        #for row in csv_file_reader:
                #print(f'{", ".join ( row )}')

def open_file(file):
    with open(file,  encoding="utf-8") as file_opened:
        lines = file_opened.readlines()
        print(lines)
        return lines


def data_imported(data):

    dict_data = {"names": data[1],
                 "surnames": data[1],
                 "tasks_missing" : data[2],
                 "grade": data[3]}
    print(dict_data)
    return dict_data


if __name__ == '__main__':
        try:
            students_read = csv_reader ( "students.csv" )

        except FileNotFoundError as err:
            print(err, "File not found. Check the spelling.")

message = str(open_file("message.txt"))
stu_dict = data_imported(students_read)



