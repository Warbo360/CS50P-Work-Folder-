def state_gen(sample_set_list):
    statement = ''
    for samples in sample_set_list:
        statement = (
                statement +
                sample_info_state(samples) +
                sample_appearance_state(samples) +
                sample_AR_state(samples) +
                sample_other_state(samples) +
                sample_total_state(samples) +
                '\n')
    return statement


def sample_info_state(sample):
    if sample['Sample Type'] == 'blank':
        return f'{sample['Sample ID']} Blank\n'
    else:
        return f'{sample['Sample ID']}\n'


def sample_appearance_state(sample):
    if sample['Sample Type'] == 'blank' \
            and sample['Appearance'] == 'pass':
        return 'Appearance and Color: Clear and colorless. Reported as "Pass".\n'
    elif sample['Sample Type'] == 'blank' \
            and sample['Appearance'] == 'fail':
        return 'Appearance and Color: Not clear and/or not colorless. Reported as "Fail".\n'
    elif sample['Sample Type'] == 'sample' \
            and sample['Appearance'] == 'pass':
        return 'Appearance and Color: Clear and not more intensely colored than blank sample(s). Reported as "Pass".\n'
    else:
        return 'Appearance and Color: not clear and/or more intensely colored than blank sample(s). ' \
               'Reported as "Fail".\n'


def sample_AR_state(sample):
    if sample['Sample Type'] == 'blank':
        if sample['Analyte Result'] < sample['Limit'] * 0.5:
            return f'{sample['Analyte']}: Not detected. Reported as "Pass".\n'
        else:
            return f'{sample['Analyte']}: Detected. RT {sample['Analyte RT']} min = {sample['Analyte Result']:.2f}'\
                   f'{sample['Units']}. Reported as "Fail".\n'
    else:
        if sample['Analyte Result'] < sample['Limit'] * 0.5:
            return f'{sample['Analyte']}: Not detected. Reported as "< {sample['Limit']} {sample['Units']} (APQL)".\n'
        elif sample['Limit'] > sample['Analyte Result'] >= sample['Limit'] * 0.5:
            return f'{sample['Analyte']}: Detected. RT {sample['Analyte RT']} min = {sample['Analyte Result']:.2f}'\
                   f'{sample['Units']}. Reported as "< {sample['Limit']} {sample['Units']} (APQL)".\n'
        elif sample['Analyte Result'] >= sample['Limit']:
            return f'{sample['Analyte']}: Detected. RT {sample['Analyte RT']} min = {sample['Analyte Result']:.2f}'\
                   f'{sample['Units']}. Reported as "{sample['Analyte Result']} {sample['Units']}".\n'


def sample_other_state(sample):
    other_str = 'Other Peaks: '
    if not sample['Other-Peaks']:
        other_str = 'Other Peak(s): Not detected.'
        return f'{other_str}\n'
    else:
        other_str = other_str + 'Detected. '
        for others in sample['Other-Peaks']:
            if others['Concentration'] >= sample['Limit']:
                other_str = other_str + f'{others['Retention Time']} min ='\
                                        f'{others['Concentration']} {sample['Units']}. '
            else:
                other_str = other_str + f'{others['Retention Time']} min ='\
                                        f' < {sample['Limit']} {sample['Units']} (APQL). '
        return f'{other_str}\n'


def sample_total_state(sample):
    if sample['Units'] == 'ug/ml' \
            and sample['Other-Peaks']:
        return rinse_state_gen_yes_other(sample)
    elif sample['Units'] == 'ug/ml' \
            and not sample['Other-Peaks']:
        return rinse_state_gen_no_other(sample)
    elif sample['Units'] == 'ug/100cm2' \
            and not sample['Other-Peaks']:
        return 'Total Other Peak(s): Not detected. Reported as "Pass". \n'
    else:
        return swab_total_state_gen(sample)


def other_peak_limit_check(sample, total_state, others_total):
    for others in sample['Other-Peaks']:
        if others['Concentration'] >= sample['Limit']:
            total_state = total_state + f'+ {others['Concentration']} {sample['Units']} '
            others_total = others_total + others['Concentration']
        else:
            total_state = total_state + f'+ < {sample['Limit']} {sample['Units']} '
            others_total = others_total + sample['Limit']
    return (total_state, others_total)


