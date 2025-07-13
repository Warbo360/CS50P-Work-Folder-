from project import get_swab_APQL, get_sample_data, get_APQL, get_ws
import pytest
from openpyxl import load_workbook  # Allows reading and writing speadsheet files
import sys


def main():
    test_get_swab_APQL_returns_list_type()
    test_get_swab_APQL_returns_sys_exit_on_string_in_numerical_column()
    test_get_sample_data_AR_is_string()
    test_get_sample_data_Other_Peaks_is_not_comma_sep()
    test_get_sample_data_Other_Peaks_is_string()
    test_get_APQL_string()


def get_ws_for_test(filename):
    try:
        wb = load_workbook(filename)
        return wb.active
    except FileNotFoundError:
        sys.exit('File not Found!')


# Tests if the output of the function is a list
def test_get_swab_APQL_returns_list_type():
    assert isinstance(get_swab_APQL(get_ws_for_test("./test_spreadsheets/1-Cleaning Samples Template.xlsx")), list)


# Tests if programs exits on seeing that there is a sting in the numerical entry for swab APQLs
def test_get_swab_APQL_returns_sys_exit_on_string_in_numerical_column():
    with pytest.raises(SystemExit):
        get_swab_APQL(get_ws_for_test("./test_spreadsheets/2-Cleaning Samples Template.xlsx"))


# Tests if programs exits on A_result for a sample is not a numerical value
def test_get_sample_data_AR_is_string():
    with pytest.raises(SystemExit):
        get_sample_data(get_ws_for_test("./test_spreadsheets/3-Cleaning Samples Template.xlsx"))


# Tests on if SystemExit is raised if a list entry cannot separate on commas
def test_get_sample_data_Other_Peaks_is_not_comma_sep():
    with pytest.raises(SystemExit):
        get_sample_data(get_ws_for_test("./test_spreadsheets/4-Cleaning Samples Template.xlsx"))


# Tests if a SystemExit is raised on if one of the seperated values for a string insert for other peaks is non-numerical
def test_get_sample_data_Other_Peaks_is_string():
    with pytest.raises(SystemExit):
        get_sample_data(get_ws_for_test("./test_spreadsheets/5-Cleaning Samples Template.xlsx"))


# Tests if program gives SystemExit on if a non-numerical value is given for APQL
def test_get_APQL_string():
    with pytest.raises(SystemExit):
        get_APQL(get_ws_for_test("./test_spreadsheets/6-Cleaning Samples Template.xlsx"))


if __name__ == "__main__":
    main()
