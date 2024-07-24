import random

def main():
    level = get_level()
    score = 0
    i = 0
    while i < 10:
        try:
            a = generate_integer(level)
            b = generate_integer(level)
        except ValueError:
            level = get_level()
        else:
            j = 0
            while j < 3:
                try:
                    guess = int(input(f'{a} + {b} = '))
                except ValueError:
                    print('EEE')
                    j += 1
                else:
                    if guess == (a + b):
                        score += 1
                        break
                    elif j < 2:
                        print('EEE')
                        j += 1
                    else:
                        print('EEE')
                        print(f'{a} + {b} = {a + b}')
                        break
            i += 1
    print('score:', score)


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if 0 >= level or level > 3:
                raise ValueError
        except (ValueError, TypeError):
            pass
        else:
            return level




def generate_integer(level):
    if level == 1:
        return random.randrange(0, 10 ** (level))
    elif 2 <= level <= 3:
        return random.randrange(10 ** (level - 1), 10 ** (level))
    else:
        raise ValueError

if __name__ == '__main__':
    main()

