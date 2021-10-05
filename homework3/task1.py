import pickle
from functools import wraps
from typing import Callable


def cache(times) -> Callable:
    """Cache accepts another function as an argument. Then it
    returns such a function, so the every call to initial one
    should be cached"""
    values = {}
    if times <= 0:
        raise ValueError('Times` value must be greater than 0')

    def wrapper(func: Callable):
        @wraps(func)
        def memoized_func(*args, **kwargs):
            key = pickle.dumps((args, kwargs))
            if times == 1:
                return func(*args, **kwargs)
            if key not in values:
                values[key] = func(*args, **kwargs)
                values['attempt'] = times - 1
                return values[key]
            if values['attempt'] > 0:
                values['attempt'] -= 1
                if values['attempt'] == 0:
                    return values.pop(key)
                return values[key]
            return func(*args, **kwargs)
        return memoized_func
    return wrapper
