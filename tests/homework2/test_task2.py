from homework1.task2 import major_and_minor_elem


def test_positive_cases():
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_negative_case():
    assert not major_and_minor_elem([0, 0, 0, 7]) == 3
    assert not major_and_minor_elem([10, 10, 10, 2]) == (2, 1)
