from um import count
import pytest

def test_count():
    test_dot_um()
    test_um_dot()
    test_comma_um()
    test_um_comma()
    test_question_um()
    test_um_question()
    test_dot_Um()
    test_Um_dot()
    test_comma_Um()
    test_Um_comma()
    test_question_Um()
    test_Um_question()
    test_one_um()
    test_two_um()
    test_three_um()
    test_four_um()
    test_um_in_words_total_equal_zero()

def test_dot_um():
    assert count('...um') == 1
def test_um_dot():
    assert count('um...') == 1
def test_comma_um():
    assert count(',um') == 1
def test_um_comma():
    assert count('um,') == 1
def test_question_um():
    assert count('?um') == 1
def test_um_question():
    assert count('um?') == 1
def test_dot_Um():
    assert count('...Um') == 1
def test_Um_dot():
    assert count('Um...') == 1
def test_comma_Um():
    assert count(',Um') == 1
def test_Um_comma():
    assert count('Um,') == 1
def test_question_Um():
    assert count('?Um') == 1
def test_Um_question():
    assert count('Um?') == 1
def test_one_um():
    assert count('Um, the lazy fox') == 1
def test_two_um():
    assert count('Um, hello, um, world') == 2
def test_three_um():
    assert count('I, um, wonder, um, how, um, many penguins they have') == 3
def test_four_um():
    assert count('Um, why, um, the, fuck, um, do, um...') == 4
def test_um_in_words_total_equal_zero():
    assert count('Umpire, sum, neum, umps, umber, gumbo, umbrella') == 0

if __name__ == '__test_count__':
    test_count()
