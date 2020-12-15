"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, itertools, math, re, modules.userInput

TURN_NUMBER = 2020

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    starters = [int(line) for line in input_stream.read().strip().split(',')]
    if log_level >= 1: print(f"Found {len(starters)} starting numbers: {starters}")

    # Run

    memory = {}
    turn = 0

    num = -1
    prev = num
    while turn < TURN_NUMBER:
        turn += 1

        if turn <= len(starters):
            num = starters[turn - 1]
        else:
            if prev in memory:
                num = turn - 1 - memory[prev]
                if log_level >= 2: print(f"[{turn}] Previous number {prev} was said on turn {memory[prev]}, so age is {num}")
            else:
                num = 0
                if log_level >= 2: print(f"[{turn}] Previous number {prev} was said for the first time on previous turn")
                
        memory[prev] = turn - 1
            
        if log_level >= 1: print(f"[{turn}] Number {num}")
        prev = num

    print(f"\nNumber on turn {TURN_NUMBER} is {num}")