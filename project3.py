# Write a script in Python that converts British spelling of a text to the American spelling
# using at least two generalizable replacement patterns.
# “Generalizable” means applicable to more than one lexeme.
# For example, replacing “fireman” with “firefighter” is not generalizable,
# but replacing “theatre” with “theater” is. Your script should read an input text file
# and write an output text file. The names of the input and output files may be hard-coded in the script.

import re

string = open('proj3.txt').read()
string = re.sub(r'our', r'or', string, flags=re.I | re.M)
print(string)
