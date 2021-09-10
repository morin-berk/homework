from typing import List


def get_longest_diverse_words(file_name: str) -> List[str]:
    """
    Finding 10 longest words consisting from largest amount of unique symbols
    """
    words_set = set()
    with open(file_name, encoding='unicode-escape', errors='ignore') as file:
        # Getting a list of unique words
        for el in file:
            words_set.add(el.strip())
        words_set = list(filter(None, words_set))
        words_set = set([word for line in words_set for word in line.split()])
        words_set = set([word.replace('.', '').replace('»', '').
                         replace('«', '').replace('-', '').replace('(', '').
                         replace(')', '').replace(';', '')
                        .replace(':', '').replace(',', '') 
                         for word in words_set])
        # Counting amount of unique letters in each word
        sym_words_dict = {}
        for el in words_set:
            if el not in sym_words_dict:
                sym_words_dict[el] = len(set(el))
        sorted_dict = sorted(sym_words_dict.items(), key=lambda item: item[1])
        largest_words = list(map(lambda x: x[0], sorted_dict))
        return largest_words[-1:-11:-1]


def get_rarest_char(file_name: str) -> str:
    """Finding rarest symbol for document"""
    symbols = {}
    with open(file_name, encoding='unicode-escape', errors='ignore') as file:
        for el in file:
            for sym in el:
                if sym in symbols:
                    symbols[sym] += 1
                else:
                    symbols[sym] = 1
    return min(symbols, key=symbols.get)


def count_punctuation_chars(file_name: str) -> int:
    """Counting every punctuation char"""
    punc_marks = ['.', ',', ':', ';', '?', '!', '(', ')', '{', '}',
                  '`', '/', "'", '"', '[', ']']
    num_of_marks = 0
    with open(file_name, encoding='unicode-escape', errors='ignore') as file:
        for el in file:
            for sym in el:
                if sym in punc_marks:
                    num_of_marks += 1
    return num_of_marks


def count_non_ascii_chars(file_name: str) -> int:
    """Counting every non ascii char"""
    num_of_non_ascii = 0
    with open(file_name, encoding='unicode-escape', errors='ignore') as file:
        for el in file:
            for sym in el:
                if not sym.isascii() and sym != ' ' and sym != '\n':
                    num_of_non_ascii += 1
    return num_of_non_ascii


def get_most_common_non_ascii_char(file_name: str) -> str:
    """Finding most common non ascii char for document"""
    symbols = {}
    with open(file_name, encoding='unicode-escape', errors='ignore') as file:
        for el in file:
            for sym in el:
                if not sym.isascii():
                    if sym in symbols:
                        symbols[sym] += 1
                    else:
                        symbols[sym] = 1
    return max(symbols, key=symbols.get)
