from openpyxl import load_workbook  # Allows reading and writing speadsheet files
import sys
import re
from statement_gen_lib import swab_sample_gen, rinse_sample_gen


def main():
    if len(sys.argv) == 2:
        print(sample_list_checker(get_sample_data(get_ws(sys.argv[1]))), 'line 9')
    elif len(sys.argv) > 2:
        sys.exit('Please only link one file path at a time.')
    else:
        sys.exit('No file path given.')
    # statement_gen(get_sample_data(ws))
    # Testing git commit editor on work comp


# def statement_gen(sample_set_dict):
#     if isinstance(sample_set_dict['Limit'], (int, float)):
#         rinse_sample_gen(sample_set_dict)
#     elif isinstance(sample_set_dict['Limit'], (list)):
#         swab_sample_gen(sample_set_dict)


# Gathers sample data and arranges it into a list of dicts, also automatically converts 'Other-Peak(s)' into one float
def get_sample_data(worksheet):
    sample_list = []
    for rows in worksheet.iter_rows(min_row=3, max_col=7, values_only=True):
        if (rows[0] and
                rows[1]):
            sample_list.append({
                'Sample ID': str(rows[0]).lower().strip(),
                'Sample Type': rows[1].lower().strip(),
                'Units': rows[2].lower().strip(),
                'Limit': rows[3],
                'Appearance': rows[4].lower().strip(),
                'Analyte Result': rows[5],
                'Other-Peaks': rows[6],
                })
    return sample_list


def sample_list_checker(sample_list):
    for dicts in sample_list:
        if (dicts['Sample Type'] != 'blank' and
                dicts['Sample Type'] != 'sample'):
            sys.exit(f'Sample Type for {dicts['Sample ID']} is not of type "Blank" or "Sample"')
        elif (dicts['Units'] != 'ug/ml' and
                dicts['Units'] != 'ug/100cm2'):
            sys.exit(f'Units for {dicts['Sample ID']} is not either "ug/mL" or "ug/100cm2"')
        elif not isinstance(dicts['Limit'], (int, float)):
            sys.exit(f'Limit for {dicts['Sample ID']} is non-numerical')
        elif (dicts['Appearance'] != 'pass' and
                dicts['Appearance'] != 'fail'):
            sys.exit(f'Appearance for {dicts['Sample ID']} is not either "Pass" or "Fail"')
        elif not isinstance(dicts['Analyte Result'], (int, float)):
            sys.exit(f'Analyte Result for {dicts['Sample ID']} is non-numerical')
        elif not dicts['Other-Peaks']:
            continue
        elif not isinstance(dicts['Other-Peaks'], (str)):
            sys.exit(f'Other-Peak(s) entrie(s) for {dicts['Sample ID']} not in proper format. Please fix and try again.')
        else:
            try:
                list_of_other_peaks = dicts['Other-Peaks'].split('), (')
            except ValueError:
                sys.exit(f'Other-Peak(s) entrie(s) for {dicts['Sample ID']} not in proper format. Please fix and try again.')
            else:
                list_of_other_peaks_dicts = []
                for pairs in list_of_other_peaks:
                    try:
                        _ = pairs.strip('()').split(',')
                        list_of_other_peaks_dicts.append({
                            'Retention Time': float(_[0].strip('()')),
                            'Concentration': float(_[1].strip('()'))
                            })
                        dicts['Other-Peaks'] = list_of_other_peaks_dicts
                    except ValueError:
                        sys.exit(f'Other-Peak(s) entrie(s) for {dicts['Sample ID']} not in proper format. Please fix and try again.')
    return sample_list


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


if __name__ == "__main__":
    main()
