import os

from homework2.task1 import (count_non_ascii_chars, count_punctuation_chars,
                             get_longest_diverse_words,
                             get_most_common_non_ascii_char, get_rarest_char)

file = os.path.join(os.path.dirname(__file__), 'data.txt')


def test_get_longest_diverse_words():
    assert len(get_longest_diverse_words(file)) == 10


def test_count_punctuation_chars():
    assert count_punctuation_chars(file) > 0


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(file) > 0


def test_get_rarest_char():
    assert get_rarest_char(file) is not None


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(file) is not ascii
