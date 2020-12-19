"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, itertools, math, re, modules.userInput

def process_section(expression, depth, day_part):
    value = 0
    start = 0
    end = 0
    nextClose = 0
    nextOpen = 0

    while start >= 0:
        start = expression.find('(')
        end = expression.find(')')

        if start < 0:
            break

        nextOpen = expression.find('(', start+1)

        if nextOpen >= start and nextOpen < end:
            start = nextOpen
            value, nextOpen, nextClose = process_section(expression[start+1:end], depth + 1, day_part)
        elif start < end:
            value, nextOpen, nextClose = process_section(expression[start+1:end], depth + 1, day_part)
                
        new_expression = expression[:start] + str(value) + expression[end+1:]
        expression = new_expression

    if day_part == 1:
        value = calculate_part1(expression)
    else:
        value = calculate_part2(expression)

    return value, start, end

def get_next_multiplication(expression):
    return re.search("(\d+)\*(\d+)", expression)

def get_next_addition(expression):
    return re.search("(\d+)\+(\d+)", expression)

def calculate_part1(expression):
    value = 0
    plus = None
    mult = None

    while True:
        plus = get_next_addition(expression)
        mult = get_next_multiplication(expression)

        if mult == None and plus == None:
            break

        if plus == None or (mult != None and mult.span()[0] < plus.span()[0]):
            value, expression = calc_mult(mult, expression)
        else:
            value, expression = calc_plus(plus, expression)

    return value

def calculate_part2(expression):
    value = 0
    plus = None
    mult = None

    while True:
        plus = get_next_addition(expression)
        if plus == None: break
        value, expression = calc_plus(plus, expression)
            
    while True:
        mult = get_next_multiplication(expression)
        if mult == None: break
        value, expression = calc_mult(mult, expression)

    return value

def calc_mult(matchObject, expression):
    start, end = matchObject.span()
    value = int(matchObject[1]) * int(matchObject[2])
    expression = expression[:start] + str(value) + expression[end:]
    return value, expression

def calc_plus(matchObject, expression):
    start, end = matchObject.span()
    value = int(matchObject[1]) + int(matchObject[2])
    expression = expression[:start] + str(value) + expression[end:]
    return value, expression

def play(input_stream:io.TextIOWrapper, day_part, input_parameters, log_level):
    
    # Initialize and read input
    
    inputs = [line.strip().replace(' ', '') for line in input_stream.read().split('\n') if line.strip()]
    print(f"Expressions found: {len(inputs)}")

    # Run

    results = [0] * len(inputs)
    for i, expression in enumerate(inputs):
        results[i] = process_section(expression, 0, day_part)[0]
        if log_level >= 1: print(f"Expression[{i}] result is {results[i]}")

    total = sum([val for val in results])
    print(f"\nSum of all expressions is {total}")