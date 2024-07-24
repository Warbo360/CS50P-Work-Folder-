def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):

    # checks to see if string length is within set parameters

    if 2 <= len(s) <= 6:

        # checks to see of all characters are alphanumeric (cuts out punct characters)

        for c in s:
            if c.isalnum():
                continue
            else:
                return False

        # checks first two characters to makes sure they are alphabetic characters only

        for c in s[0:2]:
            if c.isalpha():
                continue
            else:
                return False
        if middle_check(s):
            return True
        else:
            return False

def middle_check(m):

    # checks all characters in the string after the first two (since we assume from the is_valid())

    for c in m[2:]:

        # checks to see if a character is numeric, and if so partions the string at that first numeric, first partition is not considered for anything thus _ is used.
        # b used to see if that first numeric is zero or not, if so returns false, then checks to see if 3rd partition is all numeric (as if not presumably contains alphabetics and this has numbers in the middle and is not valid)
        # I imagine there is a way cleaner way of doing this

        if c.isnumeric():
            _,b,d = m.partition(c)
            if b == '0':
                return False
            elif d.isnumeric() == False:
                return False
            else:
                return True
        else:
            return True
main()
