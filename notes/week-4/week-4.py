# Week 4 notes - Libraries
    # Files of other program(s) that you or others have written that you then use in your own through modules
        # modules essentially come with extra functions that you can call that way we are not all copying and pasting code over and over again, and instead just importing said library/module to then use in our programs as needed.
        # One of the libraries/modules that Python comes with is random, which imports a random function for say flipping a coin or rolling dice for a program
            # doc for that docs.python.org/3/library/random.html
        # Keyword to import a library/module is just that - import -

import random

# random.choice(seq) how to call a random generator in Python where the seq param is just any list like object/data type, random needed before the choice to say which module we are loading from
coin = random.choice(['heads', 'tails'])
print(coin)

# key word - from -
    # allows us to import a specific fucntion from a given library/module into the scope of our program that way we do not need to use the random.choice() header in our program:

from random import choice

coin = choice(['heads', 'tails'])
print(coin)

# useful if 1) there are multiple uses of the name from different librarys/modules thus we need to say which is which, and 2) makes it eaiser to read/type if we use it multiple times as well.
# another function from this module is random.randint(a, b) or get random integer between a and b inclusively.

# So generates a random number from 1 to 10
number = random.randint(1, 10)
print(number)

# random.shuffle(x), takes in a list and randomizes their order/indices in practice

cards = ['jack', 'queen', 'king']
random.shuffle(cards)
for card in cards:
    print(card)

# So would shuffle the three cards and print each in the new order, each card with their own line

# Also a statistics library, for stats of course, docs.python.org/3/library/statistics.html

import statistics

print(statistics.mean([100, 90]))

# Will of course the mean of some list passed to the function.

# command-line arguments - allows to provide args to functions() being executed at commands to functions when running the program

# docs.python.org/3/library/sys.html
import sys

print('hello, my name is', sys.argv[1])

# so when running this program you would have:
# $ python name.py your_name_here
# which would then pass whatever you passed as an argument into sys.arg[1] as the input for that function, thus printing the 'hello, my name is your_name_here after running
# the reason we use [1] is that [0] in the terminal is occupied by the name of the program ofcourse. If nothing is passed to args though (so in the case above, we just run the program like we normally do), that will spit back out an error, in this case a IndexError.
    # Fix for this would be to put this piece of code in a try-except block for a IndexError just incase nothing is passed to sys.argv()

import sys
try:
    print('hello, my name is', sys.argv[1])
except IndexError:
    print('Too few arguments')

# Could also defensively code for this by introducing a conditional to make sure an arg was pass to sys.argv()

import sys

if len(sys.argv) < 2:
    print('Too few arguments')
elif len(sys.argv) > 2:
    print('Too many arguments')
else:
    print('hello, my name is', sys.argv[1])

# Thus no exception block needed for the block now with proper conditionals in place.
# Say we wanted to not hide the wanted print statment under an else statement, we would introduce a sys.exit, which just exits the program as it would seem

import sys

if len(sys.argv) < 2:
    sys.exit('Too few arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many arguments')
print('hello, my name is', sys.argv[1])

# Thus if we do not get the intended inputs the program will automatically end with a those error messages still as well, thus not requiring a else statement that then hides the print() function we actually care about.
# To take a slice of a list we can use [] next to the list to specify the indices to be included in whatever code we maybe wanting:

import sys

if len(sys.argv) < 2:
    sys.exit('Too few arguments')

for arg in sys.argv[1:]:
    print('hello, my name is', sys.argv[1])

# As you can see in the example above, the for-loop will only use the indices 1 to the end (thus no number specified) and cuts out the 0 indice in the list.

# packages - 3rd party libraries called packages, a place to grab them PyPI or pypi.org which has a ton of packages. cowsay for example, which has a cow say something. Usually handled with a package manager (in python's case pip is used alot). A program that comes with python. Done by useing the terminal:
    # $ pip install cowsay
# thus the package cowsay would be installed after running that command in the terminal.

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow('hello, ' + sys.argv[1])

# thus the cow will say whatever arg is passed when ran in the terminal with the program.

# APIs - Application Programing Interface - 3rd party interface that our code talks to, can be obatained with requests from from the requests library

    # $ install requests

# Example of API, Apple having their own API for iTunes
# JSON - Javascript Object Notation - standard text format for exchanging data between computers, Javascript not actually needed for it but just a convention used for databases.

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get('https://itunes.apple.com/search?search?entity=song&limit=1&term=' + sys.argv[1])
print(response.json())

