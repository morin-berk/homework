from typing import List

from homework2.task4 import cache


def list_func(some_list: List) -> int:
    return sum(some_list)


def test_positive_case():
    """
    Testing if cache works even for func-s
    with list arguments
    """
    cache_func = cache(list_func)
    some_list = [1, 2, 3]
    val_1 = cache_func(some_list)
    val_2 = cache_func(some_list)
    assert val_1 == val_2
