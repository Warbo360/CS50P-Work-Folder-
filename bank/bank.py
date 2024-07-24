def main():
    greeting = (input('Greeting: ').lower()).lstrip() # Takes user's greeting, lowercases, removes leading whitespace, and finally assigns it a variable
    if greeting.startswith('hello'): # Evaluates whether the greeting starts with a 'hello'
        print('$0')
    elif greeting.startswith('h'): # Evaluates whether the greeting starts with a "h"
        print('$20')
    else: # Catch all condition if the other two conditions return false
        print('$100')

main()