# What this does, is obtain a JSON response that is convberted to a Python library through the request function from the request library, granted result is rather cryptive, thus would be nice to use another tool that can manipulate JSON text formats to something more readable, luckily there is if we import the json library:

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get('https://itunes.apple.com/search?search?entity=song&limit=1&term=' + sys.argv[1])
print(json.dumps(response.json(), indent=2))

# Resultings print:

{
 "resultCount":1,
 "results": [
{"wrapperType":"track", "kind":"song", "artistId":115234, "collectionId":1440878798, "trackId":1440879325, "artistName":"Weezer", "collectionName":"Weezer", "trackName":"Buddy Holly", "collectionCensoredName":"Weezer", "trackCensoredName":"Buddy Holly", "artistViewUrl":"https://music.apple.com/us/artist/weezer/115234?uo=4", "collectionViewUrl":"https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4", "trackViewUrl":"https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4",
"previewUrl":"https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/b1/35/53/b13553c8-22f3-3e62-47cc-beaf65440f0e/mzaf_9734530910938773283.plus.aac.p.m4a", "artworkUrl30":"https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/d0/16/da/d016da24-577e-b584-3a5a-116efb5ca362/16UMGIM52971.rgb.jpg/30x30bb.jpg", "artworkUrl60":"https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/d0/16/da/d016da24-577e-b584-3a5a-116efb5ca362/16UMGIM52971.rgb.jpg/60x60bb.jpg", "artworkUrl100":"https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/d0/16/da/d016da24-577e-b584-3a5a-116efb5ca362/16UMGIM52971.rgb.jpg/100x100bb.jpg", "collectionPrice":10.99, "trackPrice":1.29, "releaseDate":"1994-02-28T12:00:00Z", "collectionExplicitness":"notExplicit", "trackExplicitness":"notExplicit", "discCount":1, "discNumber":1, "trackCount":10, "trackNumber":4, "trackTimeMillis":159587, "country":"USA", "currency":"USD", "primaryGenreName":"Pop", "isStreamable":true}]
}


# This result gives a much more readable text output in the terminal that we can read (results in a dictionary output in Python format, see notes website for more specfic).
# to store the JSON output and manipulate:

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get('https://itunes.apple.com/search?search?entity=song&limit=50&term=' + sys.argv[1])
o = response.json()
for result in o['results']:
    print(result['trackName'])

# This would result an output of trackNames from the results list from the JSON output we obtain through this like above, and if you notice the API link in the requests.get(), we changed the limit to 50 from 1 thus we will be 50 different trackNames because of this.

# Possible to makes our own libraries that way we can reuse our own functions/code for other projects.

# File Name: sayings.py:
def main():
    hello('world')
    goodbye('world')

def hello(name):
    print(f'hello, {name}')

def goodbye(name):
    print(f'goodbye {name}')

if __name__ == '__main__':
    main()

# -------------NEW FILE----------------------

# File Name: say.py
import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

# Notice in the top example file that we import it into the bottom one and since we do not want to call the imported's main() automatically we us the 'if __name__ == '__main__': convention to say only run main if we are calling from the file itself and not just calling into another file for the use of importing a library.
# __name__ a variable to be called that only runs whatever we wrap in it to then run the functions under it if we run it from the terminal as the file that those functions exsist in.

# Notes on the Style-short for python:

# PEP 8 - Python Enchancement Proposal 8 - aims to codify some standards that what python code should look like, helps with readability and maintainability. peps.python.org/pep-0008/ for further docs on this.
    # Readability Counts
        # Style guide that says what python code should look like. Consistentcy being very important in any given program, module, etc
            # Indentation
            # Tabs/spaces (python agreed on 4 spaces for all things)
            # Max line length
            # blank lines
            # imports
    # pylint - A linter/tool that reads your code that sees if your code adheres to the PEP 8 guidelines, can be installed as follows: pip install pylint, also docs pycodestyle.pycqa.org
    # pycodestyle - another tool to format code for you for python, docs pycodestyle.pycqa.org, will reformat code for you as well.
    # black - installed via pip install black - docs black.readthedocs.io - will format your code as well that is gaining popularity, and is very opinateted, does it the same everytime.

students = {'Hermione': 'Gryffindor', 'Harry': 'Gryffindor'}

for student in students:
    print(student)

# If we run in the command line $ black students.py -- The program will auto format our code for us to adhere to the black format guidelines, output:

students = {
    'Hermione': 'Gryffindor',
    'Harry': 'Gryffindor',
}

for student in students:
    print(student)
