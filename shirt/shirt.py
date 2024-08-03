import sys
from PIL import Image 
from PIL import ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few args')
    elif len(sys.argv) > 3:
        sys.exit('Too many args')
    elif '.jpg' not in sys.argv[1] and '.jpeg' not in sys.argv[1] and '.png' not in sys.argv[1]:
        sys.exit('Incorrect file type')
    elif sys.argv[1][-3:] != sys.argv[2][-3:]:
        sys.exit('Args must be same file type')
    else:
        edit(sys.argv[1], sys.argv[2]) # CLI args added after calling program in CLI [1] to be file to read, [2] to be the write file

def edit(input, output):
    try:
        shirt = Image.open('shirt.png')
        size = shirt.size
        with Image.open(input) as im:
            im = ImageOps.fit(im, size)
            im.paste(shirt, shirt)
            im.save(output)
    except FileNotFoundError:
        sys.exit('File does not exist')

if __name__ == '__main__':
    main()
