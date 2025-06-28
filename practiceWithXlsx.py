from openpyxl import load_workbook  # Allows reading and writing speadsheet files
import sys
import re


def main():
    ws = get_ws(sys.argv[1])
    for rows in ws.values:
        for ind in range(len(rows)):
            if rows[ind] == "Sample ID":
                print(rows)
    rows = ws.values
    APQL = get_APQL(ws)
    num_of_samples = get_sample_num(ws)
    A_num = get_A_num(ws)
    # i = 0
    # while i < num_of_samples:
    #     print(f'''
    #           Sample ID XXXXXXXXXX XXXX
    #           Appearance & Color: Clear and Colorless
    #           {A_num}: Not detected. Reported as "<{APQL} ug/mL (APQL).".
    #           Other Peak(s): Not detected.
    #           Total({A_num} + Other Peak(s)): Reported as "<{APQL} ug/mL (APQL).".
    #           ''')
    #     i = i + 1


def get_APQL(worksheet):
    for rows in worksheet.values:
        for ind in range(len(rows)):
            if rows[ind] == "APQL:":
                return float(rows[ind+1])


def get_sample_num(worksheet):
    for rows in worksheet.values:
        for ind in range(len(rows)):
            if rows[ind] == "Sample #:":
                return float(rows[ind+1])


def get_A_num(worksheet):
    for rows in worksheet.values:
        for ind in range(len(rows)):
            if rows[ind] == "Target-Analyte":
                try:
                    return rows[ind+1]
                except ValueError:
                    sys.exit('Target-Analyte is not a string value')


def get_ws(filename):
    if re.search('.+.xlsx+', filename):
        try:
            wb = load_workbook(filename=sys.argv[1])  # Spreadsheet should only have one sheet
            return wb.active
        except FileNotFoundError:
            sys.exit('File not Found!')
    else:
        sys.exit('File is not an ".xlsx" file')


main()
