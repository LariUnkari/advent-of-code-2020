"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput



def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    #Initialize and read input

    inputs = [group.split('\n') for group in input_stream.read().split('\n\n')]
    if log_level >= 3: print(f"Inputs:\n{inputs}")

    # Run
    
    sum = 0

    groupAnswers = {}
    groups = [{}] * len(inputs)
    groupAnswerCounts = []

    for index, group in enumerate(inputs):
        groupAnswerCounts.append({})

        for id, person in enumerate(group):
            for answer in person:
                if day_part == 1:
                    groupAnswers[answer] = True
                else:
                    if answer in groupAnswerCounts[index]:
                        groupAnswerCounts[index][answer] += 1
                    else:
                        groupAnswerCounts[index][answer] = 1
            
        groups[index] = groupAnswers;

        if day_part == 1:
            if log_level >= 1: print(f"Group {index} answered yes to {len(groupAnswers)} questions")
        else:
            for answer, count in groupAnswerCounts[index].items():
                if count >= len(group):
                    groupAnswers[answer] = True

            if log_level >= 1: print(f"All {len(group)} of group {index} answered yes to {len(groupAnswers)} question")
            
        if log_level >= 2: print(f"All group {index} positive answers: {groupAnswers.keys()}")

        sum += len(groupAnswers)
        groupAnswers.clear()

    print(f"Sum of each groups answers: {sum}")