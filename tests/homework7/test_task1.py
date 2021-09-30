import pytest

from homework7.task1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE", []],
    "second": {
        "simple_key": ["simple", "list", True, "of", "RED", "valued", [2, []]],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", set(), "of", "values", {"nested_key": "RED",
                                                         "another_key": []}],
        }
     },
    "fourth": "RED",
    "fifth": [],
    "sixth": ({}, 2, "first"),
    "seventh": True
}


@pytest.mark.parametrize('tree, el, expected',
                         [(example_tree, [], 4),
                          (example_tree, {}, 1),
                          (example_tree, set(), 1)])
def test_find_occurrences_empty_list(tree, el, expected):
    """Testing empty dict, list"""
    assert find_occurrences(tree, el) == expected


def test_find_occurrences_keys():
    """
    Testing if it counts keys,
    and any el if it goes after empty dict, list, etc
    """
    assert find_occurrences(example_tree, "first") == 2


# if I have 1 in example_tree, the test counts it as True
# but it works only in test version, if try to run the same code with
# the same tree in task1.py, it works fine. What`s the matter?
def test_find_occurrences_bool():
    """
    Testing if it counts bool
    """
    assert find_occurrences(example_tree, True) == 2


def test_find_occurrences_values():
    """
    Testing how it works with finding occurrences
    among dict values
    """
    assert find_occurrences(example_tree, "RED") == 6
