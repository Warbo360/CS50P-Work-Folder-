"""
Project will take user inputs procedurially and after
inputs are taken program is to generate scientific statments
for cleaning samples (Swab & Rinse) in an variety of possible
forms based on the what the user wants
(so CSV, straight text, or formatted table).
Relavent for automating reporting of scientific as the structure of these
satements are rather similar/exactlly the same from sample to sample
in a given sample set.
"""


def main():


"""
Calls function that will procedurally ask user for relavent
for a given sample set, orientates data into a dict of
sample info key, and data value pairs for both target
analyte and other(s) non-target analyte data value pairs
ex: {Sample Name, [A#,Other(s)]} then each dict in a list like so:
Sample Set Name = [
    {Sample_Name_1, [A#, Other(s)]},
    {Sample_Name_2, [A#, Other(s)]},
    {Sample_Name_3, [A#, Other(s)]},
]


Thus program should ask for # of samples and then loop over that many
iterations to generate that many dicts in the list


Next will ask for APQL, one to know sig figs, two to set conditionals
of statment generation ie:
    if < APQL then print such that it reads "A# is reported as 'A# < X.XX ug/mL (<APQL)'"


Next ask for csv values of A# that correspond in same order as samples given
to then temp store for total print generation.
"""
#NOTE: Can just be a list as only one A# per sample


"""
Next ask for csv values of other(s) data also corresponding in same order
as sampels generated
"""
#NOTE: Has to be list of dicts again as any number of additional reportable
#NOTE: peaks can exist for any given sample.


main()
