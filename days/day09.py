"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    nums = []
    for line in input_stream.read().split('\n'):
        if len(line) == 0 or line.strip() == '\n':
            continue

        if log_level >= 1: print(f"Found number {len(nums)} {line}")
        nums.append(int(line))

    # Select which part of day to run
    
    #part_input = modules.userInput.get_int_input_constrained("Which part to run? 1-2 (defaults to 2): ", 1, 2, 2)

    # Run
    
    length = 25
    index = length

    matchFound = False
    while index < len(nums):
        for i in range(index - length, index):
            for j in range(index - length, index):
                if i == j:
                    continue

                if nums[index] == nums[i] + nums[j]:
                    if log_level >= 1: print(f"Value[{index}] {nums[index]} matched as sum of values A[{i}] {nums[i]} and B[{j}] {nums[j]}")

                    matchFound = True
                    break
                elif log_level >= 2: print(f"Value[{index}] {nums[index]} did not match as sum of values A[{i}] {nums[i]} and B[{j}] {nums[j]}")

            if matchFound:
                break
                
        if not matchFound:
            print(f"Value[{index}] {nums[index]} did not match as sum of any previous {length} numbers!")
            break
        
        index += 1
        matchFound = False
        