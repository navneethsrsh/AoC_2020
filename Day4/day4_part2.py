# AoC Day 4 Part 2
# Solution 1 - Generic

def validate_byr(byr: str) -> bool: 
    """
    Validate birth-year entry in passport data
    
    Parameters
    -------------------------------------------------------------------
    byr: string value storing the birth-year e.g. '1997'
    
    Return
    -------------------------------------------------------------------
    boolean
    
    Validation Checks
    -------------------------------------------------------------------
    > Length of birth-year is exactly 4
    > Birth-year is at least 1920 and  at most 2002
    
    """
    
    return len(byr) == 4 and 1920 <= int(byr) <= 2002


def validate_iyr(iyr: str) -> bool:
    """
    Validate issue-year entry in passport data
    
    Parameters
    -------------------------------------------------------------------
    iyr: string value storing the issue-year e.g. '2013'
    
    Return
    -------------------------------------------------------------------
    boolean
    
    Validation Checks
    -------------------------------------------------------------------
    > Length of issue-year is exactly 4
    > Issue-year is at least 2010 and  at most 2020
    
    """
    
    return len(iyr) == 4 and 2010 <= int(iyr) <= 2020


def validate_eyr(eyr: str) -> bool:
    """
    Validate expiry-year entry in passport data
    
    Parameters
    -------------------------------------------------------------------
    eyr: string value storing the expiry-year e.g. '2025'
    
    Return
    -------------------------------------------------------------------
    boolean
    
    Validation Checks
    -------------------------------------------------------------------
    > Length of expiry-year is exactly 4
    > Expiry-year is at least 2010 and  at most 2020
    
    """
    
    return len(eyr) == 4 and 2020 <= int(eyr) <= 2030


def validate_hgt(hgt: str) -> bool:
    """
    Validate height entry in the passport data
    
    Parameters
    -------------------------------------------------------------------
    hgt: string value storing the height e.g. '166cm'
    
    Return
    -------------------------------------------------------------------
    boolean
    
    Variables
    -------------------------------------------------------------------
    uom: 
        Sub-string of parameter hgt storing the unit of measure e.g.
        'cm'
    height: 
        Sub-string of parameter hgt storing the height as integer
        e.g. '166'
    
    Validation Checks
    -------------------------------------------------------------------
    > uom must be one fo either 'cm' or 'in'
    > If uom is 'cm' then height must be at least 150 and
      at most 193
    > If uom is 'in' then height must be at least 59 and at
      most 76
      
    """
    
    uom = hgt[-2:]
    height = int(hgt[:-2])
    if uom not in ('cm', 'in'): return False    
    return 150 <= height <= 193 if uom == 'cm' else 59 <= height <= 76


def validate_hcl(hcl: str) -> bool:
    """
    Validate hair colour entry of passport data
    
    Parameters
    -------------------------------------------------------------------
    hcl: string value storing hair colour in hex format 
         e.g. '#1a2fc9'
    
    Return
    -------------------------------------------------------------------
    boolean
    
    Variables
    -------------------------------------------------------------------
    charset: {'0'-'9',a-f}
    
    Validation Checks
    -------------------------------------------------------------------
    > Length of hcl must be 7 i.e. '#" followed by 6 char
    > hcl must start with '#'
    > After '#' the characters must belong to the set of
      acceptable values defined by variable charset
      
    """
    
    charset = set([hex(c)[-1] for c in range(16)])
    return len(hcl) == 7 and hcl.startswith("#") and set(hcl[1:]) <= charset


def validate_ecl(ecl: str) -> bool:
    """
    Validate eye colour entry in passport data
    
    Parameters
    -------------------------------------------------------------------
    ecl: string value storing eye colour e.g. 'blu' for blue
    
    Return
    -------------------------------------------------------------------
    boolean

    Validation Checks
    -------------------------------------------------------------------
    > Given eye colour is within a fixed set of values
    
    """
    
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def validate_pid(pid: str) -> bool:
    """
    Validate passport id entry in passport data
    
    Parameters
    -------------------------------------------------------------------
    pid: string value of the passport id e.g. 000143292
    
    Reuturn
    -------------------------------------------------------------------
    boolean
    
    Variables
    -------------------------------------------------------------------
    numset: {'0'-'9'}
    
    Validation Checks
    -------------------------------------------------------------------
    > Length of pid is exactly nine
    > All characters in pid are within variable numset
    
    """
    numset = set([str(x) for x in range(10)])
    return len(pid) == 9 and set(pid) <= numset


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
    validation_keys:
        A defined set of keys which must exist for a passport to be
        valid
    count:
        see Return
    data: 
        Dict of key-value pairs available for each line of batch
    line:
        An element in batch
    kvp:
        Represents key-value pair for a line
    validation:
        Dispatch table which is used to check the validity of all of 
        the values in the passport data
                
    Info
    -------------------------------------------------------------------
    For each line in batch, a dict of key-value pairs is generated 
    (variable: data). A two-step validation follows thus:
    
    Step 1:
        If the list of keys in dict data includes all the keys present
        in the set validation_keys, proceed to Step 2
        
    Step 2:
        All values are then evaluated by calling the respective
        validation function (e.g. validate_byr for value associated 
        with key "byr"). If all the validations pass, the count is
        incremented.
    
    """     
    
    validation_keys = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    count = 0
    data = {}    
    for line in batch:
        data = {kvp[:kvp.index(':')]: kvp[kvp.index(':') + 1:] \
                    for kvp in line.split()}
        if validation_keys <= set(data.keys()):
            validation = {
                    1: validate_byr(data['byr']),
                    2: validate_iyr(data['iyr']),
                    3: validate_eyr(data['eyr']),
                    4: validate_hgt(data['hgt']),
                    5: validate_hcl(data['hcl']),
                    6: validate_ecl(data['ecl']),
                    7: validate_pid(data['pid']),
                }
            if validation: count += (1 if all(validation.values()) else 0)
        validation.clear()
    return count


if __name__ == "__main__":
    
    with open('input.txt', 'r') as f:
        content = f.readlines()         
    batch = ' '.join([line[:-1] if line != '\n' else line
                      for line in content]).replace(' \n ','|').split('|')
    count = getnum_valid_passports(batch)
    print(count)
