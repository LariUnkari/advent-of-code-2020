"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

def get_int_input(prompt, invalid_prompt):
    """Get integer input from user, returns a tuple (is_valid, input_value)"""

    input_value = 0
    is_input_valid = False
    while not is_input_valid:
        txt = input(prompt)

        if len(txt) == 0:
            break

        try:
            input_value = int(txt)
            is_input_valid = True
        except ValueError:
            if invalid_prompt != None:
                print(invalid_prompt.format(input_value))
            else:
                break

    return (is_input_valid, input_value)

def get_int_input_constrained(prompt, value_min, value_max, value_default):
    """Get integer input from user, constrained within min-max (inclusive),
       default for unparseable values, returns a tuple (is_valid, input_value)"""

    input_value = 0
    while input_value < 1:
        txt = input(prompt)
        try:
            input_value = min(max(int(txt), value_min), value_max)
        except ValueError:
            input_value = value_default

    return (True, input_value)

def get_int_list_input(prompt, invalid_prompt):
    """Get integer list input from user, returns a tuple (is_valid, input_list)"""

    input_list = []
    is_input_valid = False

    while not is_input_valid:
        is_input_valid = True
        input_text = input(prompt)

        #Empty input is valid too
        if len(input_text) == 0:
            break

        try:
            for txt in input_text.split(","):
                input_list.append(int(txt))
        except ValueError:
            input_list = []
            is_input_valid = False

            if invalid_prompt != None:
                print(invalid_prompt.format(input_text))
            else:
                break

    return (is_input_valid, input_list)