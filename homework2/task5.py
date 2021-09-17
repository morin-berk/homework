from typing import Iterable, List


def custom_range(iterable: Iterable, *slices: (str, int)) -> List:
    """The function accepts any iterable of unique values,
    slice(stop) / slice(start, stop) / slice(start, stop, step)
    and then it behaves as range function"""
    if len(slices) == 1:
        return [el for el in iterable if el < slices[0]]
    elif len(slices) == 2:
        return [el for el in iterable if slices[0] <= el < slices[1]]
    elif len(slices) == 3 and slices[2] < 0:
        return [el for el in iterable if slices[1] < el <= slices[0]][::slices[2]]
    elif len(slices) == 3 and slices[2] > 0:
        return [el for el in iterable if slices[0] <= el < slices[1]][::slices[2]]
