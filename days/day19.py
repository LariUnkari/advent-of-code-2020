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

        if log_level >= 2:
           print(f"'{key}' Found {len(strings)} string options found in path: {path} + {r}\n   {strings}")

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

    count = 0

    if day_part == 1:
        validMessages = {}

        for msg in build_valid(rules, '0', log_level):
            validMessages[msg] = True

        for msg in messages:
            if msg in validMessages:
                count += 1
    else:
        rules['8'][1].append(['42', '8'])
        rules['11'][1].append(['42', '11', '31'])

        rules_repeating = ['42', '31']
        validSequences = []
        sequences:list

        for i, r in enumerate(rules_repeating):
            validSequences.append({})
            sequences = build_valid(rules, r, log_level)

            for seq in sequences:
                validSequences[i][seq] = True

            if log_level >= 1:
                lengths = {}

                # Test for sequence lengths
                for seq in sequences:
                    if len(seq) not in lengths:
                        lengths[len(seq)] = True

                print(f"Rule[{i}] {r} results in {len(sequences)} of lengths: {list(lengths.keys())}\n{sequences}")
            else:
                print(f"Rule[{i}] {r} results in {len(sequences)}:\n{sequences}")

        for key in validSequences[0].keys():
            if key in validSequences[1]:
                print(f"ERROR: Matching sequence rules_repeating[0]={key} in both rules {rules_repeating}")
                

        # Magic number. Through testing, all permutations of given rules result in 8-char sequences.
        # I had an extra validation loop checking all lengths found but it was ugly and pointless due to the knowledge
        length = 8

        part:str
        seq:str
        num:int
        chk:int
        path = []

        for msg in messages:
            path.clear()

            if len(msg) % length != 0:
                if log_level >= 1: print(f"Message '{msg}' failed validation of length divisble by {length}")
                continue

            part = msg
            num = 0

            # The rule '11' means the end must match '31' and number of matches of '31' from
            # the right to left must be matched by an equal number of matches of '42', and
            # then any multiple of '42' matches as dicated by rule '8' all the way to the to the left

            while True:
                seq = part[-length:]
                if seq in validSequences[1]:
                    path.append(rules_repeating[1])
                    part = part[:-length]
                    num += 1
                else: break

            if num == 0:
                if log_level >= 1: print(f"Message '{msg}' failed validation of trailing sequences of {rules_repeating[1]}={rules[rules_repeating[1]][1]} as required by '11'={rules['11'][1]}")
                continue
            else:
                if log_level >= 2: print(f"Message '{msg}' validated {num} trailing sequences of {rules_repeating[1]}={rules[rules_repeating[1]][1]}")

            chk = num
            while num > 0:
                seq = part[-length:]
                if seq in validSequences[0]:
                    path.append(rules_repeating[0])
                    part = part[:-length]
                    num -= 1
                else: break

            if num > 0:
                if log_level >= 1: print(f"Message '{msg}' failed validation of {chk} leading sequences of {rules_repeating[0]}={rules[rules_repeating[0]][1]} as required by '11'={rules['11'][1]}")
                continue
            else:
                if log_level >= 2: print(f"Message '{msg}' validated {chk} leading sequences of {rules_repeating[0]}={rules[rules_repeating[0]][1]} as required by '11'={rules['11'][1]}")

            chk = 0
            while True:
                seq = part[-length:]
                if seq in validSequences[0]:
                    path.append(rules_repeating[0])
                    part = part[:-length]
                    chk += 1
                else: break

            if chk == 0:
                if log_level >= 1: print(f"Message '{msg}' failed validation of successive sequences of {rules_repeating[0]}={rules[rules_repeating[0]][1]} as required by '8'={rules['8'][1]}")
                continue

            if len(part) > 0:
                if log_level >= 1: print(f"Message '{msg}' failed validation of all remaining sequences of {rules_repeating[0]}={rules[rules_repeating[0]][1]} as required by '8'={rules['8'][1]}")
                continue

            if log_level >= 1: print(f"Message '{msg}' validated with sequences: {list(reversed(path))}")
            count += 1

    print(f"Found {count} valid messages")
