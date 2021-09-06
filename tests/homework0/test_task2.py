from homework0.task2 import check_fibonacci


def test_positive_case():
    """ Checking how the func works with True fib sequences """
    assert check_fibonacci([0, 1, 1, 2, 3, 5])
    assert check_fibonacci([89, 144, 233, 377])


def test_negative_case():
    """
    Checking how the func works with False fib sequences,
    len(list) <= 3
    """
    assert not check_fibonacci([0, 1, 2])
    assert not check_fibonacci([13, 22, 34, 55, 89, 144, 233, 377])
    assert not check_fibonacci([0, 1])
    assert not check_fibonacci([1])
