import pytest

from homework3.task4 import is_armstrong


@pytest.mark.parametrize('test_input, expected',
                         [(9, True), (153, True),
                          (371, True), (9926315, True)])
def test_positive_case(test_input, expected):
    """Testing positive cases"""
    assert is_armstrong(test_input) == expected


@pytest.mark.parametrize('test_input, expected',
                         [(10, False), (408, False)])
def test_negative_case(test_input, expected):
    """Testing negative cases"""
    assert is_armstrong(test_input) == expected
