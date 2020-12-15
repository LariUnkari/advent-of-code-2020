"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, itertools, math, re, modules.userInput

TARGETS = [2020, 30000000]

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    starters = [int(line) for line in input_stream.read().strip().split(',')]
    if log_level >= 1: print(f"Found {len(starters)} starting numbers: {starters}")

    # Select which part of day to run
    
    part_input = modules.userInput.get_int_input_constrained("Which part to run? 1-2 (defaults to 2): ", 1, 2, 2)
    target = TARGETS[part_input[1] - 1]
    print(f"Target turn is: {target}")

    if part_input[1] == 2: print(f"Brute force goes BRRRRRRRR just fine! :D")

    # Run

    memory = {}
    turn = 0

    num = -1
    prev = num

    for i in starters:
        turn += 1
        num = i

        if log_level >= 1 or turn % 100000 == 0: print(f"[{turn}] Starter number {num}")

        if turn > 1: memory[prev] = turn - 1
        prev = num

    while turn < target:
        if prev in memory:
            num = turn - memory[prev]
            if log_level >= 2: print(f"[{turn+1}] Previous number {prev} was said on turn {memory[prev]}, so age is {num}")
        else:
            num = 0
            if log_level >= 2: print(f"[{turn+1}] Previous number {prev} was said for the first time on previous turn")
                
        memory[prev] = turn
        prev = num
            
        turn += 1
        if log_level >= 1 or turn % 100000 == 0: print(f"[{turn}] Number {num}")

    print(f"\nNumber on turn {target} is {num}")