# Overview
# ------------------------------------------------------------------------
#
# Save the values on the input file in a dictionary(variable - exp_dict)
# The key-value pair in this dictionary is defined as
# <value_in_file>: 2020 - <value_in_file> e.g. { 1020: 1000, ...}
# Iterate over the dictionary to see if the value component exists
# in the dictioanry. If it does, the pair has been found
# multilpy the key and value component to get the result, break out of
# loop
#
# ------------------------------------------------------------------------

with open('input.txt', 'r') as f:
    exp_dict = {
        exp: 2020 - exp for exp in
        sorted([int(exp.replace('\n', '')) for exp in f.readlines()])
    }

for key, value in exp_dict.items():
    if value in exp_dict.keys():
        print(f'Entry 1: {key}\n'
        	   'Entry 2: {value}\n'
        	   'Result: {key * value}')
        break
