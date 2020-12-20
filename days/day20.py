"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, itertools, math, re, modules.userInput

SIDES = ['top', 'rgt', 'btm', 'lft']

def find_matching_side(pixels, tileID, tileData, log_level):
    for i, side in get_sides(tileData, log_level):
        if side == pixels:
            if log_level >= 2: print(f"Tile {tileID} side {i} {SIDES[i]} matches {pixels}")
            return i+1
        if side[::-1] == pixels:
            if log_level >= 2: print(f"Tile {tileID} side {i} {SIDES[i]} matches {pixels} when reversed")
            return -(i+1)

        if log_level >= 3: print(f"Tile {tileID} side {i} {SIDES[i]} does not match {pixels}")

    if log_level >= 2: print(f"Tile {tileID} side {i} {SIDES[i]} does not match {pixels}")
    return 0

def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    # Initialize and read input
    
    tiles = {}
    allSides = {}
    tileConnections
    tWidth = 0
    tHeight = 0

    s:str
    id:str
    data:list
    rMatch = None
    for line in input_stream.read().split('\n'):
        if rMatch == None:
            rMatch = re.search("(?:Tile (\d+):)", line)
            id = rMatch[1]
            print(f"Started reading tile {id} data")
            data = []
        elif len(line) > 0:
            if tWidth == 0: tWidth = len(line)
            print(f"Read tile {id} line '{line}'")
            data.append(line)
        else:
            print(f"Empty line, stopped reading tile data")

            if tHeight == 0: tHeight = len(data)
            sides = [data[0], "", data[tHeight-1], ""]

            for y in range(len(data)):
                sides[1] += data[y][tWidth-1]
                sides[3] += data[y][0]

            print(f"Sides of tile {id}: {sides}")

            for i in range(len(sides)):
                s = sides[i]
                if s in allSides:
                    print(f"Found side {i+1} '{s}' that matches {allSides[s]}")
                    allSides[s].append((id, i+1))
                else:
                    allSides[s] = [(id, i+1)]

                s = sides[i][::-1]
                if s in allSides:
                    print(f"Found side {-(i+1)} '{s}' that matches {allSides[s]}")
                    allSides[s].append((id, -(i+1)))
                else:
                    allSides[s] = [(id, -(i+1))]

            tiles[id] = (id, sides, data)
            rMatch = None

    print(f"Found {len(tiles)} tiles of dimensions {tWidth}x{tHeight}")

    # Run

    
