def main():
    while True:
        input_fraction = input('Fraction: ')
        try:
            return print(gauge(convert(input_fraction)))
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    n, d = fraction.split('/')
    if n.isnumeric() and d.isnumeric():
        n = int(n)
        d = int(d)
    else:
        raise ValueError
    percentage = round((n / d) * 100)
    if percentage > 100:
        raise ValueError
    else:
        return percentage

def gauge(percentage):
    if percentage <= 1:
        return f'E'
    elif percentage >= 99:
        return f'F'
    else:
        return f'{percentage}%'

if __name__ == '__main__':
    main()
