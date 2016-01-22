"""Verify if the function is_appropriate() returns True when the given
list follows the correct format and conditions and returns False
otherwise.
"""
from convert_odd_input import is_appropriate

def test_is_appropriate():
    """Asserts that a given list contains two strings, that the first
    string only contains an integer, and that the second string only
    contains letters.
    """
    assert not is_appropriate(['123abc'])
    assert not is_appropriate(['abc123'])
    assert not is_appropriate(['abc', '123'])
    assert not is_appropriate(['a1b2c3', 'abc'])
    assert not is_appropriate(['123', '1a2b3c'])
    assert not is_appropriate(['123', 'abc', '123'])
    assert is_appropriate(['123', 'abc'])
