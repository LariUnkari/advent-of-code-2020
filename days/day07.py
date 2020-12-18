"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput

MY_BAG = "shiny gold"

def check_bag_for(allBagsDict, verifiedBagsDict, bagType, contentType, log_level):
    if bagType in verifiedBagsDict:
        if log_level >= 3: print(f"Bag {bagType}, already verified")
        return True

    if log_level >= 1: print(f"Checking bag type {bagType} for {contentType}")
    foundChild = False

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

def count_children_of(allBagsDict, bagType, log_level):
    if allBagsDict[bagType] == None:
        return 0

    childrenFound = 0
    directChildCount = 0

    for subType in allBagsDict[bagType]:
        if log_level >= 1: print(f"Bag {bagType} can directly contain {subType[0]} of {subType[1]}")
        directChildCount += subType[0]

        if log_level >= 2: print(f"Bag {subType[1]}, child of {bagType}, counting children...")
        childrenFound += subType[0] * count_children_of(allBagsDict, subType[1], log_level)

    if log_level >= 1: print(f"Bag {bagType} can directly contain {directChildCount} children and a total of {directChildCount+childrenFound} descendants")
    return directChildCount + childrenFound


def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
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

        bags[bagType] = [(int(content[0]), content[1]) for content in re.findall(regex, inputs[i][indexContain+13:])]

        if log_level >= 2:
            for c in bags[bagType]: print(f"Can contain {c[0]} of '{c[1]}'")

    # Run

    bagDict = {}

    if day_part == 1:
        for bagType in bags.keys():
            check_bag_for(bags, bagDict, bagType, MY_BAG, log_level)

        print(f"A {MY_BAG} bag can be contained within {len(bagDict)} bag types")

        if log_level >= 1:
            print(f"All verified bag types:\n{bagDict.keys()}")
    else:
        countChildren = count_children_of(bags, MY_BAG, log_level)
        print(f"My {MY_BAG} bag's children total count: {countChildren}")
