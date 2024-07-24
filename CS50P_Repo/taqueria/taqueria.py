# define dict here for menu (menu = {dict here pls})
# main():
    # while true:
        # item_input = input('Item: ').title()
        # for item in menu:
            # if item == item_input:
                # total = float(menu[item]) + total
                # print(total)


menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.00
    while True:
        try:
            item_input = input('Item: ').title()
        except EOFError:
            print()
            break
        else:
            for item in menu:
                if item == item_input:
                    total = menu[item] + total
                    print('$',format(total, '.2f'), sep='')

main()
