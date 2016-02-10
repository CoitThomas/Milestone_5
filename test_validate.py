"""Verify if the function is_appropriate() returns True when the given
list follows the correct format and conditions and returns False
otherwise.
"""
from convert_odd_input import validate

def test_validate():
    """Asserts that a given list contains two strings, that the first
    string only contains an integer, and that the second string only
    contains letters.
    """
    assert not validate(['123abc'])
    assert not validate(['abc123'])
    assert not validate(['abc', '123'])
    assert not validate(['a1b2c3', 'abc'])
    assert not validate(['123', '1a2b3c'])
    assert not validate(['123', 'abc', '123'])
    assert validate(['123', 'abc'])
