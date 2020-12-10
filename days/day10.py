"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput

DIFF_MIN = 1
DIFF_MAX = 3
DEVICE_DIFF = 3

def find_arrangements(adapters, index, pathsFound, log_level):
    if index == len(adapters) - 1:
        if log_level >= 1 or pathsFound % 100000 == 0:
           print(f"Found a viable path {pathsFound}")
        return pathsFound + 1

    for i in range(index + 1, len(adapters)):
        a = adapters[index]
        b = adapters[i]
        d = b-a

        if d < DIFF_MIN or d > DIFF_MAX:
            if log_level >= 3: print(f"Invalid next adapter[{i}] rating {b}, previous adapter[{index}] {a}, expecting diff {d} in range {DIFF_MIN}-{DIFF_MAX}, both inclusive")
            break

        if log_level >= 2: print(f"Found new branch for arrangement[{pathsFound}], adapter[{index}] {a} -> adapter[{i}] {b}")
        pathsFound = find_arrangements(adapters, i, pathsFound, log_level)

    return pathsFound

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    adapters = []
    for line in input_stream.read().split('\n'):
        if len(line) == 0 or line.strip() == '\n':
            continue

        if log_level >= 1: print(f"Found adapter {len(adapters)}, rated for {line} jolts")
        adapters.append(int(line))

    adapters.sort()
    deviceRating = adapters[len(adapters) - 1] + DEVICE_DIFF
    adapters.append(deviceRating)

    # Select which part of day to run
    
    part_input = modules.userInput.get_int_input_constrained("Which part to run? 1-2 (defaults to 2): ", 1, 2, 2)

    # Run

    if part_input[1] == 1:
        diffCounts = {}
        for i in range(DIFF_MIN, DIFF_MAX + 1):
            diffCounts[i] = 0

        allDiffs = []
    
        ratingPrevious = 0
        for a in adapters:
            d = a-ratingPrevious
            if d < DIFF_MIN or d > DIFF_MAX:
                print(f"Invalid adapter rating {a}, previous {ratingPrevious}, expecting diff {d} in range {DIFF_MIN}-{DIFF_MAX}, both inclusive")
                return
        
            if log_level >= 1: print(f"Adapter rating {a}, previous {ratingPrevious}, diff {d}")
            allDiffs.append(d)
        
        
            diffCounts[d] += 1
            ratingPrevious = a
    
        for c in diffCounts.keys():
            print(f"Found {diffCounts[c]} diffs of {c}")

        prod = diffCounts[1] * diffCounts[3]
        print(f"Final device rating is {deviceRating}, product of diff counts 1 ({diffCounts[1]}) 3 ({diffCounts[3]}) is {prod}")
    else:
        adapters.insert(0, 0)
        pathsFound = find_arrangements(adapters, 0, 0, log_level)

        print(f"Found {pathsFound} valid arrangements")