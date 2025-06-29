from openpyxl import load_workbook  # Allows reading and writing speadsheet files
import sys
import re


def main():
    ws = get_ws(sys.argv[1])
    APQL = get_APQL(ws)
    num_of_samples = get_sample_num(ws)
    A_num = get_A_num(ws)
    swabs = determine_swabs(ws)
    # statement_gen(num_of_samples, APQL, A_num)


def statement_gen(sample_number, limit, analyte, sample_list):
    i = 0
    while i < sample_number:
        i = i + 1


# Gathers sample data and arranges it into a list of dicts
def sample_info_gatherer(worksheet):
    sample_list = []
    for rows in worksheet.iter_rows(min_row=14, max_col=6, values_only=True):
        sample_list.append({
            'Sample ID': rows[0],
            'Sample Type': rows[1],
            'Material': rows[2],
            'Appearance': rows[3],
            'A-Result': rows[4],
            'Other-Peak(s)': rows[5]
            })
    return sample_list


# Gets the value of APQL
def get_APQL(worksheet):
    if isinstance(worksheet['B6'].value, float):
        return worksheet['B6']
    elif isinstance(worksheet['B6'].value, int):
        return worksheet['B6']
    else:
        sys.exit('APQL is not set to a numerical value. Please fix and try again.')


# Gets the number of samples
def get_sample_num(worksheet):
    try:
        if worksheet['B7'].value.is_integer():
            return worksheet['B7'].value
        else:
            sys.exit('Sample number is not set as an integer. Please fix and try again')
    except AttributeError:
        sys.exit('Sample number has non-numeric characters. Please fix and try again.')


# Gets name of target analyte
def get_A_num(worksheet):
    try:
        if worksheet['B5'].value:
            return worksheet['B5'].value
        else:
            sys.exit('Target Analyte is not set. Please fix and try again.')
    except IOError:
        sys.exit('Worksheet Error')


# Gets the active Worksheet from input Workbook
def get_ws(filename):
    if re.search('.+.xlsx+', filename):
        try:
            wb = load_workbook(filename=sys.argv[1])  # Spreadsheet should only have one sheet
            return wb.active
        except FileNotFoundError:
            sys.exit('File not Found!')
    else:
        sys.exit('File is not an ".xlsx" file')


# Determines if sample set are swabs or not
def determine_swabs(worksheet):
    try:
        if worksheet['B8'].value.strip().lower() == 'yes':
            return True
        else:
            return False
    except AttributeError:
        sys.exit('Swabs in Cell "B8" not set to yes or no. Please fix and try again')


main()
