from typing import Iterable, Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    check_fibonacci() accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
    """
    def fib_gen(n: int) -> Iterable:
        a, b = 0, 1
        while a <= n:
            yield a
            a, b = b, a + b

    last_el = data[-1]
    perfect_fib = list(el for el in fib_gen(last_el))

    if len(data) < 3:
        return False
    if data[::-1] != perfect_fib[:-len(data) - 1:-1]:
        return False
    return True
