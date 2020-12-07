"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput

MY_BAG = "shiny gold"

def check_bag_for(allBagsDict, verifiedBagsDict, bagType, contentType, log_level):
    foundChild = False

    if bagType in verifiedBagsDict:
        if log_level >= 3: print(f"Bag {bagType}, already verified")
        return True

    if allBagsDict[bagType] == None:
        if log_level >= 3: print(f"Bag {bagType} can NOT contain anything")
        return False

    for subType in allBagsDict[bagType]:
        if subType[1] == contentType:
            if log_level >= 1: print(f"Bag {bagType} can directly contain {contentType}")
            verifiedBagsDict[bagType] = True
            return True
        
        if log_level >= 3: print(f"Bag {subType[1]}, child of {bagType}, checking for {contentType}")
        foundChild |= check_bag_for(allBagsDict, verifiedBagsDict, subType[1], contentType, log_level)
        
    if foundChild:
        if log_level >= 2: print(f"Bag {bagType} can contain {contentType} via children")
        verifiedBagsDict[bagType] = True
        return True

    return False

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    #Initialize and read input

    inputs = input_stream.read().replace('.', '').split('\n')
    regex = "(\d+) (\w+ \w+) bags?"

    bagType:str
    bags = {}
    for i in range(len(inputs)):
        if len(inputs[i]) == 0:
            continue

        indexContain = inputs[i].find("bags contain")
        bagType = inputs[i][:indexContain-1]
        
        if log_level >= 1: print(f"Found bag definition {i} for '{bagType}'")

        if inputs[i].find(" no ") >= 0:
            bags[bagType] = None
            continue

        bags[bagType] = [(content[0], content[1]) for content in re.findall(regex, inputs[i][indexContain+13:])]

        if log_level >= 2:
            for c in bags[bagType]: print(f"Can contain {c[0]} of '{c[1]}'")

    # Select which part of day to run
    
    part_input = modules.userInput.get_int_input_constrained("Which part to run? 1-2 (defaults to 2): ", 1, 2, 2)

    # Run

    bagDict = {}

    if part_input[1] == 1:
        for bagType in bags.keys():
            if log_level >= 1: print(f"Checking bag type {bagType}")

            check_bag_for(bags, bagDict, bagType, MY_BAG, log_level)

            if log_level >= 2: print(f"Done checking bag type {bagType}")

        print(f"{MY_BAG} can be contained within {len(bagDict)} bag types")
        if log_level >= 1:
            print(f"All verified bag types:\n{bagDict.keys()}")
