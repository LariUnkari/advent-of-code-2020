"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, itertools, math, re, modules.userInput

SIDES = ['top', 'rgt', 'btm', 'lft']
DIRS = [[0,-1], [1,0], [0,1], [-1,0]]

def create_tile(id, data, tileDict, sideDict, log_level):
    sides = ["".join(data[0]), "", "".join(data[-1][::-1]), ""]

    for i in range(len(data)):
        sides[1] += data[i][-1]
        sides[3] += data[-1-i][0]

    if log_level >= 2: print(f"Sides of tile {id}: {sides}")
    
    # Due to how sides are recorded in a cycle around perimeter, opposites are always inverted to each other
    for i in range(len(sides)):
        s = sides[i]
        if s in sideDict:
            if log_level >= 3: print(f"Found side {i} '{s}' that matches {sideDict[s]}")
            sideDict[s].append((id, False, i))
        else:
            sideDict[s] = [(id, False, i)]

        s = sides[i][::-1]
        if s in sideDict:
            if log_level >= 3: print(f"Found inverse side {i} '{s}' that matches {sideDict[s]}")
            sideDict[s].append((id, True, i))
        else:
            sideDict[s] = [(id, True, i)]

    tileDict[id] = (id, sides, data)

def print_pixels(data_list, tileDim, removeEdges):
    slice = 1 if removeEdges else 0
    pixels = [""] * tileDim
    line:str

    for data in data_list:
        for y in range(len(data)):
            line = "".join(data[y][slice:len(data[y])-slice])
            pixels[y] += line + " "

    for line in pixels:
        print(line)

def print_image(grid, tiles, gridDim, tileDim, removeEdges):
    slice = 1 if removeEdges else 0
    dim = (gridDim * (tileDim + 1)) - 1
    pixels = [None] * dim
    for i in range(len(pixels)): pixels[i] = []

    tile = None
    line:str
    id:str
    px:int
    py:int
    rot:int
    data:list
    dataRot:list
    for gy in range(gridDim):
        for gx in range(gridDim):
            tile = grid[gx][gy]

            if tile != None:
                id = tile[0]
                rot = tile[2]

                data = tiles[id][2]
                dataRot = rotate_data(data, rot)

                for ty in range(slice,tileDim-slice):
                    py = ty + gy * tileDim + gy
                    line = "".join(dataRot[ty][slice:tileDim-slice])
                    pixels[py].append(line)
            else:
                for ty in range(slice,tileDim-slice):
                    py = ty + gy * tileDim + gy
                    line = "".join([' '] * (tileDim - 2 * slice))
                    pixels[py].append(line)

        if py+1 < len(pixels):
            pixels[py+1].append("")

    for y in range(len(pixels)):
        print(" ".join(pixels[y]))

