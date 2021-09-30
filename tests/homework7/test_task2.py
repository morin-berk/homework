import pytest

from homework7.task2 import backspace_compare


def test_empty_str():
    """
    Testing str-s, consisting of one '#'
    """
    assert backspace_compare('#', '#')


def test_with_one_backspace():
    """
    Testing str-s, which contain only one backspace each
    """
    assert backspace_compare("ab#c", "ad#c")


@pytest.mark.parametrize('first, second',
                         [
                             ("a##c", "#a#c"),
                             ('a#####d##c#d', '###d'),
                             ('aa##', 'a#a')
                         ])
def test_with_two_or_more_backspaces(first, second):
    """
    Testing str, which contains two and more backspaces
    """
    assert backspace_compare(first, second)


def test_with_one_letter():
    """
    Testing two str, one of which contains only one letter
    """
    assert backspace_compare("a#c", "c")
