"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

START_SLOPE = 3

def walkMap(map, startRow, startColumn, slope, log_level):
    width = len(map[0])
    height = len(map)

    if log_level >= 1:
        print(f"Map dimensions: '{width}x{height}'")

    countTrees = 0

    c = startColumn
    for r in range(startRow, len(map)):
        if log_level >= 1:
            print(f"Map[{c},{r}]: '{map[r][c]}'")
        if map[r][c] == '#':
            countTrees += 1

        c = (c + slope) % width

    return countTrees

def play(input_file, input_parameters, log_level):
    

    #Initialize and read input


    map = []
    for index, input in enumerate(input_file):
        map.append(input.replace('\n', ''))
        if log_level >= 1:
            print(f"Input string {index}: '{map[index]}'")


    #Part 1 of Day 1

    
    countTrees = walkMap(map, 1, START_SLOPE, START_SLOPE, log_level)
    print(f"Trees found: {countTrees}")


    #Part 2 of Day 1


    