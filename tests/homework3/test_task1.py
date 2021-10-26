from typing import List

from homework3.task1 import cache


def test_func_with_int_args():
    """Testing whether caching works
    for a func with int arguments"""

    @cache(times=2)
    def func_int(a: int, b: int) -> int:
        """Just a sample of a func"""
        return (a ** b) ** 2

    some = 100, 200
    val_1 = func_int(*some)
    val_2 = func_int(*some)
    val_3 = func_int(*some)
    val_4 = func_int(*some)

    assert val_1 is val_2
    assert val_1 is not val_3
    assert val_3 is val_4


def test_func_with_list_arg():
    """Testing whether caching works
    for a func with a list argument"""

    @cache(times=2)
    def func_list(a: List) -> List:
        """Just a sample of a func"""
        return sum(a)

    some = [100, 200]
    val_1 = func_list(some)
    val_2 = func_list(some)
    val_3 = func_list(some)
    val_4 = func_list(some)

    assert val_1 is val_2
    assert val_1 is not val_3
    assert val_3 is val_4