def rinse_greater_state_gen(sample):
    total_state = f'Total({sample['Analyte']} + Other Peak(s)):'\
                  f'{sample['Analyte Result']} {sample['Units']} '
    others_total = sample['Analyte Result']
    total_state, others_total = other_peak_limit_check(sample, total_state, others_total)
    if '<' in total_state:
        return total_state + f'= < {others_total} {sample['Units']}. \n'
    else:
        return total_state + f'= {others_total} {sample['Units']}. \n'


def rinse_fewer_state_gen(sample):
    total_state = f'Total({sample['Analyte Result Result']} + Other Peak(s)):'\
                  f'< {sample['Limit']} {sample['Units']} '
    others_total = sample['Limit']
    total_state, others_total = other_peak_limit_check(sample, total_state, others_total)
    if '<' in total_state:
        return total_state + f'= < {others_total} {sample['Units']}. \n'
    else:
        return total_state + f'= {others_total} {sample['Units']}. \n'


def rinse_state_gen_yes_other(sample):
    if sample['Analyte Result'] >= sample['Limit']:
        return rinse_greater_state_gen(sample)
    else:
        return rinse_fewer_state_gen(sample)


def rinse_state_gen_no_other(sample):
    if sample['Analyte Result'] >= sample['Limit']:
        return f'Total({sample['Analyte']} and Other Peak(s)): {sample['Analyte Result']} {sample['Units']}.\n'
    else:
        return f'Total({sample['Analyte']} and Other Peak(s)): {sample['Limit']} {sample['Units']}.\n'


def swab_other_state_gen(sample, total_state, others_total):
    for others in sample['Other-Peaks']:
        _ = 0
        if others['Concentration'] >= sample['Limit']\
                and _ < 1:
            total_state = total_state + f'{others['Concentration']} {sample['Units']}.'
            others_total = others_total + others['Concentration']
        elif others['Concentration'] >= sample['Limit']\
                and _ >= 1:
            total_state = total_state + f'+ {others['Concentration']} {sample['Units']} '
            others_total = others_total + others['Concentration']
        elif others['Concentration'] < sample['Limit']\
                and _ < 1:
            total_state = total_state + f'< {sample['Limit']} {sample['Units']}.'
            others_total = others_total + sample['Limit']
        else:
            total_state = total_state + f'+ < {sample['Limit']} {sample['Units']} '
            others_total = others_total + sample['Limit']
    return (total_state, others_total)


def swab_total_state_gen(sample):
    total_state = 'Total Other Peak(s): '
    others_total = 0
    total_state, others_total = swab_other_state_gen(sample, total_state, others_total)
    if len(sample['Other-Peaks']) > 1:
        if others_total >= 400\
                and '<' in total_state:
            return total_state + f'= < {others_total} {sample['Units']}. Which is NLT than 400 ug/100cm2. '\
                                 f'Reported as "Fail".\n'
        elif others_total < 400\
                and '<' in total_state:
            return total_state + f'= < {others_total} {sample['Units']}. Which is NMT than 400 ug/100cm2. '\
                                 f'Reported as "Pass".\n'
        elif others_total >= 400:
            return total_state + f'= {others_total} {sample['Units']}. Which is NLT than 400 ug/100cm2. '\
                                 f'Reported as "Fail".\n'
        else:
            return total_state + f'= {others_total} {sample['Units']}. Which is NMT than 400 ug/100cm2. '\
                                 f'Reported as "Pass".\n'
    else:
        if others_total >= 400\
                and '<' in total_state:
            return total_state + ' Which is NLT than 400 ug/100cm2. '\
                                 'Reported as "Fail".\n'
        elif others_total < 400\
                and '<' in total_state:
            return total_state + ' Which is NMT than 400 ug/100cm2. '\
                                 'Reported as "Pass".\n'
        elif others_total >= 400:
            return total_state + ' Which is NLT than 400 ug/100cm2. '\
                                 'Reported as "Fail".\n'
        else:
            return total_state + ' Which is NMT than 400 ug/100cm2. '\
                                 'Reported as "Pass".\n'
