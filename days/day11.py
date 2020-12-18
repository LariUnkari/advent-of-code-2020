"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput

EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'
NEIGHBOURS = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

def count_neighbours(x, y, width, height, layout, allowDistance, rule, stopAt, limit, log_level):
    adjacentSeats = 0
    d:int
    u:int
    v:int

    if log_level >= 4: print(f"Checking seat {x},{y} neighbours for {rule}, stop at {stopAt}")
    
    for n in NEIGHBOURS:
        d = 1

        while d <= 1 or allowDistance:
            u = x + n[0] * d
            if u < 0 or u >= width: break

            v = y + n[1] * d
            if v < 0 or v >= height: break

            if stopAt and layout[v][u] == stopAt:
                if log_level >= 4: print(f"Seat {u},{v}, dist {d} from {x},{y} is {stopAt}")
                break
            if layout[v][u] == rule:
                if log_level >= 4: print(f"Seat {u},{v}, dist {d} from {x},{y} is {rule}")
                adjacentSeats += 1
                break
            
            if log_level >= 4: print(f"Seat {u},{v}, dist {d} from {x},{y} is NOT {rule}")
            d += 1

        if adjacentSeats >= limit: break

    return adjacentSeats

def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    # Initialize and read input
    
    layout = [[pos for pos in line] for line in input_stream.read().split('\n') if line.strip()]
    width = len(layout[0])
    height = len(layout)

    if log_level >= 1: print(f"Layout dimensions: {width}x{height}")

    # Select which part of day to run
    
    part_input = modules.userInput.get_int_input_constrained("Which part to run? 1-2 (defaults to 2): ", 1, 2, 2)

    # Run

    allowDistance = day_part != 1

    changes = []
    adjacentSeats:int
    targetAdjacents:int
    round = 0

    while True:
        for y in range(height):
            for x in range(width):
                if layout[y][x] == EMPTY_SEAT:
                    targetAdjacents = 0
                    adjacentSeats = count_neighbours(x, y, width, height, layout, allowDistance, OCCUPIED_SEAT, EMPTY_SEAT, targetAdjacents + 1, log_level)
                
                    if log_level >= 3: print(f"Round {round}: Seat {x},{y} has {adjacentSeats} neighbours")

                    if adjacentSeats == targetAdjacents:
                        if log_level >= 3: print(f"Round {round}: Seat {x},{y} going to be occupied")
                        changes.append((x, y, OCCUPIED_SEAT))
                elif layout[y][x] == OCCUPIED_SEAT:
                    targetAdjacents = 5 if allowDistance else 4
                    adjacentSeats = count_neighbours(x, y, width, height, layout, allowDistance, OCCUPIED_SEAT, EMPTY_SEAT, targetAdjacents, log_level)

                    if log_level >= 3: print(f"Round {round}: Seat {x},{y} has {adjacentSeats} neighbours")

                    if adjacentSeats == targetAdjacents:
                        if log_level >= 3: print(f"Round {round}: Seat {x},{y} going to be empty")
                        changes.append((x, y, EMPTY_SEAT))


        if len(changes) == 0:
            if log_level >= 1: print(f"No changes applied on round {round}")
            break
        for c in changes:
            if log_level >= 3: print(f"Round {round}: Seat {c[0]},{c[1]} is changing to {c[2]}")
            layout[c[1]][c[0]] = c[2]
            
        if log_level >= 2:
            print(f"Layout after round {round}")
            s = ""
            for y in range(height):
                for x in range(width): s += layout[y][x]
                print(s)
                s = ""

        changes.clear()
        round += 1

    occupiedCount = 0
    for y in range(height):
        for x in range(width):
            if layout[y][x] == OCCUPIED_SEAT: occupiedCount += 1

    print(f"Found {occupiedCount} occupied seats after {round} iterations")