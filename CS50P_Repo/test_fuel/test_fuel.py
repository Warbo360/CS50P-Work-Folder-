from fuel import convert
from fuel import gauge
from pytest import raises

def test_convert():
    floats_convert()
    str_convert()
    n_great_d_convert()
    d_by_zero_convert()
    round_convert_1()
    round_convert_2()
    round_convert_3()

def test_gauge():
    E_gauge()
    F_gauge()
    Z_gauge()

def floats_convert():
    with raises(ValueError):
        convert('3.6/5.5')

def str_convert():
    with raises(ValueError):
        convert('cat/dog')

def n_great_d_convert():
    with raises(ValueError):
        convert('4/3')

def d_by_zero_convert():
    with raises(ZeroDivisionError):
        convert('4/0')

def round_convert_1():
    assert convert('2/3') == 67

def round_convert_2():
    assert convert('1/3') == 33

def round_convert_3():
    assert convert('4/6') == 67

def E_gauge():
    assert gauge(1) == 'E'

def F_gauge():
    assert gauge(99) == 'F'

def Z_gauge():
    assert gauge(50) == '50%'

if __name__ == '__main__':
    test_convert()
    test_gauge()
