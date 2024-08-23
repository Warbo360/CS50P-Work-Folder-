import pytest
from seasons import get_age

def test_get_age():
    test_one_year_ago()
    test_two_years_ago()
    test_invalid_format()

# Tests were made as of 2024-08-23 and dates reflect that, change as needed (2024 was a leap year so 2023-08-23 is actually 366 days ago

def test_one_year_ago():
    assert get_age('2023-08-24') == f'Five hundred twenty-five thousand, six hundred minutes'

def test_two_years_ago():
    assert get_age('2022-08-24') == f'One million, fifty-one thousand, two hundred minutes'

def test_invalid_format():
    with pytest.raises(SystemExit):
        get_age('10-03-1996')

if __name__ == '__test_get_age__':
    test_get_age()
