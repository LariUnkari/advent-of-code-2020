"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, math, re, modules.userInput

def find_multiplier(mod, val, multiplier, time):
    for i in range(mod):
        if (time + val) % mod == 0:
            multiplier *= mod
            break

        time += multiplier

    return (multiplier, time)

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    inputs = [line for line in input_stream.read().split('\n') if line.strip()]
    startTime = int(inputs[0])

    if log_level >= 1: print(f"Start time is {startTime}")

    buses = []
    for index, bus in enumerate(inputs[1].split(',')):
        if bus == 'x':
            if log_level >= 2: print(f"Bus {index} is unavailable")
        else:
            if log_level >= 2: print(f"Bus {index} is {bus}")
            buses.append((index, int(bus)))

    if log_level >= 1: print(f"Found {len(buses)} buses\n")

    # Select which part of day to run
    
    part_input = modules.userInput.get_int_input_constrained("Which part to run? 1-2 (defaults to 2): ", 1, 2, 2)

    # Run

    if part_input[1] == 1:
        time:int
        wait:int
        shift:int

        closestBus:int
        shortestWait = -1

        for index, bus in enumerate(buses):
            shift = startTime // bus[1]
            if shift * bus[1] < startTime: shift += 1
            time = shift * bus[1]
            wait = time - startTime
        
            if log_level >= 1: print(f"Bus[{index}] {bus[1]} shift {shift} leaves at {time}, wait: {time - startTime}")

            if wait < shortestWait or shortestWait < 0:
                shortestWait = wait
                closestBus = index
    
        print(f"Bus with shortest wait time is {buses[closestBus][1]} at time {startTime + shortestWait}, with waiting time of {shortestWait}")
        print(f"Bus ID multiplied with wait time is {buses[closestBus][1]*shortestWait}")
    else:
        multiplier = 1
        time = 0

        moduli = [1] * len(buses)
        for index in range(len(buses)):
            for i in (x for x in range(len(buses)) if x != index):
                moduli[index] *= buses[i][1]
            if log_level >= 2: print(f"Moduli of Bus[{index}] {buses[index][1]} is {moduli[index]}")

        val:int
        for index, bus in buses:
            if log_level >= 1: print(f"Bus[{index}] {bus} being evaluated, multiplier at {multiplier}")
            
            multiplier, time = find_multiplier(bus, index, multiplier, time)
            if log_level >= 2: print(f"Bus[{index}] {bus} timing match found at multiplier {multiplier}, time is now {time}")

        print(f"Time for buses to match up in timing is {time}")