from homework1.task4 import check_sum_of_four


def test_positive_case():
    """ Checking right answers """
    assert check_sum_of_four([0, 2], [-3, 5], [2, 1], [1, -7]) == 2
    assert check_sum_of_four([1, 2, 3], [-1, -2, -3],
                             [4, 5, 6], [-4, -5, -6]) == 19
    assert check_sum_of_four([10, 3, 4, 5], [10, 3, 4, -7],
                             [10, 3, 4, 4], [9, 3, 4, -2]) == 2


def test_negative_case():
    """ Checking wrong answers """
    assert not check_sum_of_four([1], [-2], [10], [-100]) == 1
    assert not check_sum_of_four([0, 2], [3, -2], [-2, -10], [-1, 10]) == 1
    assert not check_sum_of_four([0, 2], [3, -2], [-2, -10], [-1, 10]) == 3
