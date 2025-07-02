from openpyxl import load_workbook  # Allows reading and writing speadsheet files
import sys
import re
from statement_gen_lib import *


def main():
    ws = get_ws(sys.argv[1])
    statement_gen_rinse(sample_set_org(determine_swabs(ws), get_swab_APQL(ws), get_A_num(ws), get_APQL(ws), get_sample_data(ws)))


# TODO: Finish writing statment generator function
def statement_gen_rinse(sample_set_dict):
    for dicts in sample_set_dict['Sample List']:
# Permutation of all passing blank sample
        if (dicts['Sample Type'].lower().strip() == 'blank' and
           dicts['Appearance'].lower().strip() == 'pass' and
           isinstance(sample_set_dict['Limit'], (int, float)) and
           dicts['A-Result'] < sample_set_dict['Limit']):
            passing_rinse_blank(sample_set_dict, dicts)
# Permutation of all passing except appearance for blank rinse sample
        elif (dicts['Sample Type'].lower().strip() == 'blank' and
           dicts['Appearance'].lower().strip() == 'fail' and
           isinstance(sample_set_dict['Limit'], (int, float)) and
           dicts['A-Result'] < sample_set_dict['Limit']):
            pass_fail_rinse_blank(sample_set_dict, dicts)
# Permutation of failing blank but passing appearance
        elif (dicts['Sample Type'].lower().strip() == 'blank' and
           dicts['Appearance'].lower().strip() == 'pass' and
           isinstance(sample_set_dict['Limit'], (int, float)) and
           dicts['A-Result'] > sample_set_dict['Limit']):
            fail_pass_rinse_blank(sample_set_dict, dicts)
# Permuation of failing appearance and A Result for blanks
        elif (dicts['Sample Type'].lower().strip() == 'blank' and
           dicts['Appearance'].lower().strip() == 'fail' and
           isinstance(sample_set_dict['Limit'], (int, float)) and
           dicts['A-Result'] > sample_set_dict['Limit']):
            fail_rinse_blank(sample_set_dict, dicts)
# Permuation of all passing normal rinse samp with A-Result not detected (excel cell = 0)
        elif (dicts['Sample Type'].lower().strip() == 'sample' and
           dicts['Appearance'].lower().strip() == 'pass' and
           isinstance(sample_set_dict['Limit'], (int, float)) and
           dicts['A-Result'] == 0):
            zero_pass_rinse_sample(sample_set_dict, dicts)
# Permutation of passing rinse with detected A-result but still less than APQL
        elif (dicts['Sample Type'].lower().strip() == 'sample' and
           dicts['Appearance'].lower().strip() == 'pass' and
           isinstance(sample_set_dict['Limit'], (int, float)) and
           sample_set_dict['Limit'] > dicts['A-Result'] > 0):
            less_APQL_pass_rinse_sample(sample_set_dict, dicts)
# Permutation of passing rinse sample with A-result greather than or equal to APQL
        elif (dicts['Sample Type'].lower().strip() == 'sample' and
           dicts['Appearance'].lower().strip() == 'pass' and
           isinstance(sample_set_dict['Limit'], (int, float)) and
           dicts['A-Result'] >= sample_set_dict['Limit']):
            greater_APQL_pass_rinse_sample(sample_set_dict, dicts)
# Permutation of failng Appearance and AR not detected rinse sample
        elif (dicts['Sample Type'].lower().strip() == 'sample' and
           dicts['Appearance'].lower().strip() == 'fail' and
           isinstance(sample_set_dict['Limit'], (int, float)) and
           dicts['A-Result'] == 0):
            zero_fail_rinse_sample(sample_set_dict, dicts)
# Permuatatuon of failong Appearance and AP < APQL rinse sample
        elif (dicts['Sample Type'].lower().strip() == 'sample' and
           dicts['Appearance'].lower().strip() == 'fail' and
           isinstance(sample_set_dict['Limit'], (int, float)) and
           sample_set_dict['Limit'] > dicts['A-Result'] > 0):
            less_APQL_fail_rinse_sample(sample_set_dict, dicts)
# Permutation of failing Appearance and AR >= APQL rinse sample
        elif (dicts['Sample Type'].lower().strip() == 'sample' and
           dicts['Appearance'].lower().strip() == 'fail' and
           isinstance(sample_set_dict['Limit'], (int, float)) and
           dicts['A-Result'] >= sample_set_dict['Limit']):
            greater_APQL_fail_rinse_sample(sample_set_dict, dicts)
        else:
            print(f'{dicts} did not qualify for any of the catagories please fix dev!')


# Makes a dict out of relevant sample set info
def sample_set_org(swab_state, swab_limits, analyte, limit, sample_list):
    sample_set_info = {}
    if swab_state:
        sample_set_info['Limit'] = swab_limits
    else:
        sample_set_info['Limit'] = limit
    sample_set_info['Analyte'] = analyte
    sample_set_info['Sample List'] = sample_list
    return sample_set_info


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
        if (rows[0] and
            rows[1]):
            sample_list.append({
                'Sample ID': rows[0],
                'Sample Type': rows[1],
                'Material': rows[2],
                'Appearance': rows[3],
                'A-Result': rows[4],
                'Other-Peak(s)': rows[5],
                })
    for dicts in sample_list:
        if isinstance(dicts['Other-Peak(s)'], (int, float)):
            dicts['Summed-Other-Peak(s)'] = dicts['Other-Peak(s)']
            try:
                dicts['Summed-Total-Peak(s)'] = dicts['Other-Peak(s)'] + dicts['A-Result']
            except TypeError:
                sys.exit('An "A-Result" entry is non-numerical. Please fix and try again.')
        elif not dicts['Other-Peak(s)']:
            dicts['Summed-Other-Peak(s)'] = dicts['Other-Peak(s)']
            try:
                dicts['Summed-Total-Peak(s)'] = dicts['A-Result']
            except TypeError:
                sys.exit('An "A-Result" entry is non-numerical. Please fix and try again.')
        else:
            try:
                other_peaks = dicts['Other-Peak(s)'].split(',')
            except TypeError:
                sys.exit('One of more "Other-Peak(s)" entries are non-numerical values, please fix and try again')
            sum_of_peaks = 0
            for peaks in other_peaks:
                peaks = float(peaks)
                sum_of_peaks = sum_of_peaks + peaks
            sum_of_total_peaks = sum_of_peaks + float(dicts['A-Result'])
            dicts['Summed-Other-Peak(s)'] = sum_of_peaks
            dicts['Summed-Total-Peak(s)'] = sum_of_total_peaks
    print(sample_list)
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
