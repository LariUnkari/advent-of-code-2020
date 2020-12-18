"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput

DIFF_MIN = 1
DIFF_MAX = 3
DEVICE_DIFF = 3

def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    # Initialize and read input
    
    adapters = [int(line) for line in input_stream.read().split('\n') if line.strip()]
    adapters.sort()

    if log_level >= 1:
        for i, a in enumerate(adapters): print(f"Adapter {i}, rated for {a} jolts")

    deviceRating = adapters[len(adapters) - 1] + DEVICE_DIFF
    adapters.append(deviceRating)

    if log_level >= 1: print(f"Device will be at {deviceRating} jolts")

    # Run

    if day_part == 1:
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
        pathsFound = [0] * len(adapters)

        a:int
        b:int
        d:int
        branchesFound:int
        for index in reversed(range(len(adapters)-1)):
            branchesFound = 0

            for i in range(index + 1, len(adapters)):
                a = adapters[index]
                b = adapters[i]
                d = b-a

                if d < DIFF_MIN or d > DIFF_MAX:
                    if log_level >= 3: print(f"Invalid next adapter[{i}] rating {b}, previous adapter[{index}] {a}, expecting diff {d} in range {DIFF_MIN}-{DIFF_MAX}, both inclusive")
                    break

                branchesFound += 1
                pathsFound[index] += max(1, pathsFound[i])
                if log_level >= 2: print(f"Found new branch from adapter[{index}] {a} to adapter[{i}] {b} which has {pathsFound[i]} options, total now {pathsFound[index]}")
        
            if log_level >= 1: print(f"Found {branchesFound} valid branches from adapter[{index}] {adapters[index]}, total now at {pathsFound[index]}")
            
        print(f"Found {pathsFound[0]} valid arrangements")