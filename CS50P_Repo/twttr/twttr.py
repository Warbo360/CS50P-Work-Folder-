def main():
    input_str = input('Input: ')
    print('Output: ', end='')

    # Iterates over each character in the given string, sees if it does not match any case vowel, and if so prints that character on a single line

    for c in input_str:
        if c != 'A' and c != 'a' and c != 'E'and c != 'e' and c != 'I' and c != 'i' and c != 'O' and c != 'o' and c != 'U' and c != 'u':
            print(c, end='')

    print()
main()
