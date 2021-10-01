import pytest

from homework2.task2 import major_and_minor_elem


@pytest.mark.parametrize('array, expected',
                         [
                             ([3, 2, 3], (3, 2)),
                             ([2, 2, 1, 1, 1, 2, 2], (2, 1))
                         ])
def test_positive_case(array, expected):
    """
    Testing if the func returns (max, min) elements,
    basing on their frequency
    """
    assert major_and_minor_elem(array) == expected
