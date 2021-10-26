import pytest

from homework4.task4 import fizzbuzz


def test_fizzbuzz_raises_error():
    """
    Checking if fizzbuzz raises the ValueError if n <= 0"""
    with pytest.raises(ValueError):
        fizzbuzz(-1)
