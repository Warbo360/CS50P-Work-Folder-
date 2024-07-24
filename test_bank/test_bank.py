from bank import value

def main():
    test_upper_hello()
    test_lower_hello()
    test_upper_h()
    test_lower_h()
    test_whitespace()
    test_numbers()
    test_whitespace_upper_hello()
    test_whitespace_lower_hello()
    test_whitespace_upper_h()
    test_whitespace_lower_h()
    test_whitespace_numbers()
    test_hello_not_at_start()
    test_h_not_at_start()
    test_h_hello_combo()
    test_hello_h_combo()
    test_no_input()

def test_upper_hello():
    assert value('Hello') == 0

def test_lower_hello():
    assert value('hello') == 0

def test_upper_h():
    assert value('Hey') == 20

def test_lower_h():
    assert value('hey') == 20

def test_whitespace():
    assert value('    Hello       ') == 0

def test_numbers():
    assert value('1234') == 100

def test_whitespace_upper_hello():
    assert value('        Hello        ') == 0

def test_whitespace_lower_hello():
    assert value('         hello       ') == 0

def test_whitespace_upper_h():
    assert value('           Hey           ') == 20

def test_whitespace_lower_h():
    assert value('               hey            ') == 20

def test_whitespace_numbers():
    assert value('           1234354      ') == 100

def test_hello_not_at_start():
    assert value('I am hello to you sir') == 100

def test_h_not_at_start():
    assert value('What in the world! HEY!') == 100

def test_h_hello_combo():
    assert value('Hey, Hello!') == 20

def test_hello_h_combo():
    assert value('Hello, Hey!') == 0

def test_no_input():
    assert value('') == 100

if __name__ == '__main__':
    main()
