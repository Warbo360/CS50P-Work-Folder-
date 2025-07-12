from project import get_swab_APQL, get_sample_data, get_APQL, get_ws


def main():
    test_get_swab_APQL(open('./test_spreadsheets/1-Cleaning Samples Template.xlsx'))
    test_get_sample_data('./test_spreadsheets/1-Cleaning Samples Template.xlsx')
    test_get_APQL('./test_spreadsheets/1-Cleaning Samples Template.xlsx')


def test_get_swab_APQL(worksheet):
    ...


def test_get_sample_data(worksheet):
    ...


def test_get_APQL(worksheet):
    ...


if __name__ == "__main__":
    main()
