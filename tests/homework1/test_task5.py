import pytest

from homework1.task5 import find_maximal_subarray_sum


@pytest.mark.parametrize('test_input, k, expected',
                         [([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
                          ([10, 2, 1, 7], 2, 12),
                          ([-2, -4, -5, 10, -1], 4, 10),
                          ([15, 20, -3], 1, 20),
                          ([4, 7, -2, 2, 11, 9, -3], 111, 31)])
def test_positive_case(test_input, k, expected):
    """ Checking right answers """
    assert find_maximal_subarray_sum(test_input, k) == expected


@pytest.mark.parametrize('test_input, k, expected',
                         [([1, 3, 4], 2, 4),
                          ([-5, -10, 0, 14, 4], 5, 1)])
def test_negative_case(test_input, k, expected):
    """ Checking wrong answers """
    assert find_maximal_subarray_sum(test_input, k) != expected
