import os

from homework1.task3 import find_maximum_and_minimum

file1 = os.path.join(os.path.dirname(__file__), 'tests_task3/test1.txt')
file2 = os.path.join(os.path.dirname(__file__), 'tests_task3/test2.txt')
file3 = os.path.join(os.path.dirname(__file__), 'tests_task3/test3.txt')
file4 = os.path.join(os.path.dirname(__file__), 'tests_task3/test4.txt')


def test_positive_case():
    """Checking sequences with len >= 1,
    including sequences with negative meanings"""
    assert find_maximum_and_minimum(file1) == (11, -5)
    assert find_maximum_and_minimum(file2) == (0, -10)
    assert find_maximum_and_minimum(file3) == (1, 0)
    assert find_maximum_and_minimum(file4) == (5, 5)
