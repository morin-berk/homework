from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    check_fibonacci() accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
    """
    if len(data) < 3:
        return False

    def _check_window(x: int, y: int, z: int) -> bool:
        return (x + y) == z

    a, b, c = data[0], data[1], data[2]

    while data:
        if not _check_window(a, b, c):
            return False
        if len(data) > 3:
            a, b, c = b, c, data[3]
            data = data[1:]
    return True
