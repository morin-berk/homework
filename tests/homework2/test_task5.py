import string

from homework2.task5 import custom_range


def test_positive_case():
    assert custom_range(string.ascii_lowercase, 'g') == \
           ['a', 'b', 'c', 'd', 'e', 'f']
    assert custom_range(string.ascii_lowercase, 'g', 'p') == \
           ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == \
           ['p', 'n', 'l', 'j', 'h']
    assert custom_range([1, 2, 3, 4, 5], 4, 0, -1) == [4, 3, 2, 1]
    assert custom_range(string.ascii_uppercase, 'K', 'W', 2) == \
           ['K', 'M', 'O', 'Q', 'S', 'U']
