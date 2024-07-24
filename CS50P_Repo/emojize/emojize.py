from emoji import emojize

def main():
    emoji_input = input('Input: ')
    print('Output:', emojize(emoji_input, language = 'alias'))

main()
