import functools


def instances_counter(cls):
    """
    Decorator counts how many class objects are created,
    and adds two methods to a decorated class -
    get_created_instances and reset_instances_counter.
    The first returns number of created objects,
    the second returns number of created objects and
    reloads the object`s counter.
    >>> User.get_created_instances()
    0
    >>> user, _, _ = User(), User(), User()
    >>> user.get_created_instances()
    3
    >>> user.reset_instances_counter()
    3
    """
    @functools.wraps(cls, updated=())
    class Wrapper(cls):
        _counter = 0

        def __new__(cls, *args, **kwargs):
            instance = super().__new__(cls)
            Wrapper._counter += 1
            return instance

        @classmethod
        def get_created_instances(cls) -> int:
            """Returns number of created objects"""
            return cls._counter

        @classmethod
        def reset_instances_counter(cls) -> int:
            """
            returns number of created objects and
            reloads the object`s counter
            """
            result = cls._counter
            cls._counter = 0
            return result

    return Wrapper


@instances_counter
class User:
    """An experimental class"""


if __name__ == '__main__':
    import doctest
    doctest.testmod()
