# Lib for functions that generate sample statment, takes a dict of dicts as inputs


# wrapper function that checks to see if APQLs given correlate to swabs or not
# then comparative logic that points each entru to its associated statment generator
def rinse_sample_gen(sample_list):
    for dicts in sample_list['Sample List']:
# Permutation of all passing blank sample
        if (dicts['Sample Type'].lower().strip() == 'blank' and
        dicts['Appearance'].lower().strip() == 'pass' and
        isinstance(sample_list['Limit'], (int, float)) and
        dicts['A-Result'] < sample_list['Limit']):
            passing_rinse_blank(sample_list, dicts)
# Permutation of all passing except appearance for blank rinse sample
        elif (dicts['Sample Type'].lower().strip() == 'blank' and
        dicts['Appearance'].lower().strip() == 'fail' and
        isinstance(sample_list['Limit'], (int, float)) and
        dicts['A-Result'] < sample_list['Limit']):
            pass_fail_rinse_blank(sample_list, dicts)
# Permutation of failing blank but passing appearance
        elif (dicts['Sample Type'].lower().strip() == 'blank' and
        dicts['Appearance'].lower().strip() == 'pass' and
        isinstance(sample_list['Limit'], (int, float)) and
        dicts['A-Result'] > sample_list['Limit']):
            fail_pass_rinse_blank(sample_list, dicts)
# Permuation of failing appearance and A Result for blanks
        elif (dicts['Sample Type'].lower().strip() == 'blank' and
        dicts['Appearance'].lower().strip() == 'fail' and
        isinstance(sample_list['Limit'], (int, float)) and
        dicts['A-Result'] > sample_list['Limit']):
            fail_rinse_blank(sample_list, dicts)
# Permuation of all passing normal rinse samp with A-Result not detected (excel cell = 0)
        elif (dicts['Sample Type'].lower().strip() == 'sample' and
        dicts['Appearance'].lower().strip() == 'pass' and
        isinstance(sample_list['Limit'], (int, float)) and
        dicts['A-Result'] == 0):
            zero_pass_rinse_sample(sample_list, dicts)
# Permutation of passing rinse with detected A-result but still less than APQL
        elif (dicts['Sample Type'].lower().strip() == 'sample' and
        dicts['Appearance'].lower().strip() == 'pass' and
        isinstance(sample_list['Limit'], (int, float)) and
        sample_list['Limit'] > dicts['A-Result'] > 0):
            less_APQL_pass_rinse_sample(sample_list, dicts)
# Permutation of passing rinse sample with A-result greather than or equal to APQL
        elif (dicts['Sample Type'].lower().strip() == 'sample' and
        dicts['Appearance'].lower().strip() == 'pass' and
        isinstance(sample_list['Limit'], (int, float)) and
        dicts['A-Result'] >= sample_list['Limit']):
            greater_APQL_pass_rinse_sample(sample_list, dicts)
# Permutation of failng Appearance and AR not detected rinse sample
        elif (dicts['Sample Type'].lower().strip() == 'sample' and
        dicts['Appearance'].lower().strip() == 'fail' and
        isinstance(sample_list['Limit'], (int, float)) and
        dicts['A-Result'] == 0):
            zero_fail_rinse_sample(sample_list, dicts)
# Permuatatuon of failong Appearance and AP < APQL rinse sample
        elif (dicts['Sample Type'].lower().strip() == 'sample' and
        dicts['Appearance'].lower().strip() == 'fail' and
        isinstance(sample_list['Limit'], (int, float)) and
        sample_list['Limit'] > dicts['A-Result'] > 0):
            less_APQL_fail_rinse_sample(sample_list, dicts)
# Permutation of failing Appearance and AR >= APQL rinse sample
        elif (dicts['Sample Type'].lower().strip() == 'sample' and
        dicts['Appearance'].lower().strip() == 'fail' and
        isinstance(sample_list['Limit'], (int, float)) and
        dicts['A-Result'] >= sample_list['Limit']):
            greater_APQL_fail_rinse_sample(sample_list, dicts)
        


