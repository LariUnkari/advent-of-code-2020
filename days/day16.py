"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, itertools, math, re, modules.userInput

TARGETS = [2020, 30000000]

def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    # Initialize and read input
    
    inputs = input_stream.read().split('\n')

    rules = []
    myTicket = []
    nearbyTickets = {}

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

        groups = re.findall("(.*): (\d+)-(\d+) or (\d+)-(\d+)", line)[0]
        rules.append((groups[0], int(groups[1]), int(groups[2]), int(groups[3]), int(groups[4])))
        
    if log_level >= 1: print(f"Reading my ticket at line {index}")
    myTicket = [int(d) for d in inputs[index].split(',')]

    if log_level >= 1: print(f"Found {len(myTicket)} fields for my ticket")
    if log_level >= 2:
        for ticket in myTicket: print(f"{ticket}")

    index += 3
    if log_level >= 1: print(f"Reading nearby tickets starting at line {index}")

    for i, line in enumerate(inputs[index:]):
        if line.strip():
            nearbyTickets[i] = ([int(d) for d in line.split(',')])

    if log_level >= 1: print(f"Found {len(nearbyTickets)} nearby tickets")
    if log_level >= 2:
        for n in range(len(nearbyTickets)): print(f"{nearbyTickets[n]}")

    # Run
    
    failedTickets = []
    failedValues = []
    fail = None

    for i in nearbyTickets.keys():
        for value in nearbyTickets[i]:
            fail = value

            for r, rule in enumerate(rules):
                if value >= rule[1] and value <= rule[2]:
                    if log_level >= 3: print(f"Ticket[{i}] value {value} validated by rule[{r}] {rule[1]}-{rule[2]}")
                    fail = None
                elif value >= rule[3] and value <= rule[4]:
                    if log_level >= 3: print(f"Ticket[{i}] value {value} validated by rule[{r}] {rule[3]}-{rule[4]}")
                    fail = None

            if fail != None:
                if log_level >= 1: print(f"Ticket[{i}] failed validation of value {fail}")
                failedTickets.append(i)
                failedValues.append(fail)
                break
        
        failedValue = None

    for i in failedTickets:
        del nearbyTickets[i]

    ticketCount = len(nearbyTickets)
    print(f"Failed validation of {len(failedValues)} tickets, {ticketCount} valid tickets remain")
    if log_level >= 1: print(f"Failed values {failedValues}")
    print(f"Error rate: {sum(failedValues)}")
    
    validatedValuesPerRule = {}
    for i in range(len(myTicket)):
        validatedValuesPerRule[i] = [0] * len(rules)
    
    for i in nearbyTickets.keys():
        for n, value in enumerate(nearbyTickets[i]):
            for r, rule in enumerate(rules):
                if (value >= rule[1] and value <= rule[2]) or (value >= rule[3] and value <= rule[4]):
                    if log_level >= 3: print(f"Ticket[{index}] value {value} validated by rule[{r}] {rule[1]}-{rule[2]} or {rule[3]}-{rule[4]}")
                    validatedValuesPerRule[n][r] += 1

    for r in validatedValuesPerRule.keys():
        if log_level >= 2: print(f"Field {r} validated for rules: {validatedValuesPerRule[r]}")

    ruleIndices = {}
    fieldRules:list

    while len(ruleIndices) < len(rules):
        for r in range(len(rules)):
            if r in ruleIndices:
                continue

            index = -1

            for n in validatedValuesPerRule.keys():
                if validatedValuesPerRule[n][r] == ticketCount:
                    if index == -1:
                        index = n
                    else:
                        if log_level >= 3: print(f"Multiple fields validate rule {r}")
                        index = -1
                        break

            if index != -1:
                if log_level >= 1: print(f"Field {index} is rule {r} '{rules[r][0]}'")

                ruleIndices[r] = index
                del validatedValuesPerRule[index]

                if log_level >= 2: 
                    for i in validatedValuesPerRule.keys():
                        print(f"Field {i} validated for rules: {validatedValuesPerRule[i]}")

        for n in validatedValuesPerRule.keys():
            index = -1

            for r in range(len(rules)):
                if validatedValuesPerRule[n][r] == -1:
                    continue

                if validatedValuesPerRule[n][r] == ticketCount:
                    if index == -1:
                        index = r
                    else:
                        if log_level >= 3: print(f"Multiple rules validated by field {n}")
                        index = -1
                        break

            if index != -1:
                if log_level >= 1: print(f"Field {n} is rule {index} '{rules[r][0]}'")

                ruleIndices[index] = n
                for i in validatedValuesPerRule.keys():
                    fieldRules = validatedValuesPerRule[i][index] = -1

                if log_level >= 2: 
                    for i in validatedValuesPerRule.keys():
                        print(f"Field {i} validated for rules: {validatedValuesPerRule[i]}")

    value = 1

    for r, rule in enumerate(rules):
        if log_level >= 1: print(f"Rule {rule[0]} is field {ruleIndices[r]}")

        if rule[0].startswith("departure"):
            if log_level >= 1: print(f"My ticket {rule[0]} value is {myTicket[ruleIndices[r]]}")
            value *= myTicket[ruleIndices[r]]

    print(f"Product of departure values on my ticket: {value}")