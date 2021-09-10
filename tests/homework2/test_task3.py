from homework2.task3 import combinations


def test_positive_case():
    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]


def test_negative_case():
    assert not combinations([0, 2], [1, 3]) == [[0, 1], [2, 3], [0, 3]]
