months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input('Date: ').strip()
        if date[0].isnumeric():
            try:
                m, d, y = date.split('/')
            except ValueError:
               continue
            else:
                m = int(m)
                d = int(d)
                if len(y) == 4:
                    y = int(y)
                    if 0 < m <= 12:
                        if 0 < d <= 31:
                            return print(f'{y:04}', f'-{m:02}-', f'{d:02}', sep = '')
                        else:
                            print('Invalid day input, please try again')
                    else:
                        print('Invalid month input, please try again')
                else:
                    print('Invalid year input, please try again')
        elif date[0].isalpha():
            try:
                m, d, y = date.split(' ')
            except ValueError:
                print('Invalid format input, please try again')
            else:
                try:
                    m = months.index(m) + 1
                except ValueError:
                    print('Invalid month input, please try again')
                else:
                    if ',' in d:
                        d = int(d.strip(','))
                        if len(y) == 4:
                            y = int(y)
                            if 0 < d <= 31:
                                return print(f'{y:04}', f'-{m:02}-', f'{d:02}', sep = '')
                            else:
                                print('Invalid day input, please try again')
                        else:
                            print('Invalid year input, please try again')
                    else:
                        print('Invalid format input, please try again')

main()




# I hated this exercise the most so far:), I was for some reason for like a day and a half not realzing I forgot the () for the split methods after an input is entered. With the MM/DD/YYYY format inputs working though I thought everything was fine unitl I would got to enter the other format, and if would try to enter it in through the first control flow meant for the first format and ofcouse would error out. I was going crazy. All because I forgot some ().... Anyway originally I had each process as their own functions that would be called by main(), but when I got frustrated I deleted everything to start from scratch and here I am now. Everything works but if I had to make it look prettier I would seperate each one out by its own function again.
