# GMP Cleaning Sample Summary Generator
#### [Video Demo](https://youtu.be/Sq_S1Fzg-ms)
#### Description:

This program is designed for reading of standardized spreadsheet files
that have been filled in with GMP (Good Manufacturing Practices) Cleaning Samples
for my place of work in the pharmaceutical industry. The idea being that due to
this work being GMP, that these summaries often should look the same from set to
set, and thus can be given a rather cookie cutter approach in their construction
which works well with automating the task at large. This also should ideally
limit style deviations from sample to sample in a given set and deviations of style
between sample sets as a whole. It should also limit errors id data transcription
from CDS software into a summary statement as long as the spreadsheet is filled
correctly (although ideally this program has error handling for inappropriate
entries in the standardized sheet).


#### Project.py
The main project.py file holds functions that actually open the given spreadsheet in the form of of a CLI argument.
If the given file does not exist or is not an '.xlsx' file there is error handling for this that just exits the program
and gives the user a error message on either the file not existing or not being the right file type.

Assuming the file given does exist though and is the correct file type, the functions after will parse the spreadsheet
in a specific way, and thus if the active worksheet is not laid out in the proper way, there is also error handling for this
as well that will exit the program and notify the user that something in incorrect or missing altogether. Assuming that is all
correct though the functions will parse the active sheet and create a sample set data dictionary and organize those dictionaries
into a list, this list is put into a greater dictionary of other sample set information like various analyte limit(s) and name of
the analyte. There is a function that reads a cell for the number of samples, but it is unused as the function that gathers sample
set data generates the needed number of dictionaries for the amount of samples that are filled in.
Other features of the file is the importing of OpenPyXL, a pip-installable library that handles the reading and writing of spreadsheet
files. This program only makes use of reading spreadsheet files and does not manipulate the given file in anyway.
Also imported are the included python libraries 'sys' and 're' for sys.exit() on error handling, and regex checking of '.xlsx' files.



#### Statement Gen Lib.py
This file that sits in the root directory of the project is a file that takes the gathered by project.py and uses it to determine what
statement needs generating on a sample-to-sample basis. None of these functions are tested via pytest directly as the idea being if
the functions that gather the data to begin with are test properly there should be minimal error handling needed in the generator file.
I do plan on implementing unit tests on these functions in the future though regardless. The main feature of this file is the logic used
to direct the input as it reads a given samples info from its handed dictionary to decide if it a blank or sample type, swab or rinse,
if its result for the target analyte exceeds the given limit (listed as APQL in code) of the analyte, and can handle none, single, and comma
separated numerical values for the non-analyte peaks reported as well. The functions of interest for generating swab or rinse samples is then
imported in project.py for use in there.


#### Test_Project.py
Unit tests for the main functions that read the given spreadsheets to test for proper output types, and error handling of incorrect or missing information
about the file and in the spreadsheet like missing or incorrect data types in certain cells of the spreadsheet. Imports pytest for the checking of types of
errors or events raised with pytest.raises(). Imports the previously mentioned OpenPyXL in the use of a custom load_workbook function for loading a test bank
or spreadsheets that test for a particular output or error to be handled. Also imports sys to be able to check for SystemExit event in the error handling.


#### Test_Spreadsheets/
A bank of spreadsheets that are used in conjunction with test_project.py. These spreadsheets are hard coded inputs of the test functions that use them to still
allows for just the '$ pytest test_project.py' syntax in the CLI to still properly test the file without needed special handling of arguments to pytest.
