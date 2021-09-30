from copy import deepcopy
from typing import List


def backspace_compare(first: str, second: str) -> bool:
    """
    Given two strings, the func returns if they are equal
    when both are typed into empty text editors.
    """
    first, second = list(first), list(second)
    first_copy, second_copy = deepcopy(first), deepcopy(second)

    def clear_lists(array: List[str], copy_array) -> List[str]:
        """
        Returns lists clear from backspaces and symbols which
        backspaces delete.
        """
        clean_list = []
        if len(array) == 1 and array[0] != '#':
            clean_list.append(array[0])
        for el in range(len(copy_array) - 1):
            if array[el] == '#' and array[el + 1] == '#':
                continue
            elif array[el] == '#' and array[el + 1] != '#':
                clean_list.append(array[el + 1])
            elif array[el] != '#' and array[el + 1] == '#':
                if clean_list:
                    clean_list.pop()
            else:
                clean_list.append(array[el])
                clean_list.append(array[el + 1])
        return clean_list
    return clear_lists(first, first_copy) == clear_lists(second, second_copy)
