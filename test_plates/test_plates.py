from plates import is_valid

def main():
    test_punc_is_valid()
    test_01letter_valid()
    test_0letter_valid()
    test_start_num_valid()
    test_middle_num_valid()
    test_end_num_valid()
    test_less_than_two_valid()
    test_greater_six_valid()
    test_end_num_zero_valid()
    test_whitespace_valid()

def test_punc_is_valid():
    assert is_valid('AA..34') == False

def test_01letter_valid():
    assert is_valid('AA1234') == True

def test_0letter_valid():
    assert is_valid('A12345') == False

def test_start_num_valid():
    assert is_valid('12ABCD') == False

def test_middle_num_valid():
    assert is_valid('AB12CD') == False

def test_end_num_valid():
    assert is_valid('ABCD12') == True

def test_less_than_two_valid():
    assert is_valid('A') == False

def test_greater_six_valid():
    assert is_valid('ABCD1234') == False

def test_end_num_zero_valid():
    assert is_valid('AB0012') == False

def test_whitespace_valid():
    assert is_valid('  AB1234    ') == False

if __name__ == '__main__':
    main()
