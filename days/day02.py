"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

def parsePolicyPassword(input:str, log_level):
    indexDash = input.index('-')
    indexEndRule = input.index(' ')
    indexColon = input.index(':')
    min = int(input[:indexDash])
    max = int(input[indexDash+1:indexEndRule])
    char = input[indexEndRule+1:indexEndRule+2]
    password = input[indexColon+2:]

    return (min, max, char, password)

def checkPasswordPart1(entry, log_level):
    if log_level >= 1:
        print(f"Policy limits: {entry[0]}-{entry[1]}, char: '{entry[2]}', password: '{entry[3]}' (length: {len(entry[3])})")

    count = entry[3].count(entry[2])
    result = entry[0] <= count and count <= entry[1]

    if log_level >= 1:
        print(f"Password: {entry[3]} contains {count} instances of {entry[2]}, isCorrect: {result}")

    return result

def checkPasswordPart2(entry, log_level):
    if log_level >= 1:
        print(f"Policy positions: {entry[0]} and {entry[1]}, char: '{entry[2]}', password: '{entry[3]}' (length: {len(entry[3])})")

    matchLow = entry[3][entry[0]-1] == entry[2]
    matchHigh = entry[3][entry[1]-1] == entry[2]
    result = (matchLow and not(matchHigh)) or (matchHigh and not(matchLow))

    if log_level >= 1:
        print(f"Password: {entry[3]}, low({entry[0]-1}): {matchLow}, high({entry[1]-1}): {matchHigh}, isCorrect: {result}")

    return result

def checkPasswords(entries, part_num, log_level):
    countValid = 0
    countProcessed = 0

    result = False
    for index, entry in enumerate(entries):

        if part_num == 1:
            result = checkPasswordPart1(entry, log_level)
        else:
            result = checkPasswordPart2(entry, log_level)

        countProcessed += 1

        if result:
            countValid += 1

            if log_level >= 1:
                print(f"Input {index} password '{entry[3]}' is valid, count at {countValid}\n")
        else:
            if log_level >= 1:
                print(f"Input {index} password '{entry[3]}' is NOT valid\n")

    print(f"Found a total of {countValid} valid passwords out of {countProcessed}")


def play(input_file, input_parameters, log_level):
    

    #Initialize and read input

    
    entries = []
    for index, input in enumerate(input_file):
        input = input.replace('\n', '')
        if log_level >= 1:
            print(f"Input string {index}: '{input}'")
        entries.append(parsePolicyPassword(input, log_level))


    #Part 1 of Day 2

    
    print("\nDay 2 part 1:\n")
    checkPasswords(entries, 1, log_level)


    #Part 2 of Day 2


    print("\nDay 2 part 2:\n")
    checkPasswords(entries, 2, log_level)