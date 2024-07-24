def main():
    inputConvert = input('Hi! Are you making a face? ')
    print(convert(inputConvert))

def convert(toEmoji):
    toEmoji = (toEmoji.replace(':)', '🙂')).replace(':(','🙁')
    return toEmoji

main()
