"""
Project will take user inputs procedurially and after
inputs are taken program is to generate scientific statments
for cleaning samples (Swab & Rinse) in an variety of possible
forms based on the what the user wants
(so CSV, straight text, or formatted table).
Relavent for automating reporting of scientific as the structure of these
satements are rather similar/exactlly the same from sample to sample
in a given sample set.

Might need two seperate formatters if excel sheet is passed or
user just passes results as straight csv values
"""


# def main():


"""
Can ask for procedurial fill in or ask to pass excel sheet
Calls function that will procedurally ask user for relavent
for a given sample set,
    Swabs or Rinse? A#? APQL?
        Swabs: Sample list with material swabbed, might have multiple APQLs
            atts of swabs: Blank/Sample, Material, Name, Sample ID, A# Result,
            Other Result, Appearance
        Rinse: Should jsut be one APQL
            Atts of Rinse: Blank/Sample, Name, Sample ID, A# Result,
            Other Result, Appearance


If values passed do not conform to format needed for rinse or swab
pass error asking user again for proper format or telling them
to <C-c> to stop program


function () orientates data into a dict of
sample info key, and data value pairs for both target
analyte and other(s) non-target analyte data value pairs
ex: {Sample Name, [A#,Other(s)]} then each dict in a list like so:

APQL = "APQL float here"
APQL unit = "Str Here (ug/mL or ug/100cm2)"
Sample Lot = "Str Here"


Sample Set Name = [
    {Sample_Name_1, [
        Blank/Sample,
        Material (if Swab),
        Sample ID,
        Appearance,
        A#,
        Other(s)
    ]},
    {Sample_Name_2, [
        Blank/Sample,
        Material (if Swab),
        Sample ID,
        Appearance,
        A#,
        Other(s)
    ]},
    {Sample_Name_3, [
        Blank/Sample,
        Material (if Swab),
        Sample ID,
        Appearance,
        A#,
        Other(s)
    ]},
]


Thus program should ask for # of samples and then loop over that many
iterations to generate that many dicts in the list


Next will use APQL to to set conditionals for blank(s) and samples:
A#:
    if < APQL then reports as "< X.XX ug/XX (APQL)"
    if >= APQL report as is to same sig figs as APQL:
        "X.XX ug/XX" (APQL to two decimals)
Other(s):
    if < (1/3) APQL then not reported typically.
    if > (1/3) APQL but < APQL report as "< X.XX ug/XX (APQL)"
    if > APQL then report as "X.XX ug/XX"
    Additionally for swabs add other add other non-analyte
    peaks and give pass or fail result with a limit of 400 ug/100cm2
    If rinse add analyte & other peaks to give total (note for both
    that if any result is reported as < APQL than statment needs
    such equalitly in the statment)
    if < APQL then print such that it reads
    "A# is reported as 'A# < X.XX ug/mL (<APQL)'"
    if the sample is a blank sample, output should give pass or fail result.


Next ask for csv values of A# that correspond in same order as samples given
to then temp store for total print generation.
    Another possiblity to all of this is passing a formatted
    excel sheet that can take all of this info automatically
"""
# #NOTE: Can just be a list as only one A# per sample
# #NOTE: Has to be list of dicts again as any number of additional reportable
# #NOTE: peaks can exist for any given sample.


"""
function() to generate statement for just one sample, have it iterate over whole
dict of sample set that will be saved
"""


# main()
