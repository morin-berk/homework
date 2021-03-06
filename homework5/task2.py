import functools


def return_doc_name_func_attr(func):
    """
    Wraps a decorator, allowing to return info about
    original function with __doc__, __name__.
    Also returns original func with __original_func.
    """
    def wrapper(dec_func):
        setattr(dec_func, '__doc__', func.__doc__)
        setattr(dec_func, '__name__', func.__name__)
        setattr(dec_func, '__original_func', func)
        return dec_func
    return wrapper


def print_result(func):
    """Allows to print result of a wrapped func
    without print() method"""
    @return_doc_name_func_attr(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result
         of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    without_print = custom_sum.__original_func

    # the result returns without printing
    without_print(1, 2, 3, 4)
