from contextlib import contextmanager
from typing import Any


class SupressorClass:
    """
    A context manager, that suppresses passed exception.
    """
    def __init__(self, error):
        self.error = error

    def __enter__(self) -> 'SupressorClass':
        return self

    def __exit__(self, *args) -> tuple[Any, ...]:
        if self.error in args:
            return args


@contextmanager
def supressor_func(error) -> Any:
    """
    A context manager, that suppresses passed exception.
    """
    try:
        yield
    except error:
        pass
