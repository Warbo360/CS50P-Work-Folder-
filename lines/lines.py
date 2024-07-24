from sys import argv
import sys
from pytest import raises

def main():
    if len(argv) < 2:
        sys.exit('Too few arguments')
    elif len(argv) > 2:
        sys.exit('Too many arguments')
    elif '.py' not in argv[1]:
        sys.exit('Not a Python file')
    else:
        print(f'{line_count(argv[1])}')

def line_count(file):
    count = 0
    try:
        with open(file) as opened_py:
            for line in opened_py:
                if line.strip() == '':
                    continue
                elif line.strip()[0] == '#':
                    continue
                else:
                    count += 1
    except FileNotFoundError:
        sys.exit('File does not exist')
    else:
        return count

if __name__ == '__main__':
    main()
