import pytest

from homework7.task2 import backspace_compare


def test_empty_str():
    assert backspace_compare('#', '#')


def test_with_one_backspace():
    assert not backspace_compare("ab#c", "ad#c")


@pytest.mark.parametrize('first, second',
                         [
                             ("a##c", "#a#c"),
                             ('aa##', 'a#a')
                         ])
def test_with_two_or_more_backspaces(first, second):
    assert backspace_compare(first, second)


def test_with_one_letter():
    assert not backspace_compare("a#c", "c")
    assert backspace_compare("#c", "c")


def test_with_empty_str():
    assert backspace_compare("#", "")


def test_str_without_backspace():
    assert backspace_compare("aaa", "aaa")
    assert not backspace_compare("ab", "abc")
