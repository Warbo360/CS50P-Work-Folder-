import sys
from openpyxl import load_workbook


wb = load_workbook(filename='empty_book.xlsx', read_only=True)
# Practice using openpyxl to access Excel file


def main():
    if len(sys.argv) == 2:
        auto_gen((results_pull(sys.argv[1])))
    elif len(sys.argv) < 2:
        manual_gen()
    else:
        sys.exit('Too many arguments')

# Will pull results straight from file in CLI args


def results_pull(file):
    return (file)


def auto_gen(file_test):
    print(file_test)


def manual_gen():
    print('Make your own results')


if __name__ == "__main__":
    main()
