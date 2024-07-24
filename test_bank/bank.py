def main():
    greet = input('Greeting: ')
    print(f'$ + {value(greet)}')


def value(greeting):
    greeting = greeting.strip().lower()
    try:
        if greeting[0] == 'h':
            if greeting[0:5] == 'hello':
                return 0
            else:
                return 20
        else:
            return 100
    except IndexError:
        return 100

if __name__ == "__main__":
    main()
