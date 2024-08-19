import pytest
from working import convert

def test_convert():
    test_len_4AMPM()
    test_len_5AMPM()
    test_len_7AMPM()
    test_len_8AMPM()
    test_len_4PMAM()
    test_len_5PMAM()
    test_len_7PMAM()
    test_len_8PMAM()
    test_len_4AMAM()
    test_len_5AMAM()
    test_len_7AMAM()
    test_len_8AMAM()
    test_len_4PMPM()
    test_len_5PMPM()
    test_len_7PMPM()
    test_len_8PMPM()
    test_twelve_AMPM()
    test_twelve_PMAM()
    test_twelve_AMAM()
    test_twelve_PMPM()
    test_cat()
    test_out_of_range()
    test_AM_PM_no_space()
    test_no_to_delimit()
    test_no_space_with_to()

def test_len_4AMPM():
    assert convert('8 AM to 9 PM') == f'08:00 to 21:00'
def test_len_5AMPM():
    assert convert('11 AM to 11 PM') == f'11:00 to 23:00'
def test_len_7AMPM():
    assert convert('8:30 AM to 9:30 PM') == f'08:30 to 21:30'
def test_len_8AMPM():
    assert convert('11:30 AM to 11:30 PM') == f'11:30 to 23:30'
def test_len_4PMAM():
    assert convert('8 PM to 9 AM') == f'20:00 to 09:00'
def test_len_5PMAM():
    assert convert('11 PM to 11 AM') == f'23:00 to 11:00'
def test_len_7PMAM():
    assert convert('8:30 PM to 9:30 AM') == f'20:30 to 09:30'
def test_len_8PMAM():
    assert convert('11:30 PM to 11:30 AM') == f'23:30 to 11:30'
def test_len_4AMAM():
    assert convert('8 AM to 9 AM') == f'08:00 to 09:00'
def test_len_5AMAM():
    assert convert('11 AM to 11 AM') == f'11:00 to 11:00'
def test_len_7AMAM():
    assert convert('8:30 AM to 9:30 AM') == f'08:30 to 09:30'
def test_len_8AMAM():
    assert convert('11:30 AM to 11:30 AM') == f'11:30 to 11:30'
def test_len_4PMPM():
    assert convert('8 PM to 9 PM') == f'20:00 to 21:00'
def test_len_5PMPM():
    assert convert('11 PM to 11 PM') == f'23:00 to 23:00'
def test_len_7PMPM():
    assert convert('8:30 PM to 9:30 PM') == f'20:30 to 21:30'
def test_len_8PMPM():
    assert convert('11:30 PM to 11:30 PM') == f'23:30 to 23:30'
def test_twelve_AMPM():
    assert convert('12 AM to 12 PM') == f'00:00 to 12:00'
def test_twelve_PMAM():
    assert convert('12 PM to 12 AM') == f'12:00 to 00:00'
def test_twelve_AMAM():
    assert convert('12 AM to 12 AM') == f'00:00 to 00:00'
def test_twelve_PMPM():
    assert convert('12 PM to 12 PM') == f'12:00 to 12:00'
def test_cat():
    with pytest.raises(ValueError):
        convert('cat')
def test_out_of_range():
    with pytest.raises(ValueError):
        convert('13:20 PM to 14:20 AM')
def test_AM_PM_no_space():
    with pytest.raises(ValueError):
        convert('1PM to 2AM')
def test_no_to_delimit():
    with pytest.raises(ValueError):
        convert('1 PM - 2 AM')
def test_no_space_with_to():
    with pytest.raises(ValueError):
        convert('1 PMto2 AM')

if __name__ == '__test_convert__':
    test_convert()
