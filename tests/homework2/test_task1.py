from homework2.task1 import (count_non_ascii_chars, count_punctuation_chars,
                             get_longest_diverse_words,
                             get_most_common_non_ascii_char, get_rarest_char)


path = '${{ github.workspace }}/hw1/tests/homework2/data.txt'


def test_get_longest_diverse_words():
    assert len(get_longest_diverse_words(path)) == 10


def test_count_punctuation_chars():
    assert count_punctuation_chars(path) > 0


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(path) > 0


def test_get_rarest_char():
    assert get_rarest_char(path) is not None


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(path) is not ascii
