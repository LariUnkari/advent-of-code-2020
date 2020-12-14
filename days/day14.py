"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, itertools, math, re, modules.userInput

MASK_LENGTH = 36

def parse_binary(binary, name, log_level):
    s = "".join(binary)
    val = int(s, 2)

    if log_level >= 2:
        print(f"Parsed {name} {val} from binary {s}")

    return val

def write_to_memory(memory, pos, val, log_level):
    if log_level >= 1:
        if pos in memory:
            print(f"Mem[{pos}] set to {val}, was {memory[pos]}")
        else:
            print(f"Mem[{pos}] set to {val}, was not set")

    memory[pos] = val


def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    instructions = []

    cmd:str
    pos = None
    val = None

    parts:list
    for i in [line.strip() for line in input_stream.read().split('\n') if line.strip()]:
        parts = i.split(" = ")
        
        cmd = parts[0]
        if parts[0] == "mask":
            pos = None
            val = parts[1]
            if log_level >= 2: print(f"Instruction {len(instructions)} is '{cmd}' = '{val}'")
        else:
            cmd = parts[0][:3]
            pos = int(parts[0][4:-1])
            val = int(parts[1])
            if log_level >= 2: print(f"Instruction {len(instructions)} is '{cmd}[{pos}]' = '{val}'")
        
        instructions.append((cmd, pos, val))

    if log_level >= 1: print(f"Found {len(instructions)} instructions\n")

    # Select which part of day to run
    
    part_input = modules.userInput.get_int_input_constrained("Which part to run? 1-2 (defaults to 2): ", 1, 2, 2)

    # Run

    mask = ["X"] * MASK_LENGTH
    binary = ["0"] * MASK_LENGTH
    memory = {}

    floats = []
    s:str
    address:int
    for index, instr in enumerate(instructions):
        cmd = instr[0]
        pos = instr[1]
        val = instr[2]
        

        if cmd == "mask":
            if log_level >= 1:
                s = "".join(mask)
                print(f"[{index}] mask = '{val}'")

            for i in range(MASK_LENGTH):
                mask[i] = val[i]
        else:
            if log_level >= 1: print(f"[{index}] '{cmd}'[{pos}] = '{val}'")
            
            if part_input[1] == 1:
                s = "{0:b}".format(val)
                if log_level >= 2: print(f"Input value {val}, binary {s}")
            else:
                s = "{0:b}".format(pos)
                if log_level >= 2: print(f"Address value {pos}, binary {s}")

            for i in range(MASK_LENGTH):
                address = -1-i

                if part_input[1] == 1:
                    if mask[address] != "X":
                        binary[address] = mask[address]
                    elif i < len(s):
                        binary[address] = s[address]
                    else:
                        binary[address] = "0"
                else:
                    if mask[address] == "X":
                        binary[address] = "X"
                        floats.append(i)
                    elif mask[address] == "1":
                        binary[address] = mask[address]
                    elif i < len(s):
                        binary[address] = s[address]
                    else:
                        binary[address] = "0"

            if part_input[1] == 1:
                write_to_memory(memory, pos, parse_binary(binary, "value", log_level), log_level)
            else:
                if len(floats) > 0:
                    if log_level >= 2: print(f"Found {len(floats)} floats: {floats}")
                    for p in itertools.product(range(2), repeat=len(floats)):
                        for i in range(len(floats)):
                            address = -1-floats[i]
                            binary[address] = str(p[len(floats)-1-i])
                        
                        address = parse_binary(binary, "address permutation {0}".format(p), log_level)
                        write_to_memory(memory, address, val, log_level)
                    
                    floats.clear()
                else:
                    address = parse_binary(binary, "address", log_level)
                    write_to_memory(memory, address, val, log_level)


    print(f"\nDone processing instructions, memory has {len(memory)} entries")

    sum = 0
    for key in memory.keys():
        val = memory[key]
        if log_level >= 1: print(f"Memory[{key}] = {val}")
        sum += val

    print(f"\nSum of all memory values is {sum}")