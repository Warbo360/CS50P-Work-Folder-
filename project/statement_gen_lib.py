# function that generates the actual statements for samples in the handed sample set
# Each line broke into its own fucntion:
    # Sample Info Line (LCXXXXX [Blank if blank])
    # AR found or not, needs to check against limit
        # If >= APQL report as is.
        # If < APQL report as "< APQL"
    # Other peaks, needs to check against limit
        # If greater than or equal APQL report as is to two decimals
        # If less than APQL report as "< APQL"
    # Total, needs to check sample units (ideally all samples should have the same but as is does allow mixing of rinse and swab results...) to deter-
    # mine swab or rinse
        # If ug/mL than just sum otheres with AR and report as it
        # If ug/100cm2 sum just the other peaks and if <= to 400 report as pass, if greater than report as fail


# Handler function that directs to other functions
def state_gen(sample_set_list):
    statement = ''
    for samples in sample_set_list:
        statement.append(sample_info_state(sample_set_list))
        statement.append(sample_AR_state(sample_set_list))
        statement.append(sample_other_state(sample_set_list))
        if sample['Units'] == 'ug/ml':
            statement.append(other_rinse_state(sample_set_list))
        else:
            statement.append(other_swab_state(sample_set_list))
    statement.append('\n')
    return statement