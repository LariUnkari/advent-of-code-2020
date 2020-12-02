"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

def getPolicy(input:str, log_level):
    indexDash = input.index('-')
    if log_level >= 2:
        print(f"Policy dash char index: {indexDash}")

    min = int(input[:indexDash])
    if log_level >= 2:
        print(f"Policy min: {min} parsed from {input[:indexDash]}")

    indexEnd = input.index(' ')
    if log_level >= 2:
        print(f"Policy end char index: {indexEnd}")

    max = int(input[indexDash+1:indexEnd])
    if log_level >= 2:
        print(f"Policy max: {max} parsed from {input[indexDash+1:indexEnd]}")

    char = input[indexEnd+1:indexEnd+2]
    if log_level >= 2:
        print(f"Policy char: {char} parsed from {input[indexEnd+1:indexEnd+2]}")

    return (min, max, char)

def getPassword(input:str, log_level):
    indexColon = input.index(':')
    if log_level >= 2:
        print(f"Policy colon char index: {indexColon}")
    return input[indexColon+2:].replace('\n', "")

def checkPasswordPart1(policy, password, log_level):
    if log_level >= 1:
        print(f"Policy limits: {policy[0]}-{policy[1]}, char: '{policy[2]}', password: '{password}' (length: {len(password)})")

    count = password.count(policy[2])
    result = policy[0] <= count and count <= policy[1]
    if log_level >= 1:
        print(f"Password: {password} contains {count} instances of {policy[2]}, isCorrect: {result}")

    return (result, policy, password)

def checkPasswordPart2(policy, password, log_level):
    if log_level >= 1:
        print(f"Policy positions: {policy[0]} and {policy[1]}, char: '{policy[2]}', password: '{password}' (length: {len(password)})")

    indexLow = policy[0]-1
    charLow = password[indexLow]
    if log_level >= 3:
        print(f"Char at index {indexLow} is '{charLow}'")
    matchLow = password[indexLow] == policy[2]

    indexHigh = policy[1]-1
    charHigh = password[indexHigh]
    if log_level >= 3:
        print(f"Char at index {indexHigh} is '{charHigh}'")
    matchHigh = password[indexHigh] == policy[2]

    result = False
    if matchLow and matchHigh:
        if log_level >= 2:
            print(f"Password: {password} contains instances of {policy[2]} at both required positions {policy[0]} and {policy[1]}")
    elif matchLow:
        result = True
        if log_level >= 2:
            print(f"Password: {password} contains an instance of {policy[2]} at required position {policy[0]}")
    elif matchHigh:
        result = True
        if log_level >= 2:
            print(f"Password: {password} contains an instance of {policy[2]} at required position {policy[1]}")
    else:
        if log_level >= 2:
            print(f"Password: {password} contains NO instances of {policy[2]} at required positions {policy[0]} and {policy[1]}")

    if log_level >= 1:
        print(f"Password: {password} isCorrect: {result}")

    return (result, policy, password)

def checkPasswords(entries, part_num, log_level):
    countValid = 0
    countProcessed = 0

    result = (0, 1, 2, 3)
    for index, entry in enumerate(entries):

        if part_num == 1:
            result = checkPasswordPart1(entry[0], entry[1], log_level)
        else:
            result = checkPasswordPart2(entry[0], entry[1], log_level)

        countProcessed += 1

        if result[0]:
            countValid += 1

            if log_level >= 1:
                print(f"Input {index} password '{result[2]}' is valid, count at {countValid}\n")
        else:
            if log_level >= 1:
                print(f"Input {index} password '{result[2]}' is NOT valid\n")

    print(f"Found a total of {countValid} valid passwords out of {countProcessed}")

def processLine(input:str, log_level):
    policy = getPolicy(input, log_level)
    password = getPassword(input, log_level)
    return (policy, password)

def processInput(input_file, log_level):
    entries = []
    for index, input in enumerate(input_file):
        if log_level >= 1:
            print(f"Input string {index}: '{input[:len(input)-1]}'")
        entries.append(processLine(input, log_level))

    return entries

def play(input_file, input_parameters, log_level):
    

    #Initialize and read input


    entries = processInput(input_file, log_level)


    #Part 1 of Day 2

    
    print("\nDay 2 part 1:\n")
    checkPasswords(entries, 1, log_level)


    #Part 2 of Day 2


    print("\nDay 2 part 2:\n")
    checkPasswords(entries, 2, log_level)