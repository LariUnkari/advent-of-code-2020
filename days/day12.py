"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput

INITIAL_DIR = 1
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    instructions = [(line[0], int(line[1:])) for line in input_stream.read().split('\n') if line.strip()]

    if log_level >= 1: print(f"Found {len(instructions)} instructions")

    # Run

    x = 0
    y = 0
    direction = INITIAL_DIR
    print(f"Ship starts at {x},{y}, facing {DIRS[direction]}")

    cmd:str
    val:int
    vector = None
    for index, action in enumerate(instructions):
        cmd = action[0]
        val = action[1]

        if cmd == "F": vector = DIRS[direction]
        elif cmd == "N": vector = DIRS[0]
        elif cmd == "E": vector = DIRS[1]
        elif cmd == "S": vector = DIRS[2]
        elif cmd == "W": vector = DIRS[3]
        elif cmd == "L": val = -val // 90
        elif cmd == "R": val = val // 90
            
        if vector == None:
            direction = (direction + val) % len(DIRS)
            if log_level >= 2: print(f"[{index}] Ship rotated {action[0]} by {action[1]} degrees")
        else:
            x += val * vector[0]
            y += val * vector[1]
            if log_level >= 2: print(f"[{index}] Ship moved {action[0]} by {val} in direction {vector}")

        if log_level >= 1: print(f"[{index}] Ship now at {x},{y}, facing {DIRS[direction]}")
        vector = None

    dist = abs(x)+abs(y)
    print(f"Ship ended at {x},{y}, facing {DIRS[direction]}, traveled manhattan distance: {dist}")