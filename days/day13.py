"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, math, re, modules.userInput

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    inputs = [line for line in input_stream.read().split('\n') if line.strip()]

    startTime = int(inputs[0])
    if log_level >= 1: print(f"Start time is {startTime}")

    buses = []#[int(entry) for entry in inputs[1].split(',')] if entry != "x"]
    
    for index, bus in enumerate(inputs[1].split(',')):
        if bus == 'x':
            if log_level >= 2: print(f"Bus {index} is unavailable")
        else:
            if log_level >= 2: print(f"Bus {index} is {bus}")
            buses.append(int(bus))

    if log_level >= 1: print(f"Found {len(buses)} buses")

    # Run

    time:int
    wait:int
    shift:int

    closestBus:int
    shortestWait = -1

    for index, bus in enumerate(buses):
        shift = startTime // bus
        if shift * bus < startTime: shift += 1
        time = shift * bus
        wait = time - startTime
        
        if log_level >= 1: print(f"Bus {bus} shift {shift} leaves at {time}, wait: {time - startTime}")

        if wait < shortestWait or shortestWait < 0:
            shortestWait = wait
            closestBus = index
    
    print(f"Bus with shortest wait time is {buses[closestBus]} at time {startTime + shortestWait}, with waiting time of {shortestWait}")
    print(f"Bus ID multiplied with wait time is {buses[closestBus]*shortestWait}")