def rotate_data(data, flip, rot):
    new_data = data.copy()

    if flip:
        for i, d in enumerate(new_data):
            new_data[i] = d[::-1]

    for i in range(rot):
        new_data = [list(d) for d in zip(*new_data[::-1])]

    return new_data

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
            data.append([c for c in line])
            if tWidth == 0: tWidth = len(line)
        else:
            if log_level >= 3: print(f"Empty line, creating tile data")
            create_tile(id, data, tiles, allSides, log_level)
            
            rMatch = None
            if tHeight == 0: tHeight = len(data)
            
    if rMatch != None:
        if log_level >= 1: print(f"Input processed, creating tile data")
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
        
    # Part 1 answer

    num = 1
    for id in connectionCounts[2]:
        if log_level >= 1: print(f"Corner tile: {id}")
        num *= int(id)
        
    print(f"Product of id numbers of image corners: {num}")

    # Part 2 answer

    # Take a corner piece (2 connections) and it's first side with connection
    # Position that tile as top left corner and start looking for a cycle around the perimeter

    grid = [None]*dim
    for i in range(dim):
        grid[i] = [None]*dim

    cell = None
    rot:int
    id = connectionCounts[2][0]
    for i in range(len(SIDES)):
        cell = tiles[id]
        line = cell[1][i]
        data = allSides[line]

        if len(data) > 1:
            s = cell[1][i-1]
            data = allSides[s]

            if len(data) > 1:
                rot = 2
            else:
                rot = ((i + 1) - 2 * i) % 4

            break
        
    flip = False
    corner = (id, flip, rot)

    x, y = 0, 0
    grid[x][y] = corner

    length = dim
    dep = length // 2
    num = 0
    dir = 1
    opp = 3
    
    sideThis = (dir - rot) % len(DIRS)
    sideOther = 0
    inverse = False
    tile = None
    visit = None
    cell = corner
    while True:
        tile = tiles[cell[0]]
        line = tile[1][sideThis]
        if cell[1]:
            line = line[::-1]
            if log_level >= 1: print(f"Flipped tile found: {cell[0]} inverted side {sideThis}='{line}'")

        if log_level >= 1: print(f"[{x},{y}] Visiting tile {cell[0]} at rotation {cell[2]} and flip={cell[1]}, looking for side {sideThis}='{line}'")
        
        for c in allSides[line]:
            if c[0] != cell[0]:
                id, inverse, sideOther = c
                break
            
        if not inverse: flip = not flip

        visit = tiles[id]
        sideOther = abs(sideOther)
        rot = (2 + sideOther - opp if flip else opp - sideOther) % len(DIRS)
        x += DIRS[dir][0]
        y += DIRS[dir][1]

        if log_level >= 2: print(f"[{x},{y}] Neighbour tile {id} at side {sideOther} and flip={flip}, rot={rot}")
        if log_level >= 3:
            print("")

            if dir % 2 == 0:
                print(f"{tile[0]} {cell[2]}" + ("i" if cell[1] else " "))
                print_pixels([rotate_data(tile[2], cell[1], cell[2])], tWidth, False)
                print(f"{visit[0]} {rot}" + ("i" if flip else " "))
                print_pixels([rotate_data(visit[2], flip, rot)], tWidth, False)
            else:
                print(f"{tile[0]} R{cell[2]} " + ("i" if cell[1] else " ") + f"  {visit[0]} R{rot} " + ("i" if flip else ""))
                print_pixels([rotate_data(tile[2], cell[1], cell[2]), rotate_data(visit[2], flip, rot)], tWidth, False)
                
            print("")

        if id == corner[0]:
            if log_level >= 1: print(f"Completed a full cycle around the ring at depth {dep}")
            if log_level >= 2:
                print("\nImage so far:")
                print_image(grid, tiles, dim, tWidth, False)

            length -= 2
            dep -= 1
            num = 0
            dir = 0
            
            x += 1
            cell = grid[x][y]
            y += 1

            rot = cell[2]
            sideThis = (rot + 2) % len(DIRS)
            visit = tiles[cell[0]]
            line = visit[1][sideThis]

            if log_level >= 1: print(f"Finding corner at depth {dep} at pos[{x},{y}] from {cell[0]} at rotation {cell[2]} and flip={cell[1]}\n   Looking for side {sideThis}='{line}'")
        
            data = allSides[line]
            for c in data:
                if c[0] != cell[0]:
                    id, inverse, sideOther = c
                    break

            if not inverse: flip = not flip
                
            rot = abs(sideOther)
            if log_level >= 2: print(f"[{x},{y}] Neighbour tile {id} at side {sideOther} and flip={flip}, rot={rot}")

        cell = (id, flip, rot)
        grid[x][y] = cell
        
        sideThis = sideOther + 2
        num += 1

        if num == dim - 1:
            if log_level >= 2: print(f"[{x},{y}] {id} is a corner tile")
            num = 0
            dir = (dir + 1) % len(DIRS)
            opp = (dir + 2) % len(DIRS)
            sideThis += -1 if flip else 1
            
        sideThis %= 4
