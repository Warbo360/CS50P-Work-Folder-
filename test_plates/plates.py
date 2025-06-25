def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(s):
    if (middle_check(s)
        and length_check(s)
        and start_is_alpha(s)
            and s.isalnum()):
        return True
    else:
        return False


def middle_check(m):
    for c in m[2:]:
        if c.isnumeric():
            _, b, d = m.partition(c)
            if b == '0':
                return False
            elif d.isnumeric():
                return False
            else:
                return True
        else:
            return True


def length_check(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


def start_is_alpha(s):
    for c in s[0:2]:
        if not c.isalpha():
            return False
    return True


if __name__ == '__main__':
    main()
