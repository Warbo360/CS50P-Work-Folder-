from twttr import shorten

def main():
    test_shorten_lower()
    test_shorten_upper()
    test_shorten_both_case()
    test_shorten_space()
    test_shorten_no_numbers()

def test_shorten_lower():
    assert shorten('walter') == 'wltr'
    assert shorten('twitter') == 'twttr'

def test_shorten_upper():
    assert shorten('WALTER') == 'WLTR'
    assert shorten('TWITTER') == 'TWTTR'

def test_shorten_both_case():
    assert shorten('WAlter') == 'Wltr'
    assert shorten('tWiTteR') == 'tWTtR'

def test_shorten_space():
    assert shorten('HELLO, WORLD') == 'HLL, WRLD'

def test_shorten_no_numbers():
    assert shorten('123') == '123'
