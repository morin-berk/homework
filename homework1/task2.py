from typing import Iterable, Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    The func accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
    """
    def fib_gen(n: int) -> Iterable:
        a, b = 0, 1
        while a <= n:
            yield a
            a, b = b, a + b

    last_el = data[-1]
    l_fib = list(el for el in fib_gen(last_el))
    print(l_fib[::-1])
    if data == [0, 1]:
        return True
    else:
        for el1, el2 in zip(data[::-1], l_fib[::-1]):
            if el1 != el2:
                return False
    return True
