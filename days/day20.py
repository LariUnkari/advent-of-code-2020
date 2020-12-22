"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, itertools, math, re, modules.userInput

SIDES = ['top', 'rgt', 'btm', 'lft']
DIRS = [[1,0], [0,1], [-1,0], [0,-1]]

def create_tile(id, data, tileDict, sideDict, log_level):
    sides = [data[0], "", data[-1][::-1], ""]

    for i in range(len(data)):
        sides[1] += data[i][-1]
        sides[3] += data[-1-i][0]

    if log_level >= 1: print(f"Sides of tile {id}: {sides}")
    
    # Due to how sides are recorded, opposites are always inverted to each other,
    # therefore inverted sides are not flipped but vice versa
    for i in range(len(sides)):
        s = sides[i]
        if s in sideDict:
            if log_level >= 2: print(f"Found inverse side {i} '{s}' that matches {sideDict[s]}")
            sideDict[s].append((id, True, i))
        else:
            sideDict[s] = [(id, True, i)]

        s = sides[i][::-1]
        if s in sideDict:
            if log_level >= 2: print(f"Found side {i} '{s}' that matches {sideDict[s]}")
            sideDict[s].append((id, False, i))
        else:
            sideDict[s] = [(id, False, i)]

    tileDict[id] = (id, sides, data)

def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    # Initialize and read input
    
    tiles = {}
    allSides = {}
    connectionCounts = {}
    tWidth = 0
    tHeight = 0

    s:str
    id:str
    data:list
    rMatch = None
    for line in input_stream.read().split('\n'):
        if rMatch == None:
            rMatch = re.search("(?:Tile (\d+):)", line)
            if rMatch == None: continue
            
            id = rMatch[1]
            data = []
            if log_level >= 3: print(f"Started reading tile {id} data")
        elif len(line) > 0:
            if log_level >= 3: print(f"Read tile {id} line '{line}'")
            data.append(line)
            if tWidth == 0: tWidth = len(line)
        else:
            if log_level >= 3: print(f"Empty line, finalizing tile data")
            create_tile(id, data, tiles, allSides, log_level)
            
            rMatch = None
            if tHeight == 0: tHeight = len(data)
            
    if rMatch != None:
        if log_level >= 1: print(f"Input processed, finalizing tile data")
        create_tile(id, data, tiles, allSides, log_level)
        
    dim = int(math.sqrt(len(tiles)))
    print(f"Found {len(tiles)} tiles of dimensions {tWidth}x{tHeight}, image tile dimensions: {dim}x{dim}")

    # Run

    num:int
    for id, sides, data in tiles.values():
        num = 0

        for i in range(len(SIDES)):
            data = allSides[sides[i]]
            if len(data) > 1: num += 1

        if num in connectionCounts:
            connectionCounts[num].append(id)
        else:
            connectionCounts[num] = [id]

    for key in connectionCounts.keys():
        print(f"Found {len(connectionCounts[key])} tiles with {key} connections: {connectionCounts[key]}")
        
    num = 1
    for id in connectionCounts[2]:
        if log_level >= 1: print(f"Corner tile: {id}")
        num *= int(id)
        
    print(f"Product of id numbers of image corners: {num}")
    
