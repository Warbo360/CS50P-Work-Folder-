# Lib for functions that generate sample statment, takes a dict of dicts as inputs


# wrapper function that checks to see if APQLs given correlate to swabs or not
# then comparative logic that points each entru to its associated statment generator
def rinse_sample_gen(sample_list):
    for dicts in sample_list['Sample List']:
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


# Wrapper function for swab samples, will check filled in material type of a given sample and try and match
# to the Limit dict to "set" that samples APQL
def swab_sample_gen(sample_list):
    list_of_material_APQLs = sample_list['Limit']
    list_of_APQL = []
    for materials in list_of_material_APQLs:
        list_of_APQL.append(materials['APQL'])
    min_APQL = min(list_of_APQL)
    for dicts in sample_list['Sample List']:
        _ = 1
        if not dicts['Material']:
            # Passing blank swab
            if (dicts['Sample Type'].lower().strip() == 'blank' and
                dicts['Appearance'].lower().strip() == 'pass' and
                    dicts['A-Result'] < 0.5*min_APQL):
                passing_swab_blank(sample_list, dicts, list_of_APQL, materials)
                # Passing AR swab Failing appearance
            elif (dicts['Sample Type'].lower().strip() == 'blank' and
                  dicts['Appearance'].lower().strip() == 'fail' and
                  dicts['A-Result'] < 0.5*min_APQL):
                less_fail_swab_blank(sample_list, dicts, list_of_APQL, materials)
                # Failing AR swab Passing appearance
            elif (dicts['Sample Type'].lower().strip() == 'blank' and
                  dicts['Appearance'].lower().strip() == 'pass' and
                  dicts['A-Result'] > 0.5*min_APQL):
                greater_pass_swab_blank(sample_list, dicts, list_of_APQL, materials)
                # Failing swab
            elif (dicts['Sample Type'].lower().strip() == 'blank' and
                  dicts['Appearance'].lower().strip() == 'fail' and
                  dicts['A-Result'] > 0.5*min_APQL):
                fail_swab_blank(sample_list, dicts, list_of_APQL, materials)
        elif dicts['Material']:
            for materials in list_of_material_APQLs:
                if dicts['Material'].lower().strip() == materials['Material'].lower().strip():
                    # Passing sample swab non-detected AR
                    if (dicts['Sample Type'].lower().strip() == 'sample' and
                        dicts['Appearance'].lower().strip() == 'pass' and
                            dicts['A-Result'] == 0):
                        pass_swab_sample(sample_list, dicts, list_of_APQL, materials)
                    # Passing sample swab AR detected but < APQL for the material
                    elif (dicts['Sample Type'].lower().strip() == 'sample' and
                          dicts['Appearance'].lower().strip() == 'pass' and
                          dicts['A-Result'] < materials['APQL']):
                        less_pass_swab_sample(sample_list, dicts, list_of_APQL, materials)
                    # Passing sample swab AR >= APQL for the given material
                    elif (dicts['Sample Type'].lower().strip() == 'sample' and
                          dicts['Appearance'].lower().strip() == 'pass' and
                          dicts['A-Result'] >= materials['APQL']):
                        greater_pass_swab_sample(sample_list, dicts, list_of_APQL, materials)
                    # Passing swab AR (zero) failing appearance
                    elif (dicts['Sample Type'].lower().strip() == 'sample' and
                          dicts['Appearance'].lower().strip() == 'fail' and
                          dicts['A-Result'] == 0):
                        non_fail_swab_sample(sample_list, dicts, list_of_APQL, materials)
                    # Passing sample swab AR detected but < APQL for the material appearance fails
                    elif (dicts['Sample Type'].lower().strip() == 'sample' and
                          dicts['Appearance'].lower().strip() == 'fail' and
                          dicts['A-Result'] < materials['APQL']):
                        less_fail_swab_sample(sample_list, dicts, list_of_APQL, materials)
                    # Passing sample swab AR >= APQL for the given material appearance fails
                    elif (dicts['Sample Type'].lower().strip() == 'sample' and
                          dicts['Appearance'].lower().strip() == 'fail' and
                          dicts['A-Result'] >= materials['APQL']):
                        greater_fail_swab_sample(sample_list, dicts, list_of_APQL, materials)
                elif _ < len(list_of_material_APQLs):
                    _ = _ + 1
                    continue
                else:
                    print(f'{dicts['Sample ID']} listed material does not match any of the ones listed as swab materials')
                    break


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


# NOTE: Additional statment per senario needed for possible failing other peaks summed > 400 ug/100cm2


# Passing blank swab
def passing_swab_blank(sample_list, dicts, list_of_APQL, materials):
    if (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    else:
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Not detected. Reported as 'Pass'.''')


# Passing AR swab blank Failing appearance
def less_fail_swab_blank(sample_list, dicts, list_of_APQL, materials):
    if (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Not clear and colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Not clear and colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Not clear and colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Not clear and colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    else:
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Not clear and colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Pass'.
Other Peak(s): Not detected. Reported as 'Pass'.''')


