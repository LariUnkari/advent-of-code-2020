"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, itertools, math, re, modules.userInput

TARGETS = [2020, 30000000]

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    inputs = input_stream.read().split('\n')

    rules = []
    myTicket = []
    nearbyTickets = []

    index = 0
    if log_level >= 1: print(f"Reading rules starting at line {index}")

    groups = None
    for i, line in enumerate(inputs):
        if not line.strip():
            if log_level >= 1:
                print(f"Found {len(rules)} rules, stop at line {i}")
            if log_level >= 2:
                for r in rules: print(f"{r[0]}: {r[1]}-{r[2]} or {r[3]}-{r[4]}")
                
            index += i + 2
            break

        groups = re.findall("(\w+): (\d+)-(\d+) or (\d+)-(\d+)", line)[0]
        rules.append((groups[0], int(groups[1]), int(groups[2]), int(groups[3]), int(groups[4])))
        
    if log_level >= 1: print(f"Reading my ticket at line {index}")
    myTicket = [int(d) for d in inputs[index].split(',')]

    if log_level >= 1: print(f"Found {len(myTicket)} fields for my ticket")
    if log_level >= 2:
        for ticket in myTicket: print(f"{ticket}")

    index += 3
    if log_level >= 1: print(f"Reading nearby tickets starting at line {index}")

    for i, line in enumerate(inputs[index:]):
        nearbyTickets.append([int(d) for d in line.split(',') if line.strip()])

    if log_level >= 1: print(f"Found {len(nearbyTickets)} nearby tickets")
    if log_level >= 2:
        for n in range(len(nearbyTickets)): print(f"{nearbyTickets[n]}")

    # Run
    
    failedValues = []
    fail = None
    for index, ticket in enumerate(nearbyTickets):
        for value in ticket:
            fail = value

            for i, rule in enumerate(rules):
                if value >= rule[1] and value <= rule[2]:
                    if log_level >= 2: print(f"Ticket[{index}] value {value} validated by rule[{i}] {rule[1]}-{rule[2]}")
                    fail = None
                    break

                if value >= rule[3] and value <= rule[4]:
                    if log_level >= 2: print(f"Ticket[{index}] value {value} validated by rule[{i}] {rule[3]}-{rule[4]}")
                    fail = None
                    break

            if fail != None:
                if log_level >= 1: print(f"Ticket[{index}] failed validation of value {fail}")
                failedValues.append(fail)
                break
        
        failedValue = None

    print(f"Failed validation of {len(failedValues)} values: {failedValues}")
    print(f"Error rate: {sum(failedValues)}")