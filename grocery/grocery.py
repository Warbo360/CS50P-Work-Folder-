def main():
    shopping_list = []
    shopping_count = {}
    while True:
        try:
            shopping_list.append((input()))
            shopping_list = sorted(shopping_list)
        except EOFError:
            list_to_dict(shopping_list, shopping_count)
            for j in shopping_count:
                print(shopping_count.get(j), j.upper())
            break

# can only really be used for turning values of a list into keys for a dictionary, useful if wanting to count the occurences of values in a list and that is how it is used in this program

def list_to_dict(list, dict):
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

main()
