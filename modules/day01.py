"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

FIND_SUM = 2020

def getProductTwoElements(expenses, log_level):
    sum = 0
    for posA, valA in enumerate(expenses):
        for posB, valB in enumerate(expenses):
            if posA == posB: continue

            sum = valA + valB

            if sum == FIND_SUM:
                return ([(posA, valA), (posB, valB)], valA * valB)
            elif log_level >= 2:
                print(f"Expense[{posA}]({valA}) + Expense[{posB}]({valB}) sum {sum} does not equal {FIND_SUM}")

    return ([], -1)

def getProductThreeElements(expenses, log_level):
    sum = 0
    for posA, valA in enumerate(expenses):
        for posB, valB in enumerate(expenses):
            for posC, valC in enumerate(expenses):
                if posA == posB or posA == posC or posB == posC:
                    continue

                sum = valA + valB + valC

                if sum == FIND_SUM:
                    return ([(posA, valA), (posB, valB), (posC, valC)], valA * valB * valC)
                elif log_level >= 2:
                    print(f"Expense[{posA}]({valA}) + Expense[{posB}]({valB}) + Expense[{posC}]({valC}) sum {sum} does not equal {FIND_SUM}")

    return ([], -1)


def play(input_file, input_parameters, log_level):
    

    #Initialize and read input


    print("Day 1 begins!")

    expenses = []

    for i in input_file:
        expenses.append(int(i))
        
        if log_level >= 1:
            print(f"Added expense: {i}")


    #Part 1 of Day 1


    result = getProductTwoElements(expenses, log_level)

    if (result[1] >= 0):
        print(f"Values {result[0][0]} and {result[0][1]} product is {result[1]}")
    else:
        print("Unable to find values with a sum of {FIND_SUM}")


    #Part 2 of Day 1


    result = getProductThreeElements(expenses, log_level)

    if (result[1] >= 0):
        print(f"Values {result[0][0]} and {result[0][1]} and {result[0][2]} product is {result[1]}")
    else:
        print("Unable to find values with a sum of {FIND_SUM}")