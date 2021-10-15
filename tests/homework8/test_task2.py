import os
import sqlite3

from homework8.task2 import TableData

file = os.path.join(os.path.dirname(__file__), 'example.sqlite')
books = TableData(database_name=file, table_name='books')


def test_table_data_len_method():
    assert len(books) == 3


def test_table_data_getitem_method_existing_item():
    assert books['Huxley'] == ('Brave New World', 'Huxley')
    assert books['1984'] == ('1984', 'Orwell')


def test_table_data_getitem_method_nonexisting_item():
    assert not books['Some_book']


def test_table_data_contains_method():
    assert 'Huxley' in books
    assert 'Someone' not in books


def test_table_data_is_iterable():
    book_list = []
    for book in books:
        book_list.append(book['author'])
    assert book_list == ['Bradbury', 'Huxley', 'Orwell']


def test_table_data_class_works_with_updated_data():
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books VALUES ("We", "Zamyatin")')
    conn.commit()

    assert len(books) == 4

    cursor.execute('DELETE FROM books WHERE name="We"')
    conn.commit()

    assert len(books) == 3
