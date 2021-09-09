from homework0.task3 import find_maximum_and_minimum


def test_positive_case():
    """
    Checking sequences with len >= 1,
    including sequences with negative meanings
    """
    assert find_maximum_and_minimum('tests_task3/test1.txt') == (11, -5)
    assert find_maximum_and_minimum('tests_task3/test2.txt') == (0, -10)
    assert find_maximum_and_minimum('tests_task3/test3.txt') == (1, 0)
    assert find_maximum_and_minimum('tests_task3/test4.txt') == (5, 5)
