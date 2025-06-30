from openpyxl import load_workbook  # Allows reading and writing speadsheet files
import sys
import re


def main():
    ws = get_ws(sys.argv[1])
    APQL = get_APQL(ws)
    # num_of_samples = get_sample_num(ws)
    A_num = get_A_num(ws)
    swabs = determine_swabs(ws)
    statement_gen_rinse(get_APQL(ws), get_sample_data(ws), get_A_num(ws))


# TODO: Finish writing statment generator function
def statement_gen_rinse(limit, samples_list, analyte):
    for dicts in samples_list:
        if dicts['Sample Type'] == 'Blank':
            print('This is a test')
            print(dicts['Sample Type'])
            if dicts['Appearance'] == 'Pass':
                if dicts['A-Result'] < limit:
                    print(f'''
                          Sample {dicts['Sample ID']}
                          Appearance & Color: Sample is clear and colorless. Reported as "Pass".
                          {analyte}: Not detected. Reported as "Pass".
                          Other Peak(s): {dicts['A-Result'] + dicts['Other-Peak(s)']} ug/mL
                          ''')
            ...
    ...


# Gather Swab APQL info return that info as a list of dicts
def get_swab_APQL(worksheet):
    material_APQLs = []
    for rows in worksheet.iter_rows(min_row=2, max_row=9, min_col=4, max_col=5, values_only=True):
        if rows[0] and isinstance(rows[1], (int, float)):
            material_APQLs.append({
                'Material': rows[0],
                'APQL': rows[1]
                })
        elif not rows[0] and not rows[1]:
            continue
        else:
            print(f'Please check the row of the {rows[0]} entry and that its inforamation is correct')
    return material_APQLs


# Gathers sample data and arranges it into a list of dicts, also automatically converts 'Other-Peak(s)' into one float
def get_sample_data(worksheet):
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
    for dicts in sample_list:
        if isinstance(dicts['Other-Peak(s)'], (int, float)):
            other_peaks = dicts['Other-Peak(s)']
        elif not dicts['Other-Peak(s)']:
            continue
        else:
            other_peaks = dicts['Other-Peak(s)'].split(',')
            sum_of_peaks = 0
            for peaks in other_peaks:
                peaks = float(peaks)
                sum_of_peaks = sum_of_peaks + peaks
                dicts['Other-Peak(s)'] = sum_of_peaks
    return sample_list


# Gets the value of APQL
def get_APQL(worksheet):
    if isinstance(worksheet['B6'].value, float):
        return worksheet['B6'].value
    elif isinstance(worksheet['B6'].value, int):
        return worksheet['B6'].value
    else:
        sys.exit('APQL is not set to a numerical value. Please fix and try again.')


# Gets the number of samples
# def get_sample_num(worksheet):
#     try:
#         if worksheet['B7'].value.is_integer():
#             return worksheet['B7'].value
#         else:
#             sys.exit('Sample number is not set as an integer. Please fix and try again')
#     except AttributeError:
#         sys.exit('Sample number has non-numeric characters. Please fix and try again.')


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
