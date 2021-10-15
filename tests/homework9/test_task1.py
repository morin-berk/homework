import tempfile
from typing import List

import pytest

from homework9.task1 import merge_sorted_files


@pytest.fixture()
def temporary_files(data_1: str, data_2: str) -> List[str]:
    """Creates list, containing two txt files with int-s,
    separated by lines."""
    temp_dir = tempfile.gettempdir()
    temp_file_1 = f"{temp_dir}/file1.txt"
    temp_file_2 = f"{temp_dir}/file2.txt"
    with open(temp_file_1, "w", encoding='utf8') as f:
        f.write(data_1)
    with open(temp_file_2, "w", encoding='utf8') as f:
        f.write(data_2)
    return [temp_file_1, temp_file_2]


@pytest.mark.parametrize('data_1, data_2, expected',
                         [
                             ('1\n3\n5', '2\n4\n6',
                              [1, 2, 3, 4, 5, 6]),
                             ('11\n21\n110', '2\n40\n600',
                              [2, 11, 21, 40, 110, 600])
                         ])
def test_merge_sorted_files_positive(temporary_files,
                                     data_1, data_2, expected):
    assert list(merge_sorted_files(temporary_files)) == expected
