def main():
    amount_due = 50
    print('Amount Due:', amount_due)
    print('-' * 30)

    while True:
        amount_in =int(input('Insert Coin: ').strip())
        if amount_in == 5 or amount_in == 10 or amount_in == 25:
            if amount_in < amount_due:
                amount_due = amount_due - amount_in
                amount_in = 0
                print('Amount Due:', amount_due)
                print('-' * 30)
                continue
            else:
                amount_due = amount_due - amount_in
                amount_in = 0
                print('Change Owed:', amount_due * -1)
                print('-' * 30)
                break
        else:
           print('Amount Due:', amount_due)
           print('-' * 30)
        continue

main()
