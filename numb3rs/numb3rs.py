# Ask for IP address input
# search for valid pattern via validiation function (to be tested with unit test at test_numb3rs.py)
# return valid or invalid if input is found with regex pattern

import re
import sys

def main():
    print(validate(input('IPv4 Address: ')))

def validate(ip):
    if re.search(r'^(([1]?[0-9]?[0-9]|[2][0-4][0-9]|[2][5][0-5])\.){3}([1]?[0-9]?[0-9]|[2][0-4][0-9]|[2][5][0-5])$', ip):
        return True
    else:
        return False

if __name__ == '__main__':
    main()
