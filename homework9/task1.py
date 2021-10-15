from itertools import chain
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Merges integer from sorted files and returns an iterator."""
    file_1 = open(file_list[0], 'r', encoding='utf-8')
    file_2 = open(file_list[1], 'r', encoding='utf-8')
    files = sorted(map(int, chain(file_1, file_2)))
    map(lambda x: x.close(), file_list)

    for line in files:
        yield line
