def main():
    fileName = (input('File name: ').lower()).strip() # Takes user file input, lowercases, removes whitespace, and assigns the string to a variable
    if fileName.endswith('.gif'): # if-else control flow going over the different file types with and else catch all
        print('image/gif')
    elif fileName.endswith('.jpg'):
        print('image/jpeg')
    elif fileName.endswith('.jpeg'):
        print('image/jpeg')
    elif fileName.endswith('.png'):
        print('image/png')
    elif fileName.endswith('.pdf'):
        print('application/pdf')
    elif fileName.endswith('.txt'):
        print('text/plain')
    elif fileName.endswith('.zip'):
        print('application/zip')
    else:
        print('application/octet-stream')

main()

