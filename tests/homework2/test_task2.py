from homework2.task2 import major_and_minor_elem


def test_positive_case():
    """
    Testing if the func returns (max, min) elements,
    basing on their frequency
    """
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)
