from typing import List, Iterable


def custom_range(iterable: Iterable, *stop: (str, int)) -> List:
    """The function accepts any iterable of unique values
     and then it behaves as range function"""
    if len(stop) == 1:
        return [el for el in iterable if el < stop[0]]
    elif len(stop) == 2:
        return [el for el in iterable if stop[0] <= el < stop[1]]
    elif len(stop) == 3 and stop[2] < 0:
        return [el for el in iterable if stop[1] < el <= stop[0]][::stop[2]]
    elif len(stop) == 3 and stop[2] > 0:
        return [el for el in iterable if stop[0] <= el < stop[1]][::stop[2]]
