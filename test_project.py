from project import get_swab_APQL, get_sample_data, get_APQL, get_ws
import pytest


def main():
    test_get_swab_APQL_returns_list_type(open('./test_spreadsheets/1-Cleaning Samples Template.xlsx'))
    test_get_swab_APQL_returns_sys_exit_on_string_in_numerical_column(open('./test_spreadsheets/1-Cleaning Samples Template.xlsx'))
    test_get_sample_data(open('./test_spreadsheets/1-Cleaning Samples Template.xlsx'))
    test_get_APQL_string(open('./test_spreadsheets/1-Cleaning Samples Template.xlsx'))


def test_get_swab_APQL_returns_list_type(worksheet):
    assert isinstance(get_swab_APQL(worksheet), list)


def test_get_swab_APQL_returns_sys_exit_on_string_in_numerical_column(worksheet):
    with pytest.raises(SystemExit):
        get_swab_APQL(worksheet)


def test_get_sample_data(worksheet):
    ...


def test_get_APQL_string(worksheet):
    with pytest.raises(TypeError):
        get_APQL(worksheet)


if __name__ == "__main__":
    main()
