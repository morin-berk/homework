from homework0.task5 import find_maximal_subarray_sum


def test_positive_case():
    """ Checking right answers """
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16
    assert find_maximal_subarray_sum([10, 2, 1, 7], 2) == 12
    assert find_maximal_subarray_sum([-2, -4, -5, 10, -1], 4) == 0
    assert find_maximal_subarray_sum([15, 20, -3], 1) == 20


def test_negative_case():
    """ Checking wrong answers """
    assert find_maximal_subarray_sum([1, 3, 4], 2) != 4
    assert find_maximal_subarray_sum([-5, -10, 0, 14, 4], 5) != 1
