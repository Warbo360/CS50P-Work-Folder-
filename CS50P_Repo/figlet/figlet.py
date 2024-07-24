from pyfiglet import Figlet
import sys
import random





def main():
    f = Figlet()
    if len(sys.argv) == 1:
        f.setFont(font = (random.choice(f.getFonts())))
        print('Output:', '\n', '\n', f.renderText(input('Input: ')))
    elif len(sys.argv) == 2:
        sys.exit('Too few arguments')
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and (sys.argv[2] in f.getFonts()):
        f = Figlet(sys.argv[2])
        print('Output:', '\n', '\n', f.renderText(input('Input: ')))
    elif len(sys.argv) > 3:
        sys.exit('Too many arguments')
    else:
        sys.exit('Invalid input')


main()

