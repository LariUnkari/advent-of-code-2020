"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, itertools, math, re, modules.userInput

RULE_LIST = 0
RULE_CHAR = 1

def build_valid(rules, startRule, log_level):
    return check_rule(rules, startRule, [startRule], log_level)

def check_rule(rules, key, path, log_level):
    rule = rules[key]
    if log_level >= 2: print(f"Checking rule '{key}' {rule}")

    if rule[0] == RULE_CHAR:
        if log_level >= 2: print(f"Char found: {rule[1]}")
        return [rule[1]]

    strings = []
    s:list
    opts:list
    prod:bool
    new:str

    for r in rule[1]:
        if log_level >= 2: print(f"'{key}' {len(r)} sub-rules: {r}")

        prod = False
        opts = []
        for i in range(len(r)):
            if log_level >= 3: print(f"'{key}' Sub-rule[i] {r[i]}")
            s = check_rule(rules, r[i], path + [r[i]], log_level)
            prod |= len(s) > 1
            opts.append(s)

        if prod:
            for p in itertools.product(*opts):
                new = "".join(p)
                if log_level >= 3: print(f"'{key}' String option {p} found")
                strings.append(new)
        else:
            new = "".join([o[0] for o in opts])
            strings.append(new)

        if log_level >= 2: print(f"String options found: {strings}")

    return strings

def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    # Initialize and read input
    
    rules = {}
    messages = []

    args:list
    for line in input_stream.read().split('\n'):
        line = line.strip()
        if len(line) == 0: continue

        if log_level >= 1: print(f"Evaluating line {line}")

        rMatch = re.search("(\d+): (.*)", line)
        if rMatch != None:
            if rMatch[2].startswith('\"'):
                rules[rMatch[1]] = (RULE_CHAR, rMatch[2].replace('\"',''))
            else:
                args = []
                for arg in rMatch[2].strip().split(' | '):
                    args.append(arg.strip().split(' '))
                rules[rMatch[1]] = (RULE_LIST, args)

            continue

        messages.append(line)

    print(f"{len(rules)} rules and {len(messages)} messages found")

    # Run

    validMessages = {}
    for msg in build_valid(rules, '0', log_level):
        validMessages[msg] = True

    count = 0
    for msg in messages:
        if msg in validMessages:
            count += 1

    print(f"Found {count} valid messages")
