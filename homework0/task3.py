from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    The function reads input line-by-line,
    and returns a tuple with the maximum and minimum values
    """
    min_num = 0
    max_num = 0
    with open(file_name) as fi:
        for el, line in enumerate(fi):
            if el == 0:
                min_num = int(line)
                max_num = int(line)
            elif int(line) < min_num:
                min_num = int(line)
            elif int(line) > max_num:
                max_num = int(line)
    return max_num, min_num
