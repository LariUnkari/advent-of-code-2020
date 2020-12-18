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

def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    #Initialize and read input

    inputs = input_stream.read().split('\n')
    entries = []
    for i in range(len(inputs) - 1):
        if log_level >= 1:
            print(f"Seat {i} data: {inputs[i][:7]},{inputs[i][7:]}")
        entries.append((inputs[i][:7], inputs[i][7:]))

    # Run

    seats = [None] * ROWS * COLS
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

        if day_part == 1:
            if id > highest_id:
                highest_id = id
        else:
            seats[id] = (row, col)

    if day_part == 1:
        print(f"Highest seat ID:{highest_id}")
    else:
        for i in range(ROWS * COLS):
            if seats[i] == None:
                row = i // COLS
                col = i - row

                if (i + 1 < len(seats) and seats[i+1] == None) or (i > 0 and seats[i-1] == None):
                    if log_level >= 1:
                        print(f"Seat {i} at R{row},C{col} is missing!")
                else:
                    print(f"My seat is ID:{i} at R{row},C{col}")
                    break