from tabulate import tabulate
from sys import argv
import sys

def main():
    if len(argv) < 2:
        sys.exit('Too few arguments')
    elif len(argv) > 2:
        sys.exit('Too many arguments')
    elif '.csv' not in argv[1]:
        sys.exit('Not a CSV file')
    else:
        print(grid_maker(argv[1]))

def grid_maker(CSV_file):
    pizza_table = []
    try:
        with open(f'{CSV_file}') as file:
            for line in file:
                pizza_item, small, large = line.rstrip().split(',')
                pizza_table.append([pizza_item, small, large])
    except FileNotFoundError:
        sys.exit('File does not exist')
    else:
        return tabulate(pizza_table, headers='firstrow', tablefmt='grid')

if __name__ == '__main__':
    main()
