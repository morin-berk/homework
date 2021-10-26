import os

import pytest

from homework8.task2 import TableData

file = os.path.join(os.path.dirname(__file__), 'example.sqlite')


def test_table_data_len_method():
    with TableData(database_name=file, table_name='books') as books:
        assert len(books) == 3


def test_table_data_getitem_method_existing_item():
    with TableData(database_name=file, table_name='books') as books:
        assert books['Huxley'] == ('Brave New World', 'Huxley')
        assert books['Orwell'] == ('1984', 'Orwell')


def test_table_data_getitem_method_nonexisting_item():
    with pytest.raises(TypeError):
        with TableData(database_name=file, table_name='books') as books:
            assert books['Some_book']


def test_table_data_contains_method():
    with TableData(database_name=file, table_name='books') as books:
        assert 'Huxley' in books


def test_table_data_is_iterable():
    with TableData(database_name=file, table_name='books') as books:
        book_list = []
        for book in books:
            book_list.append(book['author'])
        assert book_list == ['Bradbury', 'Huxley', 'Orwell']
