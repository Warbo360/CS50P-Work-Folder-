import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few args')
    elif len(sys.argv) > 3:
        sys.exit('Too many args')
    elif '.csv' not in sys.argv[1] or '.csv' not in  sys.argv[2]:
        sys.exit('One or both args was not a CSV file')
    else:
        convert(sys.argv[1], sys.argv[2])


# Idea is to use csv reader to parse input file into a list of dicts, writer then just puts into new file and returns to main

def convert(csv_in, csv_out):
    list_of_students = []
    try:
        with open(csv_in, 'r') as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                last, first = row['name'].split(',')
                first = first.strip()
                unqiue_student = {'first': first, 'last': last, 'house': row['house']}
                list_of_students.append(unqiue_student)
    except FileNotFoundError:
        sys.exit('File does not exist')
    else:
        with open(csv_out, 'w') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            i = 0
            while i < len(list_of_students):
                writer.writerow(list_of_students[i])
                i += 1

if __name__ == '__main__':
    main()


