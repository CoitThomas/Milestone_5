"""Convert input in the form:
<positive_integer>,<string>
If the positive integer is odd, print the name in all capital letters.
Otherwise, print the name as it was entered.
"""
def is_appropriate(some_list):
    """Return True if the given input is a list of two strings, the
    first string only contains a number, and the second string only
    contains letters. Otherwise, return False.
    """
    assert isinstance(some_list, list), "The given parameter needs to be a list."
    for element in some_list:
        assert isinstance(element, str), "Both elements in the list needs to be a string."
    return len(some_list) == 2 and some_list[0].isdigit() and some_list[1].isalpha()

def is_odd(integer):
    """Return True if a given integer is odd. Otherwise, return False."""
    assert isinstance(integer, int), "The given parameter needs to be an integer."
    if integer%2 == 1:
        return True
    return False

def convert(some_string):
    """Parse a string into a list of two strings. Convert the first
    string into an integer. If the integer is an odd number, capitalize
    all the letters in the second string and return it. Otherwise, just
    return the second string.
    """
    assert isinstance(some_string, str), "The given parameter needs to be a string."
    parse_input = some_string.split(',')
    assert is_appropriate(parse_input), "Input needs to follow the format: positive_integer,name"

    number = int(parse_input[0])
    name = parse_input[1]

    if is_odd(number):
        name = name.upper()

    return name
