from homework1.task4 import cache, func


def test_positive_case():
    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 == val_2
