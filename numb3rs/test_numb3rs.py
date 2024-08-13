from numb3rs import validate

def test_validate():
    validate_alpha()
    validate_num()
    validate_white_space()
    validate_wrong_reps()
    validate_wrong_num_range()


def validate_alpha():
    assert validate('A.A.A.A') == f'invalid'

def validate_num():
    assert validate('12.12.12.12') == f'valid'

def validate_white_space():
    assert validate('     12.12.12.12         ') == f'valid'

def validate_wrong_reps():
    assert validate('12.12.12') == f'invalid'

def validate_wrong_num_range():
    assert valdiate('400.400.400.400') == f'invalid'

test_validate()