# Passing rinse blank perm
def passing_rinse_blank(sample_list, dicts):
    if isinstance(dicts['Other-Peak(s)'], (int, float)):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/mL. Reported as 'Pass'.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/mL.''')
    elif isinstance(dicts['Other-Peak(s)'], str):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Peak(s) detected at {' ug/mL,'.join(dicts['Other-Peak(s)'].split(','))} ug/mL. Reported as 'Pass'.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/mL.''')
    else:
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Not detected. Reported as 'Pass'.''')


# Passing A-R, Failing Appearance, Rinse Blank
def pass_fail_rinse_blank(sample_list, dicts):
    if isinstance(dicts['Other-Peak(s)'], (int, float)):
                print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/mL. Reported as 'Pass'.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/mL.''')
    elif isinstance(dicts['Other-Peak(s)'], str):
                print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Peak(s) detected at {' ug/mL,'.join(dicts['Other-Peak(s)'].split(','))} ug/mL. Reported as 'Pass'.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/mL.''')
    else:
                print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Not detected. Reported as 'Pass'.''')


# Failing AR but passing appearance blank rinse
def fail_pass_rinse_blank(sample_list, dicts):
            if isinstance(dicts['Other-Peak(s)'], (int, float)):
                print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as 'Fail'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/mL. Reported as 'Fail'.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/mL.''')
            elif isinstance(dicts['Other-Peak(s)'], str):
                print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as 'Fail'.
Other Peak(s): Peak(s) detected at {' ug/mL,'.join(dicts['Other-Peak(s)'].split(','))} ug/mL. Reported as 'Fail'.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Total-Peak(s)']} ug/mL.''')
            else:
                print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as 'Fail'.
Other Peak(s): Not detected. Reported as 'Pass'.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['A-Result']} ug/mL.''')


# Failing AR and appearance for rinse blanks
def fail_rinse_blank(sample_list, dicts):
    if isinstance(dicts['Other-Peak(s)'], (int, float)):
                print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as 'Fail'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/mL. Reported as 'Fail'.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/mL.''')
    elif isinstance(dicts['Other-Peak(s)'], str):
                print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as 'Fail'.
Other Peak(s): Peak(s) detected at {' ug/mL,'.join(dicts['Other-Peak(s)'].split(','))} ug/mL. Reported as 'Fail'.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Total-Peak(s)']} ug/mL.''')
    else:
                print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as 'Fail'.
Other Peak(s): Not detected. Reported as 'Fail'.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['A-Result']} ug/mL.
''')


# Zero AR and passing appearance generator for rinse samples
def zero_pass_rinse_sample(sample_list, dicts):
    if isinstance(dicts['Other-Peak(s)'], (int, float)):
                print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: No peak detected. Reported as '< {sample_list['Limit']} ug/mL (<APQL)'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/mL.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/mL.''')
    elif isinstance(dicts['Other-Peak(s)'], str):
                print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: No peak detected. Reported as '< {sample_list['Limit']} ug/mL (<APQL)'.
Other Peak(s): Peak(s) detected at {' ug/mL,'.join(dicts['Other-Peak(s)'].split(','))} ug/mL.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Total-Peak(s)']} ug/mL.''')
    else:
                print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: No peak detected. Reported as '< {sample_list['Limit']} ug/mL (<APQL)'.
Other Peak(s): Not detected.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['A-Result']} ug/mL.''')


# < APQL and passing appearance generator for risne samples
def less_APQL_pass_rinse_sample(sample_list, dicts):
    if isinstance(dicts['Other-Peak(s)'], (int, float)):
                print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as '< {sample_list['Limit']} ug/mL (<APQL)'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/mL.
Total({sample_list['Analyte']} + Other Peak(s)): < {dicts['Summed-Other-Peak(s)']+sample_list['Limit']} ug/mL.''')
    elif isinstance(dicts['Other-Peak(s)'], str):
                print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as '< {sample_list['Limit']} ug/mL (<APQL)'.
Other Peak(s): Peak(s) detected at {' ug/mL,'.join(dicts['Other-Peak(s)'].split(','))} ug/mL.
Total({sample_list['Analyte']} + Other Peak(s)): < {dicts['Summed-Total-Peak(s)']} ug/mL.''')
    else:
                print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as '< {sample_list['Limit']} ug/mL (<APQL)'.
Other Peak(s): Not detected.
Total({sample_list['Analyte']} + Other Peak(s)): < {sample_list['Limit']} ug/mL (<APQL).''')


# >= APQL and passing appearance generator for rinse samples
def greater_APQL_pass_rinse_sample(sample_list, dicts):
    if isinstance(dicts['Other-Peak(s)'], (int, float)):
                print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as '{dicts['A-Result']} ug/mL'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/mL.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Other-Peak(s)']+dicts['A-Result']} ug/mL.''')
    elif isinstance(dicts['Other-Peak(s)'], str):
                print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as '{dicts['A-Result']} ug/mL'.
