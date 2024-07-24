def main():
    inputWord = input('Input: ')
    print('Output:', shorten(inputWord))

def shorten(word):
    stripList = ['A','a','E','e','I','i','O','o','U','u']
    shorterWord = ''
    for c in word:
        if c not in stripList:
            shorterWord += c
    return shorterWord

if __name__ == '__main__':
    main()
