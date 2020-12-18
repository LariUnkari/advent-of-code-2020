"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput

INITIAL_DIR = 1
INITIAL_WAYPOINT = (10, 1)
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

def run_part_1(instructions, x, y, direction, log_level):
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
            if log_level >= 2: print(f"[{index}] Ship rotated {action[0]} by {abs(val*90)} degrees")
        else:
            x += val * vector[0]
            y += val * vector[1]
            if log_level >= 2: print(f"[{index}] Ship moved {action[0]} by {val} in direction {vector}")

        if log_level >= 1: print(f"[{index}] Ship now at {x},{y}, facing {DIRS[direction]}")
        vector = None

    return (x,y)

def rotate_point(rotations, x, y, log_level):
    a = x
    b = y

    if log_level >= 3: print(f"Rotating {x},{y} {rotations*90} degrees")

    for i in range(abs(rotations)):
        if rotations < 0:
            x = -b
            y = a
        else:
            x = b
            y = -a

        a = x
        b = y

        if log_level >= 3: print(f"Rotation {rotations*i*90/abs(rotations)}: now at {x},{y}")

    return (x, y)

def run_part_2(instructions, x, y, wx, wy, log_level):
    print(f"Ship starts at {x},{y}, waypoint at {wx},{wy}")

    cmd:str
    val:int
    vector = None

    for index, action in enumerate(instructions):
        cmd = action[0]
        val = action[1]

        if cmd == "F":
            vector = (wx, wy)
            x += val * vector[0]
            y += val * vector[1]
            if log_level >= 2: print(f"[{index}] Ship and waypoint moved by {val} in direction {vector}")
        else:
            if cmd == "N": vector = DIRS[0]
            elif cmd == "E": vector = DIRS[1]
            elif cmd == "S": vector = DIRS[2]
            elif cmd == "W": vector = DIRS[3]
            elif cmd == "L": val = -val // 90
            elif cmd == "R": val = val // 90
            
            if vector == None:
                wx, wy = rotate_point(val, wx, wy, log_level)
                if log_level >= 2: print(f"[{index}] Waypoint rotated around ship by {val*90} degrees")
            else:
                wx += val * vector[0]
                wy += val * vector[1]
                if log_level >= 2: print(f"[{index}] Waypoint moved {action[0]} by {val} in direction {vector}")

        vector = None

        if log_level >= 1: print(f"[{index}] Ship now at {x},{y}, waypoint at {wx},{wy}")
        

    return (x,y)

def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    # Initialize and read input
    
    instructions = [(line[0], int(line[1:])) for line in input_stream.read().split('\n') if line.strip()]

    if log_level >= 1: print(f"Found {len(instructions)} instructions")

    # Run

    x, y = 0, 0

    if day_part == 1:
        x, y = run_part_1(instructions, x, y, INITIAL_DIR, log_level)
    else:
        x, y = run_part_2(instructions, x, y, INITIAL_WAYPOINT[0], INITIAL_WAYPOINT[1], log_level)

    dist = abs(x)+abs(y)
    print(f"Ship ended at {x},{y}, traveled manhattan distance: {dist}")