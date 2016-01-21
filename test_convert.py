"""Verify if function convert() capitalizes all the letters in the
second part of a string when the first part of the string is a positive
odd integer.
"""
from convert_odd_input_from_user import convert

def test_convert():
    """Assert the correct output for various positive integers given to
    the function convert().
    """
    assert convert('1,hello') == 'HELLO'
    assert convert('12,world') == 'world'
    assert convert('123,jimmy') == 'JIMMY'
    assert convert('1234,Coit') == 'Coit'
    assert convert('12345,jOhN') == 'JOHN'