Other Peak(s): Peak(s) detected at {' ug/mL,'.join(dicts['Other-Peak(s)'].split(','))} ug/mL.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Other-Peak(s)']+dicts['A-Result']} ug/mL.''')
    else:
                print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as '{dicts['A-Result']} ug/mL'.
Other Peak(s): Not detected.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['A-Result']} ug/mL.''')


# Zero AR and failing appearance generator for rinse samples
def zero_fail_rinse_sample(sample_list, dicts):
    if isinstance(dicts['Other-Peak(s)'], (int, float)):
                print(f'''
{dicts['Sample ID']}
Appearance and Color: More intensely colored and not clear. Reported as 'Fail'.
{sample_list['Analyte']}: No peak detected. Reported as '< {sample_list['Limit']} ug/mL (<APQL)'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/mL.
Total({sample_list['Analyte']} + Other Peak(s)): < {dicts['Summed-Other-Peak(s)']+sample_list['Limit']} ug/mL.''')
    elif isinstance(dicts['Other-Peak(s)'], str):
                print(f'''
{dicts['Sample ID']}
Appearance and Color: More intensely colored and not clear. Reported as 'Fail'.
{sample_list['Analyte']}: No peak detected. Reported as '< {sample_list['Limit']} ug/mL (<APQL)'.
Other Peak(s): Peak(s) detected at {' ug/mL,'.join(dicts['Other-Peak(s)'].split(','))} ug/mL.
Total({sample_list['Analyte']} + Other Peak(s)): < {dicts['Summed-Total-Peak(s)']+sample_list['Limit']} ug/mL.''')
    else:
                print(f'''
{dicts['Sample ID']}
Appearance and Color: More intensely colored and not clear. Reported as 'Fail'.
{sample_list['Analyte']}: No peak detected. Reported as '< {sample_list['Limit']} ug/mL (<APQL)'.
Other Peak(s): Not detected.
Total({sample_list['Analyte']} + Other Peak(s)): < {sample_list['Limit']} ug/mL (<APQL).''')


# < APQL and failing appearance generator for rinse samples
def less_APQL_fail_rinse_sample(sample_list, dicts):
    if isinstance(dicts['Other-Peak(s)'], (int, float)):
                print(f'''
{dicts['Sample ID']}
Appearance and Color: More intensely colored and not clear. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as '< {sample_list['Limit']} ug/mL (<APQL)'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/mL.
Total({sample_list['Analyte']} + Other Peak(s)): < {dicts['Summed-Other-Peak(s)']+sample_list['Limit']} ug/mL.''')
    elif isinstance(dicts['Other-Peak(s)'], str):
                print(f'''
{dicts['Sample ID']}
Appearance and Color: More intensely colored and not clear. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as '< {sample_list['Limit']} ug/mL (<APQL)'.
Other Peak(s): Peak(s) detected at {' ug/mL,'.join(dicts['Other-Peak(s)'].split(','))} ug/mL.
Total({sample_list['Analyte']} + Other Peak(s)): < {dicts['Summed-Other-Peak(s)']+sample_list['Limit']} ug/mL.''')
    else:
                print(f'''
{dicts['Sample ID']}
Appearance and Color: More intensely colored and not clear. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as '< {sample_list['Limit']} ug/mL (<APQL)'.
Other Peak(s): Not detected.
Total({sample_list['Analyte']} + Other Peak(s)): < {sample_list['Limit']} ug/mL (<APQL).''')


# >= APQL and failing appearance generator for rinse samples
def greater_APQL_fail_rinse_sample(sample_list, dicts):
    if isinstance(dicts['Other-Peak(s)'], (int, float)):
                print(f'''
{dicts['Sample ID']}
Appearance and Color: More intensely colored and not clear. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as '{dicts['A-Result']} ug/mL'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/mL.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Other-Peak(s)']+dicts['A-Result']} ug/mL.''')
    elif isinstance(dicts['Other-Peak(s)'], str):
                print(f'''
{dicts['Sample ID']}
Appearance and Color: More intensely colored and not clear. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as '{dicts['A-Result']} ug/mL'.
Other Peak(s): Peak(s) detected at {' ug/mL,'.join(dicts['Other-Peak(s)'].split(','))} ug/mL.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['Summed-Other-Peak(s)']+dicts['A-Result']} ug/mL.''')
    else:
                print(f'''
{dicts['Sample ID']}
Appearance and Color: More intensely colored and not clear. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/mL. Reported as '{dicts['A-Result']} ug/mL'.
Other Peak(s): Not detected.
Total({sample_list['Analyte']} + Other Peak(s)): {dicts['A-Result']} ug/mL.''')