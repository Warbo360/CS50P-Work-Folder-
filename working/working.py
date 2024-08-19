import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_one = ''
    time_two = ''
    if matches := re.search(r'^((?:[0-9]:?[0-5]?[0-9]? (?:AM|PM))|(?:[1][0-2]:?[0-5]?[0-9]? (?:AM|PM))) to ((?:[0-9]:?[0-5]?[0-9]? (?:AM|PM))|(?:[1][0-2]:?[0-5]?[0-9]? (?:AM|PM)))$',s):
        if 'AM' in matches.group(1):
            if re.search(r'12:?[0-5]?[0-9]?', f'{matches.group(1)}'):
                try:
                    h,m = matches.group(1).split(':')
                except ValueError:
                    time_one = f'00:00'
                else:
                    m,_ = m.split(' ')
                    time_one = time_one + f'00:{m}'
            elif len(matches.group(1)) == 4:
                t,_ = matches.group(1).split(' ')
                time_one = time_one + f'0{t}:00'
            elif len(matches.group(1)) == 5:
                t,_ = matches.group(1).split(' ')
                time_one = time_one + f'{t}:00'
            elif len(matches.group(1)) == 7:
                t,_ = matches.group(1).split(' ')
                time_one = time_one + f'0{t}'
            elif len(matches.group(1)) == 8:
                t,_ = matches.group(1).split(' ')
                time_one = time_one + f'{t}'
            else:
                sys.exit('time_one Error Please Try Again')
        elif 'PM' in matches.group(1):
            if re.search(r'12:?[0-5]?[0-9]?', f'{matches.group(1)}'):
                try:
                    h,m = matches.group(1).split(':')
                except ValueError:
                    time_one = time_one + f'12:00'
                else:
                    m,_ = m.split(' ')
                    time_one = time_one + f'{h}:{m}'
            elif len(matches.group(1)) == 4 or len(matches.group(1)) == 5:
                t,_ = matches.group(1).split(' ')
                t = int(t) + 12
                time_one = time_one + f'{t}:00'
            elif len(matches.group(1)) == 7 or len(matches.group(1)) == 8:
                t,_ = matches.group(1).split(' ')
                h,m = t.split(':')
                h = int(h) + 12
                time_one = f'{h}:{m}'
            else:
                sys.exit('time_one Error Please Try Again')
        if 'AM' in matches.group(2):
            if re.search(r'12:?[0-5]?[0-9]?', f'{matches.group(2)}'):
                try:
                    h,m = matches.group(2).split(':')
                except ValueError:
                    time_two = f'00:00'
                else:
                    m,_ = m.split(' ')
                    time_two = time_two + f'00:{m}'
            elif len(matches.group(2)) == 4:
                t,_ = matches.group(2).split(' ')
                time_two = time_two + f'0{t}:00'
            elif len(matches.group(2)) == 5:
                t,_ = matches.group(2).split(' ')
                time_two = time_two + f'{t}:00'
            elif len(matches.group(2)) == 7:
                t,_ = matches.group(2).split(' ')
                time_two = time_two + f'0{t}'
            elif len(matches.group(2)) == 8:
                t,_ = matches.group(2).split(' ')
                time_two = time_two + f'{t}'
            else:
                sys.exit('time_two Error Please Try Again')
        elif 'PM' in matches.group(2):
            if re.search(r'12:?[0-5]?[0-9]?', f'{matches.group(2)}'):
                try:
                    h,m = matches.group(2).split(':')
                except ValueError:
                    time_two = time_two + f'12:00'
                else:
                    m,_ = m.split(' ')
                    time_two = time_two + f'{h}:{m}'
            elif len(matches.group(2)) == 4 or len(matches.group(2)) == 5:
                t,_ = matches.group(2).split(' ')
                t = int(t) + 12
                time_two = time_two + f'{t}:00'
            elif len(matches.group(2)) == 7 or len(matches.group(2)) == 8:
                t,_ = matches.group(2).split(' ')
                h,m = t.split(':')
                h = int(h) + 12
                time_two = f'{h}:{m}'
            else:
                sys.exit('time_two Error Please Try Again')
        return f'{time_one} to {time_two}'

    else:
        raise ValueError





if __name__ == "__main__":
    main()
