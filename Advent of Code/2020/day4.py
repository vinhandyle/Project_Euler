# Day 4: Passport Processing
# Part 1: 230
# Part 2: 156

from pathlib import Path


INPUT = Path('input_4.txt')


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    passports = _get_passports()
    valid_passports = 0
    
    for passport in passports:
        if _is_valid_passport(passport):
            valid_passports += 1
            
    return valid_passports



def get_second_ans() -> '???':
    passports = _get_passports()
    valid_passports = 0

    for passport in passports:
        if _is_valid_passport(passport):
            if _is_more_valid_passport(passport):
                valid_passports += 1

    return valid_passports



def _is_more_valid_passport(passport: dict) -> bool:
    '''
    Returns True if the given passport is valid. Returns False, otherwise.
    A passport is valid if each of its required fields have valid data.
    '''
    if not 1920 <= int(passport['byr']) <= 2002 or \
       not 2010 <= int(passport['iyr']) <= 2020 or \
       not 2020 <= int(passport['eyr']) <= 2030 or \
       not _is_valid_height(passport['hgt']) or \
       not _is_valid_hair_color(passport['hcl']) or \
       not _is_valid_eye_color(passport['ecl']) or \
       not _is_valid_passport_id(passport['pid']):
        return False
    return True
    


def _is_valid_height(field: str) -> bool:
    '''Returns True if the given height is valid. Return False, otherwise'''
    unit = field[-2:]
    
    if unit == 'cm':
        if not 150 <= int(field[:-2]) <= 193:
            return False
    elif unit == 'in':
        if not 59 <= int(field[:-2]) <= 76:
            return False
    else:
        return False
    return True



def _is_valid_hair_color(field: str) -> bool:
    '''Returns True if the given hair color is valid. Return False, otherwise'''
    valid_chars = '1234567890abcdef'

    if field[0] != '#':
        return False
    elif len(field) != 7:
        return False
    else:
        for char in field[1:]:
            if not char in valid_chars:
                return False
    return True



def _is_valid_eye_color(field: str) -> bool:
    '''Returns True if the given eye color is valid. Return False, otherwise'''
    valid_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if field in valid_color:
        return True
    return False



def _is_valid_passport_id(field: str) -> bool:
    '''Returns True if the given passport id is valid. Return False, otherwise'''
    if len(field) == 9:
        try:
            int(field)
            return True
        except ValueError:
            return False
    return False


def _is_valid_passport(passport: dict) -> bool:
    '''
    Returns True if the given passport is valid. Returns False, otherwise.
    A passport is valid if has no missing fields, with 'cid' being optional.
    '''
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    for field in required_fields:
        if not field in passport:
            return False
    return True


    
def _get_passports() -> [dict]:
    '''
    Finds the text file called input_4.txt and returns its content as a list of
    dictionaries containing passport fields.
    '''
    passports = []
    passport = dict()
    file = open(INPUT, 'r')

    for line in file:
        # Add to list of passports
        if line == '\n':
            passports.append(passport)
            passport = dict()
            
        else:
            key = ''
            field = ''

            # Create passport profile
            for char in line:
                if char == ':':
                    continue
                elif char == ' ' or char == '\n':
                    passport[key] = field
                    key = ''
                    field = ''
                elif len(key) == 3:
                    field += char     
                else:
                    key += char

    file.close()
    
    # Get the very last passport
    passports.append(passport)
    return passports


    
if __name__ == '__main__':
    run()
