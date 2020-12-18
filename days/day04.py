"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput

VALIDATE_FIELDS = {
    'byr': ('(\d{4})',
            lambda a : int(a[0]),
            lambda b : b >= 1920 and b <= 2002 ),
    'iyr': ('(\d{4})',
            lambda a : int(a[0]),
            lambda b : b >= 2010 and b <= 2020 ),
    'eyr': ('(\d{4})',
            lambda a : int(a[0]),
            lambda b : b >= 2020 and b <= 2030 ),
    'hgt': ('(\d+)(cm|in)',
            lambda a : (int(a[0]), a[1]),
            lambda b : (b[1] == 'cm' and b[0] >= 150 and b[0] <= 193) or (b[1] == 'in' and b[0] >= 59 and b[0] <= 76)),
    'hcl': ('#[0-9a-f]{6}', None, None),
    'ecl': ('^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$', None, None),
    'pid': ('^(\d{9})$', None, None)
}

def process_data(input_stream:io.TextIOWrapper, log_level):
    inputData = []
    index = -1
    line = "begin"
    data = ""
    while len(line) > 0:
        index += 1
        line = input_stream.readline()

        if len(line) == 0 or line == '\n':
            if log_level >= 1:
                print(f"Input string {index} is an empty line, appending entry[{len(inputData)}]")
            inputData.append(data)
            data = ""
            continue
        
        if log_level >= 2:
            print(f"Input string {index} is '{line}'")
        data += line.replace('\n', ' ')

    print(f"Read {len(inputData)} entries from data")

    regex = '(\w{3}):(#*\w+)'
    entries = []

    for inputLine in inputData:
        entry = []

        for match in re.findall(regex, inputLine):
            entry.append((match[0], match[1]))

        if log_level >= 1:
            print(f"Read {len(entry)} fields in entry {len(entries)}")

        entries.append(entry)

    return entries

def validate_part_1(fieldsToValidate, index, entry, log_level):
    for field in entry:
        if field[0] in fieldsToValidate:
            fieldsToValidate[field[0]] = True
            
    for f in fieldsToValidate:
        if not(fieldsToValidate[f][0]):
            if log_level >= 1:
                print(f"Entry {index} failed validation on fields: {list(fieldsToValidate.keys())}")
            return False
    
    return True

def validate_part_2(fieldsToValidate, index, entry, log_level):
    rule:dict = None
    regex:str = None
    converter:function = None
    validator:function = None
            
    match = None
    value = None
    for field in entry:
        if field[0] in VALIDATE_FIELDS:
            rule = VALIDATE_FIELDS[field[0]]
            regex = rule[0]
            converter = rule[1]
            validator = rule[2]
            
            value = None
            match = re.search(regex, field[1])
            if match != None:
                if validator == None:
                    value = True
                else:
                    if converter != None:
                        value = converter(match.groups())
                    else:
                        value = match.groups()

                    if value != None and not(validator(value)):
                        value = None

            if value != None:
                if log_level >= 2:
                    print(f"Entry {index} passed validation on {field[0]}:{field[1]}")
                fieldsToValidate[field[0]] = True
            elif log_level >= 2:
                print(f"Entry {index} failed validation failed on {field[0]}:{field[1]}")

    for f in fieldsToValidate:
        if not(fieldsToValidate[f]):
            if log_level >= 1:
                print(f"Entry {index} failed validation on fields: {list(fieldsToValidate.keys())}")
            return False

    return True

def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    #Initialize and read input

    entries = process_data(input_stream, log_level)

    # Run
    
    countValid = 0

    fieldsToValidate = dict.fromkeys(VALIDATE_FIELDS.keys(), False)
    for index, entry in enumerate(entries):

        if day_part == 1:
            if validate_part_1(fieldsToValidate, index, entry, log_level):
                countValid += 1
        else:
            if validate_part_2(fieldsToValidate, index, entry, log_level):
                countValid += 1
                
        for f in fieldsToValidate:
            fieldsToValidate[f] = False

    print(f"Found {countValid} valid entries")
