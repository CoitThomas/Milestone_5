"""Verify if the function is_odd returns True when a given integer is
odd and returns False when a given integer is even.
"""
from convert_odd_input import is_odd

def test_is_odd():
    """Assert that any integer given returns True if it is an odd
    integer and False if it is an even integer.
    """
    assert is_odd(101)
    assert not is_odd(20)
    assert is_odd(-5)
    assert not is_odd(-10)
    assert not is_odd(0)
