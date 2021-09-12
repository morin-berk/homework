import pickle
from functools import wraps
from typing import Callable


def cache(times):
    """
    Cache accepts another function as an argument. Then it
    returns such a function, so the every call to initial one
    should be cached
    """
    values = {}

    def wrapper(func: Callable):

        @wraps(func)
        def memoized_func(*args, **kwargs):
            result = func(*args, **kwargs)
            key = pickle.dumps((args, kwargs))
            if key not in values:
                values[key] = func(*args, **kwargs)
                values['attempt'] = times - 1
                return values[key]
            if values['attempt'] > 0:
                values['attempt'] -= 1
                return values[key]
            return result
        return memoized_func
    return wrapper
