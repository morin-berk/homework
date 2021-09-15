import tempfile

import pytest

from homework4.task1 import read_magic_number


@pytest.fixture()
def temporary_file(data) -> str:
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/sample.txt"
    with open(temp_file, "w") as f:
        f.write(data)
    return temp_file


@pytest.mark.parametrize('data, expected',
                         [('1', True), ('2', True)])
def test_read_magic_number_positive_test(temporary_file, data, expected):
    """
    Checking the case when the first line data belongs to [1, 3)
    """
    assert read_magic_number(temporary_file) is expected


@pytest.mark.parametrize('data, expected',
                         [('3', False), ('-2', False)])
def test_read_magic_number_negative_test(temporary_file, data, expected):
    """
    Checking the case when the first line data does not belong to [1, 3)
    """
    assert read_magic_number(temporary_file) is expected


@pytest.mark.parametrize('data', ['This is str not int'])
def test_read_magic_number_negative_errors(temporary_file, data):
    """
    Checking whether the func raises ValueError
    if the first line data is not int
    """
    with pytest.raises(ValueError):
        read_magic_number(temporary_file)
