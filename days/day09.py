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

    # Run

    invalidIndex = -1
    
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
            invalidIndex = index
            break
        
        index += 1
        matchFound = False

    if invalidIndex == -1:
        print(f"No invalid numbers found")
        return
    else:
        print(f"Part 1: Value[{invalidIndex}] {nums[invalidIndex]} did not match as sum of any previous {length} numbers!")

    val = nums[invalidIndex]
    low = -1
    high = -1

    index = 0
    sum:int
    while index < len(nums):
        if index == invalidIndex or index + 1 == invalidIndex:
            index += 1
            continue

        low = index
        high = index + 1
        sum = nums[low] + nums[high]
        if log_level >= 2: print(f"Sum of values[{low}] to values[{high}] is {sum}")

        while sum < val:
            high += 1
            sum += nums[high]
            if log_level >= 2: print(f"Sum of values[{low}] to values[{high}] is {sum}")
            
        if sum == val:
            break
        
        if log_level >= 1: print(f"Sum of values[{low}] to values[{high}] is {sum} and exceeded {val}")

        index += 1

    if low >= 0 and high >= 0:
        vals = nums[low:high+1]
        print(f"Values adding up to {val} range from values[{low}] to values[{high}]: {vals}")

        low = min(vals)
        high = max(vals)
        sum = low + high

        print(f"Sum of lowest {low} and highest {high} values in range is {sum}")