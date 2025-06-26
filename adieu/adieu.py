import inflect
p = inflect.engine()


def main():
    names = []
    while True:
        try:
            names.append(input('Name: '))
        except EOFError:
            names = p.join(names, final_sep=',')
            return print('Adieu, adieu, to', names)


main()
