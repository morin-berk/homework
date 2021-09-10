from typing import List, Any
from itertools import product


def combinations(*args: List[Any]) -> List[List]:
    """The func takes K lists as arguments and returns all possible
    lists of K items where the first element is from the first list,
    the second is from the second and so one"""
    return list([list(el) for el in list(product(*args))])
