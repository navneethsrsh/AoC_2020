# Day 4 AoC 2020
# Solution 1 - Generic

def getnum_valid_passports(batch: list) -> int:
    """
    Count the number of valid passports
    
    Parameters
    -------------------------------------------------------------------
    batch: Batch of passport data represented in a list
    
    Return
    -------------------------------------------------------------------
    count: The count of valid passports
    
    Variables
    -------------------------------------------------------------------
    validation_keys: A defined set of keys which must exist
                     for a passport to be valid
    count: see Return
    data: List of keys available for each line of batch
    line: An element in batch
    kvp: Represents key-value pair for a line
    
    Info
    -------------------------------------------------------------------
    For each line in batch, a list of keys is generated (variable: data)
    If the list of keys in data includes all the keys in the set
    validation_keys then count is incremented to record a valid passport
    
    """
    
    validation_keys = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    count = 0
    data = []
    for line in batch:
        data = [kvp[:kvp.index(':')] for kvp in line.split()]
        count += (1 if validation_keys <= set(data) else 0)
        data.clear()
    return count


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()    
    batch = ' '.join([line[:-1] if line != '\n' else line 
                      for line in content]).replace(' \n ','|').split('|')
    count = getnum_valid_passports(batch)
    print(count)
