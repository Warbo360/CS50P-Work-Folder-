from numb3rs import validate

def main():
    test_validate_range()
    test_validate_format()

def test_validate_range():
    test_validate_alpha()
    test_validate_num()
    test_validate_wrong_num_range_total()
    test_validate_wrong_num_range_one_rep()
    test_validate_wrong_byte()

def test_validate_format():
    test_validate_white_space()
    test_validate_wrong_reps()
    test_validate_dot_delimit()
    test_validate_digit_01()
    test_validate_digit_02()
    test_validate_digit_03()
    test_validate_digit_04()
    test_validate_digit_05()
    test_validate_leading_zeros()

def test_validate_alpha():
    assert validate('A.A.A.A') == False

def test_validate_num():
    assert validate('12.12.12.12') == True

def test_validate_white_space():
    assert validate('     12.12.12.12         ') == False

def test_validate_wrong_reps():
    assert validate('12.12.12') == False

def test_validate_wrong_num_range_total():
    assert validate('400.400.400.400') == False

def test_validate_wrong_num_range_one_rep():
    assert validate('400.12.12.12') == False

def test_validate_dot_delimit():
    assert validate('40/2.12.12') == False

def test_validate_digit_01():
    assert validate('012.054.111.009') == True

def test_validate_digit_02():
    assert validate('012.54.111.9') == True

def test_validate_digit_03():
    assert validate('12.054.111.9') == True

def test_validate_digit_04():
    assert validate('12.54.111.009') == True

def test_validate_digit_05():
    assert validate('12.54.111.9') == True

def test_validate_wrong_byte():
    assert validate('75.456.76.65') == False

def test_validate_leading_zeros():
    assert validate('01.01.01.01') == True

if __name__ == '__main__':
    main()
