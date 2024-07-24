def main():
    camel_input = input('camelCase: ' )

    # Iterates over the characters in the str

    for i in camel_input:

        # Checks if each charcter in the str is an uppercase str

        if i.isupper():

            # If str is uppercase, swaps its case to lower, and adds a underscore str infront of it

           i = '_' + (i.lower())

            # Prints each character scanned in the for-loop, "end=''" added so it appears all in the same line

        print(i, end='')

    # empty print() to move the cursor to a new line like typical behavior

    print()

main()
