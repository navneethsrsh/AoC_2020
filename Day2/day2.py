import datetime
# Day 2 AoC 2020

with open('input.txt', 'r') as f:
    checklist = [line.replace('\n','') for line in f.readlines()]

# Part 1
# ---------------------------------------------------------------------
#
    
valid = 0
for record in checklist:
    minimum = int(record[:record.index('-')])
    maximum = int(record[record.index('-') + 1:record.index(' ')])
    search = record[record.index(' ') + 1: record.index(':')]
    if minimum <= list(record.split(':')[-1]).count(search) <= maximum:
        valid += 1

print("Valid: " + str(valid))

# Part 2
# ---------------------------------------------------------------------
#

valid = 0
for record in checklist:
    pos1 = int(record[:record.index('-')])
    pos2 = int(record[record.index('-') + 1:record.index(' ')])
    search = record[record.index(' ') + 1: record.index(':')]
    pwd = record.split(':')[-1].lstrip()
    if search in set([pwd[pos1-1], pwd[pos2-1]]) and \
                len(set([pwd[pos1-1], pwd[pos2-1]])) != 1:
        valid +=1

print("Valid:" +  str(valid))
    