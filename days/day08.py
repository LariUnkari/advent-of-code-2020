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
            print(f"Revisiting line {i}, breaking out of loop with acc: {acc}")
            return (-1, acc)

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
    return (0, acc)

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    cmds = []
    args = []
    for line in input_stream.read().split('\n'):
        if len(line) < 3:
            continue
        
        if log_level >= 2: print(f"Found command: {line[:3]} args: {line[4:]}")

        cmds.append(line[:3])
        args.append(int(line[4:].replace('+','')))

    # Select which part of day to run
    
    part_input = modules.userInput.get_int_input_constrained("Which part to run? 1-2 (defaults to 2): ", 1, 2, 2)
    if part_input[1] == 1:
        run(cmds, args, log_level)
    else:
        lineToEdit:int = -1
        cmdToSet:str = ""
        newCmds = cmds.copy()

        # BRUTE FORCE, ENGAGE!
        retVal = None
        for index, cmd in enumerate(newCmds):
            if cmd == "jmp":
                newCmds[index] = "nop"
            elif cmd == "nop":
                newCmds[index] = "jmp"
                
            if log_level >= 1: print(f"Replaced command {cmd} at line {index} with {newCmds[index]}")
            retVal = run(newCmds, args, log_level - 1)
            if retVal[0] == 0:
                lineToEdit = index
                cmdToSet = newCmds[index]
                print(f"Replacing line {lineToEdit} command with {cmdToSet} allowed program to terminate")
                break
            
            newCmds[index] = cmd
            retVal = None

        print(f"Final value in accumulator with fixed program: {retVal[1]}")
        cmds[lineToEdit] = cmdToSet

    # Run
