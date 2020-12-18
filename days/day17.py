"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, itertools, math, re, modules.userInput

TARGET_CYCLES = 6
NEIGHBOURS3 = [p for p in itertools.product([-1,0,1], repeat=3) if p.count(0) < 3]
NEIGHBOURS4 = [p for p in itertools.product([-1,0,1], repeat=4) if p.count(0) < 4]
STAY_ACTIVE = dict.fromkeys([2, 3])
TURN_ACTIVE = 3
CUBE_ON = '#'
CUBE_OFF = '.'

def count_active_neighbours3(cubeMap, x, y, z, w, log_level):
    count = 0

    pos:tuple
    for n in NEIGHBOURS3:
        pos = (x + n[0], y + n[1], z + n[2], w)
        if pos in cubeMap and cubeMap[pos] == CUBE_ON:
            count += 1
            if log_level >= 3: print(f"({x},{y},{z}) neighbour {pos} is active! Count: {count}")

    return count

def count_active_neighbours4(cubeMap, x, y, z, w, log_level):
    count = 0

    pos:tuple
    for n in NEIGHBOURS4:
        pos = (x + n[0], y + n[1], z + n[2], w + n[3])
        if pos in cubeMap and cubeMap[pos] == CUBE_ON:
            count += 1
            if log_level >= 3: print(f"({x},{y},{z},{w}) neighbour {pos} is active! Count: {count}")

    return count

def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    # Initialize and read input

    inputs = [line.strip() for line in input_stream.read().split('\n') if line.strip()]
    
    loX, hiX = 1 - len(inputs) // 2 - len(inputs) % 2, len(inputs) // 2
    loY, hiY = 1 - len(inputs[0]) // 2 - len(inputs[0]) % 2, len(inputs[0]) // 2
    loZ, hiZ = 0, 0
    loW, hiW = 0, 0

    if log_level >= 1:
        print(f"Starting cubes:")
        for line in inputs: print(f"   {line}")

    cubeMap = {}
    z = 0
    w = 0

    for y, row in enumerate(inputs):
        for x, cube in enumerate(row):
            cubeMap[(loX + x, loY + y, z, w)] = cube

    # Run

    cycle = 0
    neighbourCount:int
    coordinate:tuple

    changes = []

    while cycle < TARGET_CYCLES:
        cycle += 1

        for x in range(loX-1, hiX+2):
            for y in range(loY-1, hiY+2):
                for z in range(loZ-1, hiZ+2):
                    for w in (range(0, 1) if day_part == 1 else range(loW-1, hiW+2)):
                        coordinate = (x, y, z, w)
                        if day_part == 1:
                            neighbourCount = count_active_neighbours3(cubeMap, x, y, z, w, log_level)
                        else:
                            neighbourCount = count_active_neighbours4(cubeMap, x, y, z, w, log_level)

                        if coordinate in cubeMap and cubeMap[coordinate] == CUBE_ON:
                            if neighbourCount in STAY_ACTIVE:
                                if log_level >= 2: print(f"[{cycle}]  Active  cube {coordinate} has {neighbourCount} neighbours and will stay active")
                            else:
                                if log_level >= 2: print(f"[{cycle}]  Active  cube {coordinate} has {neighbourCount} neighbours and will turn inactive")
                                changes.append((coordinate, CUBE_OFF))
                        else:
                            if neighbourCount == TURN_ACTIVE:
                                if log_level >= 2: print(f"[{cycle}] Inactive cube {coordinate} has {neighbourCount} neighbours and will turn active")
                                changes.append((coordinate, CUBE_ON))
                            else:
                                if log_level >= 2: print(f"[{cycle}] Inactive cube {coordinate} has {neighbourCount} neighbours and will stay inactive")

        if log_level >= 1: print(f"[{cycle}] Applying, {len(changes)} changes to cube map")
        for c in changes:
            cubeMap[c[0]] = c[1]

            if c[0][0] < loX: loX = c[0][0]
            if c[0][0] > hiX: hiX = c[0][0]
            if c[0][1] < loY: loY = c[0][1]
            if c[0][1] > hiY: hiY = c[0][1]
            if c[0][2] < loZ: loZ = c[0][2]
            if c[0][2] > hiZ: hiZ = c[0][2]
            if c[0][3] < loW: loW = c[0][3]
            if c[0][3] > hiW: hiW = c[0][3]

        print(f"[{cycle}] Cycle ended, map range now ({loX} - {hiX}), ({loY} - {hiY}), ({loZ} - {hiZ}), ({loW} - {hiW})")

        # This prints a pretty map z layer at a time, but skips it in part 2 and 4D map
        # Similar to looks of sample in the puzzle, but doesn't fool the user and actually prints X and Y coordinates
        if log_level >= 1 and day_part == 1:
            s1:str
            s2:str
            for z in range(loZ, hiZ+1):
                s1 = "Z={: 02d}   X: ".format(z) + ("  " if loX % 2 == 0 else "")
                s2 = "Y:        " + ("" if loX % 2 == 0 else "  ")
                for x in range(loX, hiX+1):
                    if x % 2 == 0:
                        s2 += "{: 02d}  ".format(x)
                    else:
                        s1 += "{: 02d}  ".format(x)

                print(f"\n{s1}\n{s2}")
                for y in range(loY, hiY+1):
                    s1 = "{: 02d}".format(y)
                    s2 = " ".join([cubeMap[(x,y,z,0)] if (x,y,z,0) in cubeMap else CUBE_OFF for x in range(loX, hiX+1)])
                    print(f"{s1}         {s2}")

            print(" ")

        changes.clear()

    count = sum(value == CUBE_ON for value in cubeMap.values())
    print(f"\nNumber on active cubes {count}")