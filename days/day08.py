"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, re, modules.userInput





def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input

    program = [(command[:3], int(command[4:].replace('+',''))) for command in input_stream.read().split('\n') if len(command) > 3]
    if log_level >= 1:
        for cmd in program: print(f"Found command: {cmd[0]} args: {cmd[1]}")

    # Select which part of day to run
    
    #part_input = modules.userInput.get_int_input_constrained("Which part to run? 1-2 (defaults to 2): ", 1, 2, 2)

    # Run

    i = 0
    acc = 0
    visited = {}
    
    cmd:str
    arg:int
    while i >= 0 and i < len(program):
        if i in visited:
            print(f"Revisiting line {i}, breaking out of loop with acc: {acc}")
            break

        visited[i] = True
        cmd = program[i][0]
        arg = program[i][1]

        if cmd == "jmp":
            if log_level >= 1: print(f"[{i}] Jumping by arg: {arg} to line: {i+arg}")
            i += arg
        else:
            if cmd == "nop":
                if log_level >= 1: print(f"[{i}] No operation, arg: {arg}")
            else:
                acc += arg
                if log_level >= 1: print(f"[{i}] Accumulate, arg: {arg}, acc: {acc}")

            i += 1

    print(f"\nProgram terminated with value {acc} in the accumulator")