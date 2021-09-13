from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    The function reads input line-by-line,
    and returns a tuple with the maximum and minimum values
    """
    numbers = [int(el.strip()) for el in open(file_name, encoding='utf8')]
    return max(numbers), min(numbers)
