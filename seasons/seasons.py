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
        age = age/60
        age = int(age.total_seconds())
        print(age)
        return f'{p.number_to_words(age, andword="")} minutes'

if __name__ == "__main__":
    main()
