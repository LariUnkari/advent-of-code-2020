"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput

EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'
NEIGHBOURS = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

def count_neighbours(x, y, width, height, layout, rule, stopAt, log_level):
    adjacentSeats = 0
    u:int
    v:int

    for n in NEIGHBOURS:
        u = x + n[0]
        if u < 0 or u >= width: continue

        v = y + n[1]
        if v < 0 or v >= height: continue

        if layout[v][u] == rule:
            adjacentSeats += 1

        if adjacentSeats == stopAt:
           return adjacentSeats

    return adjacentSeats

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    layout = [[pos for pos in line] for line in input_stream.read().split('\n') if line.strip()]
    width = len(layout[0])
    height = len(layout)

    if log_level >= 1: print(f"Layout dimensions: {width}x{height}")

    # Run

    changes = []
    adjacentSeats:int
    round = 0

    while True:
        for y in range(height):
            for x in range(width):
                if layout[y][x] == EMPTY_SEAT:
                    adjacentSeats = count_neighbours(x, y, width, height, layout, OCCUPIED_SEAT, 1, log_level)
                
                    if log_level >= 2: print(f"Round {round}: Seat {x},{y} has {adjacentSeats} neighbours")

                    if adjacentSeats == 0:
                        if log_level >= 3: print(f"Round {round}: Seat {x},{y} going to be occupied")
                        changes.append((x, y, OCCUPIED_SEAT))
                elif layout[y][x] == OCCUPIED_SEAT:
                    adjacentSeats = count_neighbours(x, y, width, height, layout, OCCUPIED_SEAT, 4, log_level)

                    if log_level >= 2: print(f"Round {round}: Seat {x},{y} has {adjacentSeats} neighbours")

                    if adjacentSeats == 4:
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