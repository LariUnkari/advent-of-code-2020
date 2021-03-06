"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput


def run(cmds, args, log_level):
    i = 0
    acc = 0
    visited = {}
    
    c:str
    a:int
    while i >= 0 and i < len(cmds):
        if i in visited:
            if log_level >= 1: print(f"Revisiting line {i}, breaking out of loop with acc: {acc}")
            return None

        visited[i] = True
        c = cmds[i]
        a = args[i]

        if c == "jmp":
            if log_level >= 1: print(f"[{i}] Jumping by arg: {a} to line: {i+a}")
            i += a
        else:
            if c == "nop":
                if log_level >= 1: print(f"[{i}] No operation, arg: {a}")
            else:
                acc += a
                if log_level >= 1: print(f"[{i}] Accumulate, arg: {a}, acc: {acc}")

            i += 1

    print(f"\nProgram terminated with value {acc} in the accumulator")
    return acc

def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    # Initialize and read input
    
    cmds = []
    args = []
    for line in input_stream.read().split('\n'):
        if len(line) < 3:
            continue
        
        if log_level >= 2: print(f"Found command: {line[:3]} args: {line[4:]}")

        cmds.append(line[:3])
        args.append(int(line[4:].replace('+','')))

    # Run

    if day_part == 1:
        run(cmds, args, log_level)
    else:
        lineToEdit:int = -1
        cmdToSet:str = ""

        # BRUTE FORCE, ENGAGE!
        retVal = None
        for index, cmd in enumerate(cmds):
            if cmd == "jmp":
                cmdToSet = "nop"
            elif cmd == "nop":
                cmdToSet = "jmp"
            else:
                continue
                
            cmds[index] = cmdToSet
            if log_level >= 1: print(f"Replaced command '{cmd}' at line {index} with {cmds[index]}")

            retVal = run(cmds, args, log_level - 1)
            if retVal != None:
                lineToEdit = index
                break
            
            cmds[index] = cmd
            retVal = None

        if lineToEdit >= 0:
            print(f"Replacing line {lineToEdit} command with '{cmdToSet}' allowed program to terminate with value {retVal} in accumulator")
        else:
            print("Failed to fix program :(")