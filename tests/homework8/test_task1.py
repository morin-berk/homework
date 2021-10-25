import tempfile

import pytest

from homework8.task1 import KeyValueStorage


@pytest.fixture()
def temporary_storage() -> str:
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/sample.txt"
    with open(temp_file, "w", encoding='utf8') as f:
        f.write('name=kek\nlast_name=top\npower=9001\n__module__=245')
    return temp_file


@pytest.fixture()
def temporary_storage_with_data_error() -> str:
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/sample.txt"
    with open(temp_file, "w", encoding='utf8') as f:
        f.write('name=kek\nlast_name=top\npower=9001\n1=error')
    return temp_file


def test_int_value_is_always_int(temporary_storage_with_data_error):
    with pytest.raises(ValueError):
        KeyValueStorage(temporary_storage_with_data_error)


@pytest.mark.parametrize('key, expected',
                         [
                             ('name', 'kek'),
                             ('power', 9001)
                         ])
def test_collection_items_access_positive(temporary_storage, key, expected):
    assert KeyValueStorage(temporary_storage)[key] == expected


def test_attributes_access_positive(temporary_storage):
    assert KeyValueStorage(temporary_storage).name == 'kek'
    assert KeyValueStorage(temporary_storage).power == 9001


def test_attribute_clash_builtin_attributes_wins(temporary_storage):
    assert KeyValueStorage(temporary_storage).__module__ == 'homework8.task1'
