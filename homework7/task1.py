from typing import Any, Iterable

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    """
        Takes nested dict, element,
        and finds number of element occurrences
    """
    counter = 0

    def find_occurrences_recursive(tree: Iterable, el: Any) -> Iterable:
        """
        Recursive func walks through any(dict, set, tuple, list)
        and counts number of element occurrences with
        nonlocal counter
        """
        nonlocal counter

        if isinstance(tree, dict):
            for key, value in tree.items():
                if key == el:
                    counter += 1
                if value == el:
                    counter += 1
                elif isinstance(value, (dict, list, set, tuple)):
                    return find_occurrences_recursive(value, el)
        elif isinstance(tree, (list, set, tuple)):
            for iterable in tree:
                if iterable == el:
                    counter += 1
                elif isinstance(iterable, (list, set, tuple, dict))\
                        and iterable:
                    return find_occurrences_recursive(iterable, el)

    for key, value in tree.items():
        if key == element:
            counter += 1
        if value == element:
            counter += 1
        elif isinstance(value, (dict, list, set, tuple)):
            find_occurrences_recursive(value, element)
    return counter


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
