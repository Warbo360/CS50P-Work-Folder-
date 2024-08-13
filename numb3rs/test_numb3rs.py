from numb3rs import validate

def test_validate():
    validate_alpha()
    validate_num()
    validate_white_space()
    validate_wrong_reps()
    validate_wrong_num_range_total()
    validate_wrong_num_range_one_rep()
    validate_dot_delimit()
    validate_digit_01()
    validate_digit_02()
    validate_digit_03()
    validate_digit_04()
    validate_digit_05()

def validate_alpha():
    assert validate('A.A.A.A') == f'False'

def validate_num():
    assert validate('12.12.12.12') == f'True'

def validate_white_space():
    assert validate('     12.12.12.12         ') == f'False'

def validate_wrong_reps():
    assert validate('12.12.12') == f'False'

def validate_wrong_num_range_total():
    assert validate('400.400.400.400') == f'False'

def validate_wrong_num_range_one_rep():
    assert validate('400.12.12.12') == f'False'

def validate_dot_delimit():
    assert validate('40012.12.12') == f'False'

def validate_digit_01():
    assert validate('012.054.111.009') == f'False'

def validate_digit_02():
    assert validate('012.54.111.9') == f'False'

def validate_digit_03():
    assert validate('12.054.111.9') == f'False'

def validate_digit_04():
    assert validate('12.54.111.009') == f'False'

def validate_digit_05():
    assert validate('12.54.111.9') == f'True'

test_validate()
