# Input Values
# ---------------------------------------------------------------------
# Values provided by AoC saved into a file input.txt
# Create a soreted list of the values in the file
#
# ---------------------------------------------------------------------

with open('input.txt', 'r') as f:
    exp_list = sorted([int(exp.replace[:-1]) for exp in f.readlines()])

# Part 1: if n1 + n2 = 2020 then result = n1 * n2
# ---------------------------------------------------------------------
# 
# Using list exp_list create a dictionary with key: value pairs defined
# as <element_in_list>: 2020 - <element_in_list> e.g. {1000: 1020,...}
# The dictionary is populated only if the value comopnent exists in the
# list exp_list. The dictionary will only have two key-value pairs      
# like {n1: n2, n2: n1}. Taking the first pair we multiply key * value
# to get the result
#    
# ---------------------------------------------------------------------

exp_dict = {exp: 2020 - exp for exp in exp_list if 2020 - exp in exp_list}

n1 = next(iter(exp_dict))
n2 = exp_dict[n1]
result = n1 * n2
print(result)

# Part 2: if n1 + n2 + n3 = 2020 then result = n1 * n2 * n3 
# ---------------------------------------------------------------------
#
# Solution is a modification of the solution to Part 1
# For each element n1 in exp_list the maximum value for 
# (n2 + n3) = 2020 - n1
# exp_dict will now be key: value pairs defined as 
# <element_in_list>: <max_value> - <element_in_list>
# The dictionary is populated only if the value component exists in
# exp_list
# As was the case in Part 1, the result will only have two key-value
# pairs. Taking the first pair n2 = Key and n3 = Value
# (interchangeable)
# Multiply n1, n2 and n3 for the result
#
# ---------------------------------------------------------------------

n1 = exp_list.pop(0)
while exp_list:
    max_value = 2020 - n1
    exp_dict = {exp: max_value - exp for exp in exp_list if max_value - exp in exp_list}
    if exp_dict:
        n2 = next(iter(exp_dict))  # Get the first key in exp_dict
        n3 = exp_dict[n2]  # Value component for key n2 
        result = n1 * n2 * n3
    n1 = exp_list.pop(0)
    n -= 1
print(result)
