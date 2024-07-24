from random import randrange
import sys

def main():
    level = 0
    actual = 0
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            pass
        else:
            if level > 0:
                actual = randrange(1, level + 1)
                while True:
                    try:
                        guess = int(input('Guess: '))
                    except ValueError:
                        pass
                    else:
                        if guess > actual:
                            print('Too large!')
                        elif guess < actual:
                            print('Too small!')
                        else:
                            sys.exit('Just right!')
            else:
                True

main()
