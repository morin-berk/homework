import string

from homework2.task5 import custom_range


def test_positive_case_one_slice():
    assert custom_range(string.ascii_lowercase, 'g') == \
           ['a', 'b', 'c', 'd', 'e', 'f']


def test_positive_case_two_slices():
    assert custom_range(string.ascii_lowercase, 'g', 'p') == \
           ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


def test_positive_case_three_slices():
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == \
           ['p', 'n', 'l', 'j', 'h']


def test_positive_case_list_of_integers():
    assert custom_range([1, 2, 3, 4, 5], 4, 0, -1) == [4, 3, 2, 1]


def test_positive_case_upper_case():
    assert custom_range(string.ascii_uppercase, 'K', 'W', 2) == \
           ['K', 'M', 'O', 'Q', 'S', 'U']
