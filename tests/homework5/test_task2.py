import functools

from homework5.task2 import print_result


def test_decorator_returns_doc_name_func_of_origin_func():
    """
    Check if a func, decorated with @print_result, returns
    its original __doc__, __name__, and returns itself with
    __original_func method
    """
    @print_result
    def custom_sum(*args):
        """This function can sum any objects which have __add___"""
        return functools.reduce(lambda x, y: x + y, args)

    custom_sum([1, 2, 3], [4, 5])
    without_print = custom_sum.__original_func
    assert custom_sum.__doc__ == 'This function can ' \
                                 'sum any objects which have __add___'
    assert custom_sum.__name__ == 'custom_sum'
    assert without_print(1, 2, 3, 4) == 10
