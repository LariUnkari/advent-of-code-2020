"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import modules.userInput

SLOPES = [(1,1), (3,1), (5,1), (7,1), (1,2)]

def walk_map(map, startRow, startColumn, slope, log_level):
    width = len(map[0])
    height = len(map)

    countTrees = 0

    c = startColumn
    for r in range(startRow + slope[1], len(map), slope[1]):
        if log_level >= 1:
            print(f"Map[{c},{r}]: '{map[r][c]}'")
        if map[r][c] == '#':
            countTrees += 1

        c = (c + slope[0]) % width
        
    print(f"Trees found on slope {slope}: {countTrees}")
    return countTrees

def play(input_file, day_part, input_parameters, log_level):
    
    #Initialize and read input

    mapData = []
    for index, inputText in enumerate(input_file):
        mapData.append(inputText.replace('\n', ''))
        if log_level >= 1:
            print(f"Input string {index}: '{map[index]}'")

    # Run
    
    if day_part == 1:
        walk_map(mapData, 0, SLOPES[1][0], SLOPES[1], log_level)
    else:
        countTrees = 0
        treeCountProduct = 1

        for slope in SLOPES:
            countTrees = walk_map(mapData, 0, slope[0], slope, log_level)
            treeCountProduct *= countTrees

        print(f"Trees count total product is {treeCountProduct}")