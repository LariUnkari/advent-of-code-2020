"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput

ROWS = 128
COLS = 8

def find_position(index, steps, upper, capacity, log_level):
    start = 0
    end = capacity
    half = capacity
    
    if log_level >= 2:
        print(f"Seat {index} {upper} position between {start}-{end}")

    for r in range(len(steps)):
        half = round(half / 2)

        if steps[r] == upper:
            start += half
        else:
            end -= half

        if log_level >= 2:
            print(f"Seat {index} section towards {steps[r]}, position between {start}-{end}")

    return end

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    #Initialize and read input

    inputs = input_stream.read().split('\n')
    entries = []
    for i in range(len(inputs) - 1):
        if log_level >= 1:
            print(f"Seat {index} data: {inputs[i][:7]},{inputs[i][7:]}")
        entries.append((inputs[i][:7], inputs[i][7:]))

    # Select which part of day to run
    
    #part_input = modules.userInput.get_int_input_constrained("Which part to run? 1-2 (defaults to 2): ", 1, 2, 2)

    # Run

    highest_id = -1
    row = 0
    col = 0
    id = 0

    for index, entry in enumerate(entries):
        row = find_position(index, entry[0], 'B', ROWS - 1, log_level)
        col = find_position(index, entry[1], 'R', COLS - 1, log_level)
        id = row * COLS + col

        if log_level >= 1:
            print(f"Seat {index} position is R[{entry[0]}]:{row} C[{entry[1]}]:{col} ID:{id}")

        if id > highest_id:
            highest_id = id

    print(f"Highest seat ID:{highest_id}")