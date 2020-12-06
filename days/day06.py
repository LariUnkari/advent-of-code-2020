"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput



def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    #Initialize and read input

    inputs = [group.split('\n') for group in input_stream.read().split('\n\n')]
    if log_level >= 3: print(f"Inputs:\n{inputs}")

    # Select which part of day to run
    
    #part_input = modules.userInput.get_int_input_constrained("Which part to run? 1-2 (defaults to 2): ", 1, 2, 2)

    # Run
    
    sum = 0
    groupAnswers = {}
    groups = [{}] * len(inputs)
    for index, group in enumerate(inputs):
        for person in group:
            for answer in person:
                groupAnswers[answer] = True

        groups[index] = groupAnswers;
        if log_level >= 1: print(f"Group {index} answered yes to {len(groupAnswers)} questions")
        if log_level >= 2: print(f"Group {index} positive answers: {groupAnswers.keys()}")

        sum += len(groupAnswers)
        groupAnswers.clear()

    print(f"Sum of each groups answers: {sum}")