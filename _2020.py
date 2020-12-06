"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""


#Definitions

import importlib, modules.userInput

def get_day_input():
    """Takes in user input for day choice"""

    print(f"Select day (1-{0:d}), then press enter.\n".format(DAY_COUNT)+
          "Give an empty input or 'exit' to end program\n")

    return input("Choose the day: ")

def get_program_and_input(input_string):
    """Returns a day solution program and input as tuple (module, input_file). If invalid, returns (None, None)"""
    
    mod = None
    modName = "day{0:02d}"
    filepath = "data/day{0:02d}input.txt"

    try:
        value = int(input_string)

        if value < 1:
            print(f"Invalid day value {value} given!\n")
            return (None, None)
        elif value > DAY_COUNT:
            print(f"Day {value} has not been reached yet!\n")
            return (None, None)
        else:
            day = modName.format(value)
            print(f"Day {value} given, importing {day}")
            mod = importlib.import_module("."+day, package='days')
    except ValueError:
        print(f"Invalid input {input_string} given!")
        return (None, None)

    return (mod, open(filepath.format(value), "r"))


#Program

DAY_COUNT = 6
USER_INPUT = "0"

print("Advent of Code 2020 by Lari Unkari\n\n")

while True:
    USER_INPUT = get_day_input()
    
    if len(USER_INPUT) == 0 or USER_INPUT.strip() == "exit":
        break

    params = get_program_and_input(USER_INPUT)
    if params != None and params[0] != None:
        mod = params[0]
        if mod == None:
            print(f"No module found for {USER_INPUT}")
            break

        input_file = params[1]
        if input_file == None:
            print(f"No input file found for {USER_INPUT}")
            break

        #Input is a Tuple of (was_parse_success, list_of_int_values)
        program_input = modules.userInput.get_int_list_input("\nProgram input: ",
            "Invalid input {0}, try again or press enter without input to exit!")

        if not program_input[0]:
            break

        input_length = len(program_input)
        if input_length > 0:
            print(f"Input value list[0-{input_length-1}]: {program_input[1]}")
        else:
            print("No input given")

        log_level_input = modules.userInput.get_int_input("\nLog level (defaults to level zero): ", None)

        print("\n\n************************\n")
        mod.play(params[1], program_input[1], log_level_input[1] if log_level_input[0] else 0)
        print(f"\nModule {mod.__name__} program ended\n\n")

print("Goodbye and Merry Christmas 2020!")