# def main():
    # while True:
        # get_frac(f)
        # if condtional to check if (f) inputted is greater than 100%
            # if so reprompt user for input as over 100% fuel makes no sense
        # elif conditonal to check if less than of equal to 1%
            # print 'E' as output
        # elif condtional to check if greater than or equal to 99%
            # print 'F' as output
        # else
            # Print int value as is

# get fracfunc():
    # while True:
        # try:
            # return( prompt user for fraction input,partition with '/' seperator, convert to int, round to nearest int, * 100)
        # except ValueError
            # print('not a fraction') for ValueError
        # except ZeroDivisionError
            # print('Can not divide by zero')

# main()

def main():
    while True:
        gas_left_frac = getfrac('Fraction: ')
        if gas_left_frac > 100:
            print('Fuel can not exceed 100%, please try again')
        elif gas_left_frac <= 1:
            return print('E')
        elif gas_left_frac >= 99:
            return print('F')
        else:
            return print(gas_left_frac, '%', sep='')

def getfrac(prompt):
    while True:
        try:
            num1, _, num2 = input(prompt).partition('/')
            return round((int(num1) / int(num2)) * 100)
        except ValueError:
            print('Not a valid fraction, please try again')
        except ZeroDivisionError:
            print('Can\'t divide by zero, please try again')

main()

