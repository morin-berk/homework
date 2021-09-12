from homework3.task1 import cache


def test_num_cases():
    """Testing whether caching works for func with num arguments"""

    @cache(times=2)
    def func(a: int, b: int) -> int:
        """Just a sample of a func"""
        return (a ** b) ** 2

    some = 100, 200
    val_1 = func(*some)
    val_2 = func(*some)
    val_3 = func(*some)

    assert val_1 is val_2
    assert val_1 is not val_3