# Failing AR swab blank Passing appearance
def greater_pass_swab_blank(sample_list, dicts, list_of_APQL, materials):
    if (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as 'Fail'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as 'Fail'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as 'Fail'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as 'Fail'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    else:
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Clear and Colorless. Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as 'Fail'.
Other Peak(s): Not detected. Reported as 'Pass'.''')


# Failing swab blank appearance and AR
def fail_swab_blank(sample_list, dicts, list_of_APQL, materials):
    if (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Not clear and colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as 'Fail'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Not clear and colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as 'Fail'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Not clear and colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as 'Fail'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Not clear and colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as 'Fail'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    else:
        print(f'''
{dicts['Sample ID']} Blank
Appearance and Color: Not clear and colorless. Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as 'Fail'.
Other Peak(s): Not detected. Reported as 'Pass'.''')


# Passing sample swab non-detected AR
def pass_swab_sample(sample_list, dicts, list_of_APQL, materials):
    if (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Not detected'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Not detected'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Not detected'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Not detected'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    else:
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Not detected'.
Other Peak(s): Not detected. Reported as 'Pass'.''')


# Passing sample swab AR detected but < APQL for the material
def less_pass_swab_sample(sample_list, dicts, list_of_APQL, materials):
    if (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '< {materials['APQL']} ug/100cm2 (APQL)'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '< {materials['APQL']} ug/100cm2 (APQL)'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '< {materials['APQL']} ug/100cm2 (APQL)'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '< {materials['APQL']} ug/100cm2 (APQL)'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    else:
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '< {materials['APQL']} ug/100cm2 (APQL)'.
Other Peak(s): Not detected. Reported as 'Pass'.''')


# Passing sample swab AR >= APQL for the given material
def greater_pass_swab_sample(sample_list, dicts, list_of_APQL, materials):
    if (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '{dicts['A-Result']} ug/100cm2'
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '{dicts['A-Result']} ug/100cm2'
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '{dicts['A-Result']} ug/100cm2'
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '{dicts['A-Result']} ug/100cm2'
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    else:
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Clear and not more intensely colored than the blank sample(s). Reported as 'Pass'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '{dicts['A-Result']} ug/100cm2'
Other Peak(s): Not detected. Reported as 'Pass'.''')


# Non-detected AR failing appearance on swab sample
def non_fail_swab_sample(sample_list, dicts, list_of_APQL, materials):
    if (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Not detected'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Not detected'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Not detected'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Not detected'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    else:
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak not detected. Reported as 'Not detected'.
Other Peak(s): Not detected. Reported as 'Pass'.''')


# Passing sample swab AR detected but < APQL for the material appearance fails
def less_fail_swab_sample(sample_list, dicts, list_of_APQL, materials):
    if (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '< {materials['APQL']} ug/100cm2 (APQL)'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '< {materials['APQL']} ug/100cm2 (APQL)'.
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '< {materials['APQL']} ug/100cm2 (APQL)'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '< {materials['APQL']} ug/100cm2 (APQL)'.
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    else:
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '< {materials['APQL']} ug/100cm2 (APQL)'.
Other Peak(s): Not detected. Reported as 'Pass'.''')


# Passing sample swab AR >= APQL for the given material appearance fails
def greater_fail_swab_sample(sample_list, dicts, list_of_APQL, materials):
    if (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '{dicts['A-Result']} ug/100cm2'
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], (int, float)) and
            dicts['Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '{dicts['A-Result']} ug/100cm2'
Other Peak(s): Peak(s) detected at {dicts['Other-Peak(s)']} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] < 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '{dicts['A-Result']} ug/100cm2'
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is < 400 ug/100cm2. Reported as 'Pass\'.''')
    elif (isinstance(dicts['Other-Peak(s)'], str) and
            dicts['Summed-Other-Peak(s)'] >= 400):
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '{dicts['A-Result']} ug/100cm2'
Other Peak(s): Peak(s) detected at {' ug/100cm2,'.join(dicts['Other-Peak(s)'].split(','))} ug/100cm2.
Total(Other Peak(s)): {dicts['Summed-Other-Peak(s)']} ug/100cm2. Which is >= 400 ug/100cm2. Reported as 'Fail\'.''')
    else:
        print(f'''
{dicts['Sample ID']}
Appearance and Color: Not clear and more intensely colored than blank sample(s). Reported as 'Fail'.
{sample_list['Analyte']}: Peak detected at {dicts['A-Result']} ug/100cm2. Reported as '{dicts['A-Result']} ug/100cm2'
Other Peak(s): Not detected. Reported as 'Pass'.''')
