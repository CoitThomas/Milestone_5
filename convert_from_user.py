"""Continually convert user input in the form:
<positive_integer>,<string>
If the positive integer is odd, print the string in all capital letters.
Otherwise, print the name as it was entered.
"""
import convert_odd_input

def get_input():
    """Prompts the user for input in the format:
    ####,name
    Receive the input as raw_input.
    """
    return raw_input("Enter a positive integer and a name (positive_integer,name): ")

if __name__ == "__main__":
    INPUT = get_input()
    while not INPUT.isspace() and INPUT:
        print convert_odd_input.convert(INPUT)
        INPUT = get_input()
