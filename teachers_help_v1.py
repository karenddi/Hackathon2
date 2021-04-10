import csv


def csv_reader(file):

    line_count = 0

    with open(file, encoding="utf-8") as csv_open:
        csv_file_reader = csv.reader(csv_open, delimiter=';')
        list_of_rows = list(csv_file_reader)
        print(list_of_rows)
        #for row in csv_file_reader:
                #print(f'{", ".join ( row )}')


if __name__ == '__main__':
        try:
            students_read = csv_reader ( "students.csv" )

        except FileNotFoundError as err:
            print(err, "File not found. Check the spelling.")



