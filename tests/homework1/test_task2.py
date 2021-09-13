import pytest

from homework1.task2 import check_fibonacci


@pytest.mark.parametrize('test_input', [([0, 1, 1, 2, 3, 5]),
                         ([89, 144, 233, 377]), ([0, 1])])
def test_positive_case(test_input):
    """ Checking how the func works with True fib sequences """
    assert check_fibonacci(test_input)


@pytest.mark.parametrize('test_input', [([0, 1, 2]), ([4, 4, 8, 12]),
                         ([13, 22, 34, 55, 89, 144, 233, 377])])
def test_negative_case(test_input):
    """
    Checking how the func works with False fib sequences.
    """
    assert not check_fibonacci(test_input)
