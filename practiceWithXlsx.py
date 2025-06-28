from openpyxl import load_workbook


def main():
    wb = load_workbook(filename='Cleaning Samples Template.xlsx')
    ws = wb.active
    APQL = get_APQL(ws)
    num_of_samples = get_sample_num(ws)
    i = 0
    while i < num_of_samples:
        print(f'''
              Sample ID XXXXXXXXXX XXXX
              Appearance & Color: Clear and Colorless
              A-XXXXXXXX: Not detected. Reported as "<{APQL} ug/mL (APQL).".
              Other Peak(s): Not detected.
              Total(A-XXXXXXX + Other Peak(s)): Reported as "<{APQL} ug/mL (APQL).".
              ''')
        i = i + 1

    # j = 0
    # while j < num_of_samples:
    #     print(f'This is a test, here is {APQL}\n')
    #     j = j + 1


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


main()
