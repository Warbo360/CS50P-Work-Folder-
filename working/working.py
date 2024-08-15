import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r'^((?:[0-9]:?[0-5]?[0-9]? (?:AM|PM))|(?:[1][0-2]:?[0-5]?[0-9]? (?:AM|PM))) to ((?:[0-9]:?[0-5]?[0-9]? (?:AM|PM))|(?:[1][0-2]:?[0-5]?[0-9]? (?:AM|PM)))$',s):
        return f'{matches.group(1)} to {matches.group(2)}'
    else:
        raise ValueError





if __name__ == "__main__":
    main()
