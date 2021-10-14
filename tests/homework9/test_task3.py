import os

from homework9.task3 import universal_file_counter

file_dir = os.path.dirname(__file__)


def test_universal_file_counter_with_tokenizer():
    assert universal_file_counter(file_dir, "txt", str.split) == 7


def test_universal_file_counter_without_tokenizer():
    assert universal_file_counter(file_dir, "txt") == 5
