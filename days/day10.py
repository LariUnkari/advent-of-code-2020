"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput

DIFF_MIN = 1
DIFF_MAX = 3
DEVICE_DIFF = 3

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    adapters = []
    for line in input_stream.read().split('\n'):
        if len(line) == 0 or line.strip() == '\n':
            continue

        if log_level >= 1: print(f"Found adapter {len(nums)}, rated for {line} jolts")
        adapters.append(int(line))

    # Run

    adapters.sort()
    deviceRating = adapters[len(adapters) - 1] + DEVICE_DIFF
    adapters.append(deviceRating)

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