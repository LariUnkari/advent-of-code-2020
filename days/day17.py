"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, itertools, math, re, modules.userInput

TARGET_CYCLES = 6
NEIGHBOURS = [p for p in itertools.product([-1,0,1], repeat=3) if p.count(0) < 3]
STAY_ACTIVE = dict.fromkeys([2, 3])
TURN_ACTIVE = 3
CUBE_ON = '#'
CUBE_OFF = '.'

def count_active_neighbours(cubeMap, x, y, z, log_level):
    count = 0

    pos:tuple
    for n in NEIGHBOURS:
        pos = (x + n[0], y + n[1], z + n[2])
        if pos in cubeMap and cubeMap[pos] == CUBE_ON:
            count += 1
            if log_level >= 3: print(f"({x},{y},{z}) neighbour {pos} is active! Count: {count}")

    return count

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    print(f"Neighbours:\n{NEIGHBOURS}")
    
    inputs = [line.strip() for line in input_stream.read().split('\n') if line.strip()]
    
    loX, hiX = 1 - len(inputs) // 2 - len(inputs) % 2, len(inputs) // 2
    loY, hiY = 1 - len(inputs[0]) // 2 - len(inputs[0]) % 2, len(inputs[0]) // 2
    loZ, hiZ = 0, 0

    if log_level >= 1: print(f"Found {1+hiX-loX}x{1+hiY-loY}")
    if log_level >= 2:
        print(f"Starting cubes:")
        for line in inputs: print(f"   {line}")

    cubeMap = {}
    z = 0

    for y, row in enumerate(inputs):
        for x, cube in enumerate(row):
            cubeMap[(loX + x, loY + y, z)] = cube

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
                    neighbourCount = count_active_neighbours(cubeMap, x, y, z, log_level)
                    if log_level >= 2: print(f"[{cycle}] cube {x},{y},{z} has {neighbourCount} neighbours")

                    coordinate = (x, y, z)
                    if coordinate in cubeMap and cubeMap[coordinate] == CUBE_ON:
                        if neighbourCount in STAY_ACTIVE:
                            if log_level >= 2: print(f"[{cycle}]  Active  cube {x},{y},{z} has {neighbourCount} neighbours and will stay active")
                        else:
                            if log_level >= 2: print(f"[{cycle}]  Active  cube {x},{y},{z} has {neighbourCount} neighbours and will turn inactive")
                            changes.append((coordinate, CUBE_OFF))
                    else:
                        if neighbourCount == TURN_ACTIVE:
                            if log_level >= 2: print(f"[{cycle}] Inactive cube {x},{y},{z} has {neighbourCount} neighbours and will turn active")
                            changes.append((coordinate, CUBE_ON))
                        else:
                            if log_level >= 2: print(f"[{cycle}] Inactive cube {x},{y},{z} has {neighbourCount} neighbours and will stay inactive")

        if log_level >= 1: print(f"[{cycle}] Applying, {len(changes)} changes to cube map")
        for c in changes:
            cubeMap[c[0]] = c[1]

            if c[0][0] < loX: loX = c[0][0]
            if c[0][0] > hiX: hiX = c[0][0]
            if c[0][1] < loY: loY = c[0][1]
            if c[0][1] > hiY: hiY = c[0][1]
            if c[0][2] < loZ: loZ = c[0][2]
            if c[0][2] > hiZ: hiZ = c[0][2]

        if log_level >= 1: print(f"[{cycle}] Cycle ended, map range now ({loX} - {hiX}), ({loY} - {hiY}), ({loZ} - {hiZ})")
        if log_level >= 2:
            s1:str
            header2:str
            for z in range(loZ, hiZ+1):
                s1 = "Z={: 02d}  ".format(z)
                s2 = "     " if loX % 2 == 0 else "       "
                for x in range(loX, hiX+1):
                    if x % 2 == 0:
                        s2 += "{: 02d}".format(x)
                    else:
                        s1 += "{: 02d}".format(x)

                print(f"\n{s1}\n{s2}")
                for y in range(loY, hiY+1):
                    s1 = "{: 02d}".format(y)
                    s2 = "".join([cubeMap[(x,y,z)] if (x,y,z) in cubeMap else CUBE_OFF for x in range(loX, hiX+1)])
                    print(f"{s1}     {s2}")

        changes.clear()

    count = sum(value == CUBE_ON for value in cubeMap.values())
    print(f"\nNumber on active cybes {count}")