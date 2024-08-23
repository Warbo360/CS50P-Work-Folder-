from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    print(get_age(input('Date of Birth: ')))

def get_age(birth_day):
    try:
        age = date.today()-date.fromisoformat(birth_day)
    except ValueError:
        sys.exit('Invalid date, input as YYYY-MM-DD')
    else:
        return f'{p.number_to_words(int(age.total_seconds()/60), andword="")} minutes'

if __name__ == "__main__":
    main()
