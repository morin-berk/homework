from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Given an array of size n, the func finds the most common
    and the least common elements """
    frequency = {}
    for el in inp:
        if el in frequency:
            frequency[el] += 1
        else:
            frequency[el] = 1
    sorted_freq = sorted(frequency.items(), key=lambda item: item[1])
    fr = list(map(lambda x: x[0], sorted_freq))
    return fr[-1], fr[0]
