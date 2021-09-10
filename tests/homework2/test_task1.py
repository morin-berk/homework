from homework2.task1 import get_longest_diverse_words, \
    count_non_ascii_chars, get_most_common_non_ascii_char, \
    get_rarest_char, count_punctuation_chars


def test_get_longest_diverse_words():
    assert len(get_longest_diverse_words('data.txt')) == 10


def test_count_punctuation_chars():
    assert count_punctuation_chars('data.txt') > 0


def test_count_non_ascii_chars():
    assert count_non_ascii_chars('data.txt') > 0


def test_get_rarest_char():
    assert get_rarest_char('data.txt') is not None


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char('data.txt') is not ascii
