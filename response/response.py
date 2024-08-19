from validator_collection import checkers

def main():
    print(validate(input('Email: ')))

def validate(s):
    if checkers.is_email(s):
        return f'Valid'
    else:
        return f'Invalid'

if __name__ == '__main__':
    main()


