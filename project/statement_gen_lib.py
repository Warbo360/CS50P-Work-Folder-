# Handler function that directs to other functions
def state_gen(sample_set_list):
    statement = ''
    for samples in sample_set_list:
        statement = statement + sample_info_state(samples) + sample_AR_state(samples)
        # statement.append(sample_AR_state(sample_set_list))
        # statement.append(sample_other_state(sample_set_list))
        # if sample['Units'] == 'ug/ml':
        #     statement.append(other_rinse_state(sample_set_list))
        # else:
        #     statement.append(other_swab_state(sample_set_list))
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
            return f'{sample['Analyte']}: Detected. RT {sample['Analyte RT']} = {sample['Analyte Result']} {sample['Units']}. Reported as "Fail".\n'
    else:
        if sample['Analyte Result'] < sample['Limit'] * 0.5:
            return f'{sample['Analyte']}: Not detected. Reported as "< {sample['Limit']} {sample['Units']} (APQL)".\n'
        elif sample['Limit'] > sample['Analyte Result'] >= sample['Limit'] * 0.5:
            return f'{sample['Analyte']}: Detected. RT {sample['Analyte RT']} = {sample['Analyte Result']}. Reported as "< {sample['Limit']} {sample['Units']} (APQL)".\n'
        elif sample['Analyte Result'] >= sample['Limit']:
            return f'{sample['Analyte']}: Detected. RT {sample['Analyte RT']} = {sample['Analyte Result']}. Reported as "{sample['Analyte Result']} {sample['Units']}".\n'
