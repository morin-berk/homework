from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    The func takes a number N as an input
    and returns N FizzBuzz numbers
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz',\
 'buzz', '11', 'fizz', '13', '14', 'fizz buzz']
     >>> fizzbuzz(-1)
     Traceback (most recent call last):
     ...
     ValueError: n must be > 0
    """
    fizz_buzz_list = []
    if n <= 0:
        raise ValueError('n must be > 0')
    for el in range(1, n + 1):
        if el % 3 == 0 and el % 5 == 0:
            fizz_buzz_list.append('fizz buzz')
        elif el % 3 == 0:
            fizz_buzz_list.append('fizz')
        elif el % 5 == 0:
            fizz_buzz_list.append('buzz')
        else:
            fizz_buzz_list.append(str(el))
    return fizz_buzz_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
