from typing import Callable


def func(a: int, b: int) -> int:
    """Just a sample of a func"""
    return (a ** b) ** 2


def cache(funct: Callable) -> Callable:
    """
    Cache accepts another function as an argument. Then it
    returns such a function, so the every call to initial one
    should be cached
    """
    cach = {}

    def memoized_func(*args):
        if args in cach:
            return cach[args]
        result = funct(*args)
        cach[args] = result
        return result

    return memoized_func
