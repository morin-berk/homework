from collections import defaultdict
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Given an array of size n, the func finds the most common
    and the least common elements"""
    frequency = defaultdict(int)
    for el in inp:
        frequency[el] += 1
    return max(frequency.items(),
               key=lambda item: item[1])[0], min(frequency.items(),
                                                 key=lambda item: item[1])[0]
