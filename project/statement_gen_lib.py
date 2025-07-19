def state_gen(sample_set_list):
    statement = ''
    for samples in sample_set_list:
        statement = (
                statement +
                sample_info_state(samples) +
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
            if others['Concentration'] > sample['Limit']:
                other_str = other_str + f'{others['Retention Time']} min ='\
                                        f'{others['Concentration']} {sample['Units']}. '
            else:
                other_str = other_str + f'{others['Retention Time']} min ='\
                                        f'< {sample['Limit']} {sample['Units']} (APQL). '
        return f'{other_str}\n'


def sample_total_state(sample):
    ...
