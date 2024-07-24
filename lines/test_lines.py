from lines import line_count
from lines import main
from sys import argv
import pytest

def test_line_count():
    test_comment()
    test_doc_string()
    test_five_lines()
    test_file_not_found()
    test_all_combo_for_ten_lines()

def test_comment():
    assert line_count('com.py') == 0

def test_doc_string():
    assert line_count('docstring.py') == 2

def test_five_lines():
    assert line_count('five.py') == 5

def test_file_not_found():
    with pytest.raises(SystemExit):
        line_count('NoName.py')

def test_all_combo_for_ten_lines():
    assert line_count('tenPiece.py') == 10

if __name__ == '__main__':
    test_line_count()

