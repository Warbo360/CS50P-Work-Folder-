import sys
import requests
import json


def main():
    bitCoinInput = 0
    if len(sys.argv) == 2:
        try:
            bitCoinInput = float(sys.argv[1])
        except ValueError:
            sys.exit('Command-line argument is not a number')
    else:
        sys.exit('Too few or too many command-line arguments, please input one integer as an argument')
    try:
        coinList = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.RequestException:
        sys.exit('Request failed please try again later')
    else:
        rate = json.dumps(coinList.json()['bpi']['USD']['rate'])
        rate = float(strip_middle_characters(rate.strip('"'), ','))
        print(f'${rate * bitCoinInput:,.4f}')


def strip_middle_characters(str, sep):
    str = str.partition(sep)
    str = str[0] + str[2]
    return str


main()
