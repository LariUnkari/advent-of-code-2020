"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

SLOPES = [(1,1), (3,1), (5,1), (7,1), (1,2)]

def walkMap(map, startRow, startColumn, slope, log_level):
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

def play(input_file, input_parameters, log_level):
    

    #Initialize and read input


    map = []
    for index, inputText in enumerate(input_file):
        map.append(inputText.replace('\n', ''))
        if log_level >= 1:
            print(f"Input string {index}: '{map[index]}'")

    part_num = -1
    while part_num < 1:
        txt = input("Which part to run? 1-2 (defaults to 2): ")
        try:
            part_num = int(txt)
        except ValueError:
            print(f"Invalid input {txt} given!")
    
    if part_num == 1:
        countTrees = walkMap(map, 0, SLOPES[1][0], SLOPES[1], log_level)
    else:
        countTrees = 0
        treeCountProduct = 1
        for slope in SLOPES:
            countTrees = walkMap(map, 0, slope[0], slope, log_level)
            treeCountProduct *= countTrees
        print(f"Trees count total product is {treeCountProduct}")