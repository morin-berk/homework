import pickle
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
    cache_dict = {}

    def memoized_func(*args, **kwargs) -> Callable:
        key = pickle.dumps((args, kwargs))
        if key in cache_dict:
            return cache_dict[key]
        result = funct(*args)
        cache_dict[key] = result
        return result

    return memoized_func
