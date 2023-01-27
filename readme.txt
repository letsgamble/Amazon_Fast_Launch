##################### Version #####################
1.3 - Beta Version

##################### Author ######################
@kawesolo

##################### Overview #####################
Amazon Fast Launch is a tool created
for the automated selection of the
Parent Classes based on provided Child
Classes list.

##################### Features #####################
-Recognizing 'no action needed' and
'no chanages needed' based on
'Root Cause' column
-Recognizing 'merge' tickets based on
'Root Cause Details'

###################### Usage ######################
In the program directory please provide
two files (case sensitive):
weekly.xlsx - Classes list, provided on a
weekly basis
tcorp.csv - Finished tickets exported from
the t.corp (columns 'Title', 'RootCause',
           ('RootCauseDetails' must be in)
Output will be saved in 'To_launch.csv'.

################ Technology Stacks ################
Python, Pandas

#################### Compile ######################
pyinstaller --onefile --icon=engine.ico --noconsole engine.py

################### Source Code ###################
https://github.com/letsgamble/Amazon_Fast_Launch