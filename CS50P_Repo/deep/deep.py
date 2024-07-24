def main():
    hitchHikerInput = (input('What is the answer to the Great Question of Life, the Universe and Everything? ').lower()).strip() # Takes user input and lowercases, then removes whitespace around it, finally assigns the input as a variable
    match hitchHikerInput: # match-case with various forms of 42 printing 'yes' and all other inputs printing 'no'
        case '42' | 'forty-two' | 'forty two':
            print('Yes')
        case _:
            print('No')

main()
