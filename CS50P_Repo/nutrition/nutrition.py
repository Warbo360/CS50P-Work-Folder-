def main():
    item = input('Item: ').lower()

    # make a dict of idex of items and their values being calories of that item
    # iterate over dict to match user input and output that items calories

    fruits = {
        'apple': 130,
        'avocado': 50,
        'banana': 110,
        'cantaloupe': 50,
        'grapefruit': 60,
        'grapes': 90,
        'honeydew melon': 50,
        'kiwifruit': 90,
        'lemon': 15,
        'lime': 20,
        'nectarine': 60,
        'orange': 80,
        'peach': 60,
        'pear': 100,
        'pineapple': 50,
        'plums': 70,
        'strawberries': 50,
        'sweet cherries': 100,
        'tangerine': 50,
        'watermelon': 80,
    }

    for fruit in fruits:
        if fruit == item:
            print('Calories:',fruits[fruit])
            break

main()
