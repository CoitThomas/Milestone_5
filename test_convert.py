"""Verify if function convert() capitalizes all the letters in the
second part of a string when the first part of the string is a positive
odd integer.
"""
from convert_odd_input import convert

def test_convert():
    """Assert the correct output for various positive integers given to
    the function convert().
    """
    assert convert('1,hello') == '1,HELLO'
    assert convert('12,world') == '12,world'
    assert convert('123,jimmy') == '123,JIMMY'
    assert convert('1234,Coit') == '1234,Coit'
    assert convert('12345,jOhN') == '12345,JOHN'
