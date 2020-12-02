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
    return input[indexColon+2:len(input)-1]

def processLine(input:str, log_level):
    policy = getPolicy(input, log_level)
    password = getPassword(input, log_level)
    if log_level >= 1:
        print(f"Policy limits: {policy[0]}-{policy[1]}, char: '{policy[2]}', password: '{password}' (length: {len(password)})")

    count = password.count(policy[2])
    result = policy[0] <= count and count <= policy[1]
    if log_level >= 1:
        print(f"Password: {password} contains {count} instances of {policy[2]}, isCorrect: {result}")

    return (result, count, policy, password)

def play(input_file, input_parameters, log_level):
    

    #Initialize and read input


    print("Day 2 begins!\n")

    countValid = 0
    countProcessed = 0

    result = (0, 1, 2, 3)
    for index, input in enumerate(input_file):
        if log_level >= 1:
            print(f"Input string {index}: '{input[:len(input)-1]}'")

        result = processLine(input, log_level)
        countProcessed += 1

        if result[0]:
            countValid += 1

            if log_level >= 1:
                print(f"Input {index} password '{result[3]}' is valid, count at {countValid}\n")
        else:
            if log_level >= 1:
                print(f"Input {index} password '{result[3]}' is NOT valid\n")

    print(f"Found a total of {countValid} valid passwords out of {countProcessed}")


    #Part 1 of Day 2


    #Part 2 of Day 2
